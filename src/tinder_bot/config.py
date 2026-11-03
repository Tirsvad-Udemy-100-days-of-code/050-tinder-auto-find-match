"""Settings read from environment variables."""

import os
from dataclasses import dataclass

DEFAULT_URL = "https://app.100daysofpython.dev/"


@dataclass(frozen=True)
class Settings:
    """Everything the bot needs from the outside world."""

    url: str = DEFAULT_URL
    facebook_email: str = ""
    facebook_password: str = ""
    max_likes: int = 20
    like_delay: float = 1.5
    retry_delay: float = 2.0
    timeout: float = 10.0

    @classmethod
    def from_env(cls) -> "Settings":
        """Build settings from the environment; unset values keep defaults."""
        return cls(
            url=os.getenv("TINDER_URL", DEFAULT_URL),
            facebook_email=os.getenv("FACEBOOK_EMAIL", ""),
            facebook_password=os.getenv("FACEBOOK_PASSWORD", ""),
            max_likes=int(os.getenv("MAX_LIKES", "20")),
        )
