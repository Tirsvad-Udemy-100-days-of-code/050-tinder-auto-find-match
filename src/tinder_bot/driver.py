"""Browser factory."""

from pathlib import Path

from selenium import webdriver


def create_driver(
    *, headless: bool = False, profile_dir: Path | None = None
) -> webdriver.Chrome:
    """Create a Chrome driver; a profile dir keeps the login between runs."""
    options = webdriver.ChromeOptions()
    options.add_argument("--lang=en")
    options.add_argument("--window-size=1280,900")
    if headless:
        options.add_argument("--headless=new")
        options.add_argument("--no-sandbox")
    if profile_dir is not None:
        options.add_argument(f"--user-data-dir={profile_dir}")
    return webdriver.Chrome(options=options)
