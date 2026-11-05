"""One function per lecture step. Each takes a driver and does one job."""

import logging
from collections.abc import Callable
from time import sleep

from selenium.common.exceptions import (
    ElementClickInterceptedException,
    ElementNotInteractableException,
    NoSuchElementException,
    TimeoutException,
    WebDriverException,
)
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait

from tinder_bot import locators
from tinder_bot.config import Settings

log = logging.getLogger(__name__)


def _click_when_ready(
    driver: WebDriver, locator: locators.Locator, timeout: float
) -> None:
    """Wait until the element is clickable, then click it."""
    WebDriverWait(driver, timeout).until(ec.element_to_be_clickable(locator)).click()


def open_login_page(driver: WebDriver, settings: Settings) -> None:
    """Step 2: open the site, press LOG IN, then LOG IN WITH FACEBOOK."""
    driver.get(settings.url)
    _click_when_ready(driver, locators.LOGIN_BUTTON, settings.timeout)
    _click_when_ready(driver, locators.FACEBOOK_BUTTON, settings.timeout)


def sign_in_with_facebook(driver: WebDriver, settings: Settings) -> None:
    """Fill the Facebook pop-up window and return to the main window."""
    main = driver.current_window_handle
    WebDriverWait(driver, settings.timeout).until(lambda d: len(d.window_handles) > 1)
    popup = next(h for h in driver.window_handles if h != main)
    driver.switch_to.window(popup)
    driver.find_element(*locators.FACEBOOK_EMAIL).send_keys(settings.facebook_email)
    password = driver.find_element(*locators.FACEBOOK_PASSWORD)
    password.send_keys(settings.facebook_password)
    password.submit()
    driver.switch_to.window(main)


def dismiss_requests(driver: WebDriver, settings: Settings) -> None:
    """Step 4: ALLOW location, NOT INTERESTED notifications, I ACCEPT cookies."""
    for locator in (
        locators.ALLOW_LOCATION,
        locators.NOT_INTERESTED,
        locators.ACCEPT_COOKIES,
    ):
        try:
            _click_when_ready(driver, locator, settings.timeout)
        except TimeoutException:
            log.warning("Pop-up not shown, skipping: %s", locator[1])


def like_once(
    driver: WebDriver,
    settings: Settings,
    pause: Callable[[float], None] = sleep,
) -> None:
    """Click Like once, waiting out loading and dismissing match pop-ups.

    A missing or still hidden (not interactable) button counts as loading.
    """
    while True:
        try:
            driver.find_element(*locators.LIKE_BUTTON).click()
            return
        except (NoSuchElementException, ElementNotInteractableException):
            pause(settings.retry_delay)
        except ElementClickInterceptedException:
            try:
                driver.find_element(*locators.BACK_TO_TINDER).click()
            except NoSuchElementException:
                pause(settings.retry_delay)


def like_profiles(
    driver: WebDriver,
    settings: Settings,
    pause: Callable[[float], None] = sleep,
) -> int:
    """Step 5: like up to ``max_likes`` profiles; return how many were liked."""
    liked = 0
    for _ in range(settings.max_likes):
        try:
            like_once(driver, settings, pause)
        except WebDriverException:
            log.exception("Stopping after %d likes", liked)
            break
        liked += 1
        pause(settings.like_delay)
    return liked
