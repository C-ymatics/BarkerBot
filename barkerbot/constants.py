import os

from loguru import logger

try:
    import dotenv
except ModuleNotFoundError:
    pass
else:
    if dotenv.find_dotenv():
        logger.info("Found .env file, loading environment variables")

        dotenv.load_dotenv(override=True)


__all__ = ("Config",)


class Config:
    token = os.getenv("DEV") if os.name == "nt" else os.getenv("TOKEN")
