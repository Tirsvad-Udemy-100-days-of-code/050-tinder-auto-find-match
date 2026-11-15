[English](Getting-Started) · **Dansk** · [Bahasa Melayu](Getting-Started-ms)

# Kom godt i gang

## Krav

Python 3.11 eller nyere og Google Chrome (Selenium Manager henter selv en passende driver). Den eneste afhængighed ved kørsel er `selenium`; kontrollerne bruger `pytest` og `ruff`. Docker skal kun bruges til den valgfrie end-to-end-kørsel.

## Opsætning

```bash
git clone https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/050-tinder-auto-find-match.git
cd 050-tinder-auto-find-match
python -m venv .venv
source .venv/Scripts/activate   # Windows Git Bash; Linux/macOS: .venv/bin/activate
pip install -e ".[dev]"
cp .env.example .env
```

## Kør

```bash
python -m tinder_bot
```

Det åbner siden i Chrome, logger ind via Facebook-popuppen, lukker popup'erne om lokation, notifikationer og cookies og liker profiler, højst `MAX_LIKES` (som standard 20). Det kræver en internetforbindelse og indstillinger i miljøet (`FACEBOOK_EMAIL`, `FACEBOOK_PASSWORD`; filen `.env.example` nævner dem). Brug det kun med kursets øvelsesside TinDog og en testkonto, aldrig med en rigtig konto.

## Ansvarlig brug

Automatisering af en tredjepartstjeneste kan overtræde dens brugsvilkår, og de profiler, som botten liker, tilhører andre mennesker. Programmet er skrevet til kursets øvelsesside TinDog. Vær ærlig over for dem, du dater: fortæl dem, at du automatiserer dine swipes, og hold dig til den daglige grænse (TinDog 20, Tinder gratis 100). Læg aldrig en rigtig adgangskode eller anden legitimation i repositoriet.

## Tests

```bash
python -m pytest
```

Enhedstestene i `tests/unit/` bruger en falsk driver, så de åbner ingen browser og kontakter ingen side.

## Licens

Koden er udgivet under licensen GNU Affero General Public License v3.0 only (AGPL-3.0-only). Se filen `LICENSE`.
