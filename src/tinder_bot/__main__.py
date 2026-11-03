"""Run with ``python -m tinder_bot``."""

import logging
from pathlib import Path

from tinder_bot.config import Settings
from tinder_bot.driver import create_driver
from tinder_bot.steps import (
    dismiss_requests,
    like_profiles,
    open_login_page,
    sign_in_with_facebook,
)


def main() -> None:
    """Log in, dismiss pop-ups and like profiles."""
    logging.basicConfig(level=logging.INFO)
    settings = Settings.from_env()
    driver = create_driver(profile_dir=Path(".data").resolve())
    try:
        open_login_page(driver, settings)
        sign_in_with_facebook(driver, settings)
        dismiss_requests(driver, settings)
        like_profiles(driver, settings)
    finally:
        driver.quit()


if __name__ == "__main__":
    main()
