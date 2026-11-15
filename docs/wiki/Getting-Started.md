**English** · [Dansk](Getting-Started-da) · [Bahasa Melayu](Getting-Started-ms)

# Getting Started

## Requirements

Python 3.11 or newer and Google Chrome (Selenium Manager downloads a matching driver by itself). The only runtime dependency is `selenium`; the checks use `pytest` and `ruff`. Docker is needed only for the optional end-to-end run.

## Setup

```bash
git clone https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/050-tinder-auto-find-match.git
cd 050-tinder-auto-find-match
python -m venv .venv
source .venv/Scripts/activate   # Windows Git Bash; Linux/macOS: .venv/bin/activate
pip install -e ".[dev]"
cp .env.example .env
```

## Run

```bash
python -m tinder_bot
```

This opens the site in Chrome, logs in through the Facebook pop-up, dismisses the location, notification and cookie pop-ups and likes profiles, at most `MAX_LIKES` (20 by default). It needs an internet connection and settings in the environment (`FACEBOOK_EMAIL`, `FACEBOOK_PASSWORD`; the file `.env.example` lists them). Use it only with the course's practice site TinDog and a test account, never with a real account.

## Responsible use

Automating a third-party service may violate its terms of use, and the profiles that the bot likes belong to other people. The program is written for the course's practice site TinDog. Be honest with the people you date: tell them that you automate your swiping, and keep to the daily limit (TinDog 20, Tinder free tier 100). Never put a real credential in the repository.

## Tests

```bash
python -m pytest
```

The unit tests in `tests/unit/` use a fake driver, so they open no browser and contact no site.

## Licence

The code is licensed under the GNU Affero General Public License v3.0 only (AGPL-3.0-only). See the `LICENSE` file.
