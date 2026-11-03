# End-to-end run against a mock TinDog

`site/` is a static mock of the TinDog flow (home, login modal, fake Facebook
popup, location / notifications / cookies pop-ups, cards with a 2 s loading
delay, a match modal every 4th like, stop at 20 likes). `run_e2e.py` serves it
with `http.server`, drives the bot with headless Chrome and saves one
screenshot per step (`01-home.png` ... `09-done.png`).

Run it in Docker only, never on the host desktop. From the project root:

```bash
docker build -f tests/e2e/Dockerfile -t tinder-e2e .
docker run --rm -v "$PWD/e2e-out:/out" tinder-e2e
```

The screenshots appear in `e2e-out/`. The exit code is 0 when 20 likes were
given.

If Chrome fails to start as root in the container, `create_driver` already
passes `--no-sandbox`; add `--shm-size=1g` to `docker run` if it crashes.
