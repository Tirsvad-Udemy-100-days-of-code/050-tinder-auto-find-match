"""Run the bot against the static mock TinDog site and screenshot each step.

Usage: ``python tests/e2e/run_e2e.py --out /out``. Run it in the Docker
container (see README.md), never on the host desktop.
"""

import argparse
import logging
import sys
import threading
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from time import sleep

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "src"))

from tinder_bot import locators  # noqa: E402
from tinder_bot.config import Settings  # noqa: E402
from tinder_bot.driver import create_driver  # noqa: E402
from tinder_bot.steps import like_once, sign_in_with_facebook  # noqa: E402

SITE_DIR = Path(__file__).resolve().parent / "site"
LIKING_SHOT_AFTER = 2
MATCH_EVERY = 4  # must equal MATCH_EVERY in site/app.js

log = logging.getLogger("e2e")


class QuietHandler(SimpleHTTPRequestHandler):
    """Static file handler that does not log each request."""

    def log_message(self, format: str, *args: object) -> None:  # noqa: A002
        return


def start_server() -> tuple[ThreadingHTTPServer, str]:
    """Serve the mock site on a free port; return the server and its URL."""
    handler = partial(QuietHandler, directory=str(SITE_DIR))
    server = ThreadingHTTPServer(("127.0.0.1", 0), handler)
    threading.Thread(target=server.serve_forever, daemon=True).start()
    return server, f"http://127.0.0.1:{server.server_address[1]}/index.html"


def shoot(driver: WebDriver, out: Path, name: str) -> None:
    """Save a screenshot of the current window as ``name``."""
    driver.save_screenshot(str(out / name))
    log.info("saved %s", out / name)


def wait_visible(driver: WebDriver, locator: locators.Locator, timeout: float) -> None:
    WebDriverWait(driver, timeout).until(ec.visibility_of_element_located(locator))


def click(driver: WebDriver, locator: locators.Locator, timeout: float) -> None:
    WebDriverWait(driver, timeout).until(ec.element_to_be_clickable(locator)).click()


def shoot_popup(driver: WebDriver, out: Path, timeout: float) -> None:
    """Screenshot the Facebook window, then return to the main window."""
    main = driver.current_window_handle
    WebDriverWait(driver, timeout).until(lambda d: len(d.window_handles) > 1)
    popup = next(h for h in driver.window_handles if h != main)
    driver.switch_to.window(popup)
    wait_visible(driver, locators.FACEBOOK_EMAIL, timeout)
    shoot(driver, out, "03-facebook-popup.png")
    driver.switch_to.window(main)


def like_all(driver: WebDriver, settings: Settings, out: Path) -> int:
    """Like ``max_likes`` profiles, screenshotting mid-run and the match pop-up."""
    liked = 0
    match_shot_taken = False
    while liked < settings.max_likes:
        like_once(driver, settings, sleep)
        liked += 1
        if liked == LIKING_SHOT_AFTER:
            shoot(driver, out, "07-liking.png")
        if liked % MATCH_EVERY == 0 and not match_shot_taken:
            wait_visible(driver, locators.BACK_TO_TINDER, settings.timeout)
            shoot(driver, out, "08-match-popup.png")
            match_shot_taken = True
        sleep(settings.like_delay)
    shoot(driver, out, "09-done.png")
    return liked


def run(out: Path) -> int:
    """Drive the whole flow against the mock site; return the likes given."""
    server, url = start_server()
    settings = Settings(
        url=url,
        facebook_email="bot@example.com",
        facebook_password="not-a-real-password",
        like_delay=0.2,
        retry_delay=0.5,
    )
    driver = create_driver(headless=True)
    try:
        driver.get(settings.url)
        wait_visible(driver, locators.LOGIN_BUTTON, settings.timeout)
        shoot(driver, out, "01-home.png")
        click(driver, locators.LOGIN_BUTTON, settings.timeout)
        wait_visible(driver, locators.FACEBOOK_BUTTON, settings.timeout)
        shoot(driver, out, "02-login-modal.png")
        click(driver, locators.FACEBOOK_BUTTON, settings.timeout)
        shoot_popup(driver, out, settings.timeout)
        sign_in_with_facebook(driver, settings)
        for locator, name in (
            (locators.ALLOW_LOCATION, "04-location.png"),
            (locators.NOT_INTERESTED, "05-notifications.png"),
            (locators.ACCEPT_COOKIES, "06-cookies.png"),
        ):
            wait_visible(driver, locator, settings.timeout)
            shoot(driver, out, name)
            click(driver, locator, settings.timeout)
        return like_all(driver, settings, out)
    finally:
        driver.quit()
        server.shutdown()


def main() -> int:
    """Parse arguments, run the flow and return the process exit code."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out", type=Path, required=True, help="screenshot directory")
    args = parser.parse_args()
    logging.basicConfig(level=logging.INFO)
    args.out.mkdir(parents=True, exist_ok=True)
    liked = run(args.out)
    log.info("liked %d profiles", liked)
    return 0 if liked == Settings().max_likes else 1


if __name__ == "__main__":
    sys.exit(main())
