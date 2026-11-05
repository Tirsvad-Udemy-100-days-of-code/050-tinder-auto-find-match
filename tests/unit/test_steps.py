from unittest.mock import MagicMock

import pytest
from selenium.common.exceptions import (
    ElementClickInterceptedException,
    ElementNotInteractableException,
    NoSuchElementException,
)

from tinder_bot import locators
from tinder_bot.config import Settings
from tinder_bot.steps import like_once, like_profiles


def test_like_once_retries_while_loading() -> None:
    driver = MagicMock()
    button = MagicMock()
    driver.find_element.side_effect = [NoSuchElementException(), button]
    pauses: list[float] = []

    like_once(driver, Settings(), pauses.append)

    button.click.assert_called_once()
    assert pauses == [2.0]


def test_like_once_retries_while_button_hidden() -> None:
    driver = MagicMock()
    hidden, button = MagicMock(), MagicMock()
    hidden.click.side_effect = ElementNotInteractableException()
    driver.find_element.side_effect = [hidden, button]
    pauses: list[float] = []

    like_once(driver, Settings(), pauses.append)

    button.click.assert_called_once()
    assert pauses == [2.0]


def test_like_once_dismisses_match_popup() -> None:
    driver = MagicMock()
    like, back = MagicMock(), MagicMock()
    like.click.side_effect = [ElementClickInterceptedException(), None]
    driver.find_element.side_effect = lambda by, value: (
        back if value == locators.BACK_TO_TINDER[1] else like
    )

    like_once(driver, Settings(), lambda _: None)

    back.click.assert_called_once()
    assert like.click.call_count == 2


def test_like_profiles_stops_at_max_and_pauses_between_likes() -> None:
    driver = MagicMock()
    pauses: list[float] = []

    liked = like_profiles(driver, Settings(max_likes=3), pauses.append)

    assert liked == 3
    assert pauses == [1.5, 1.5, 1.5]


def test_settings_from_env(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("MAX_LIKES", "5")
    monkeypatch.setenv("FACEBOOK_EMAIL", "a@b.c")

    settings = Settings.from_env()

    assert settings.max_likes == 5
    assert settings.facebook_email == "a@b.c"
