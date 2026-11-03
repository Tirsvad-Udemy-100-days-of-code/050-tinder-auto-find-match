FROM python:3.12-slim

RUN apt-get update \
    && apt-get install -y --no-install-recommends chromium chromium-driver fonts-liberation \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir "selenium>=4.20"

WORKDIR /app
COPY src ./src
COPY tests/e2e ./tests/e2e

# Selenium finds /usr/bin/chromedriver on PATH; point it at the distro Chromium.
ENV CHROME_BIN=/usr/bin/chromium
VOLUME /out
ENTRYPOINT ["python", "tests/e2e/run_e2e.py", "--out", "/out"]
