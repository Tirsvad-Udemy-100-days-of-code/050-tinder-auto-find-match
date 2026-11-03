"""XPath locators for the elements the lecture steps target."""

from selenium.webdriver.common.by import By

Locator = tuple[str, str]

LOGIN_BUTTON: Locator = (By.XPATH, '//*[normalize-space(text())="Log in"]')
FACEBOOK_BUTTON: Locator = (
    By.XPATH,
    '//button[contains(normalize-space(.), "Log in with Facebook")]',
)
FACEBOOK_EMAIL: Locator = (By.ID, "email")
FACEBOOK_PASSWORD: Locator = (By.ID, "pass")

ALLOW_LOCATION: Locator = (By.XPATH, '//button[normalize-space(.)="Allow"]')
NOT_INTERESTED: Locator = (By.XPATH, '//button[normalize-space(.)="Not interested"]')
ACCEPT_COOKIES: Locator = (By.XPATH, '//button[normalize-space(.)="I accept"]')

LIKE_BUTTON: Locator = (By.XPATH, '//button[@aria-label="Like"]')
BACK_TO_TINDER: Locator = (By.XPATH, '//button[normalize-space(.)="Back to Tinder"]')
