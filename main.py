import logging
import logging.handlers
import os

import requests

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger_file_handler = logging.handlers.RotatingFileHandler(
    "status.log",
    maxBytes=1024 * 1024,
    backupCount=1,
    encoding="utf8",
)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
logger_file_handler.setFormatter(formatter)
logger.addHandler(logger_file_handler)

try:
    SOME_SECRET = os.environ["SOME_SECRET"]
except KeyError:
    SOME_SECRET = "Token not available!"
    # logger.info("Token not available!")
    # raise


def log_city_weather():
    logger.info(f"Token value: {SOME_SECRET}")

    r = requests.get(
        "https://weather.talkpython.fm/api/weather/?city=Bengaluru&country=IN"
    )
    if r.status_code == 200:
        data = r.json()
        temperature = data["forecast"]["temp"]
        weather = data["weather"]["description"]
        logger.info(f"Temperature in Bengaluru is: {temperature} °C")
        logger.info(f"Weather is: {weather}")


def log_random_quote():

    r = requests.get("https://parks-and-rec-api.frozencoast05.workers.dev/quote/random")

    if r.status_code == 200:
        data = r.json()
        character = data["character"]
        quote = data["quote"]
        logger.info("Quote for today")
        logger.info(f"{quote} - {character}")


def main():
    log_city_weather()
    log_random_quote()


if __name__ == "__main__":
    main()
