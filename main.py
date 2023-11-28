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
    REPO_SECRET = os.environ["REPO_SECRET"]
except KeyError:
    REPO_SECRET = "Token not available!"
    # logger.info("Token not available!")
    # raise


if __name__ == "__main__":
    logger.info(f"Token value: {REPO_SECRET}")

    r = requests.get(
        "https://weather.talkpython.fm/api/weather/?city=Chennai&country=IN"
    )
    if r.status_code == 200:
        data = r.json()
        temperature = data["forecast"]["temp"]
        logger.info(f"Weather in Chennai, India: {temperature}")
