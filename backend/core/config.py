import os
import logging
from dotenv import load_dotenv
from logging.handlers import RotatingFileHandler

Base_Dir = os.getenv('')
load_dotenv()

LOG_LEVEL = os.getenv("LOG_INFO", "INFO").upper()


logger = logging.getLogger(__name__)
logger.setLevel(getattr(logging, LOG_LEVEL, logging.INFO))


formatter = logging.Formatter(
    "%(asctime)s | %(levelname)s |%(name)s | %(message)s ",
    datefmt= "%y-%m-%d %H:%M:%S"
)

console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)


file_handler = RotatingFileHandler("app.log",
                                   maxBytes = 5_00_000 ,
                                   backupCount= 3)

file_handler.setFormatter(formatter)


if not logging.hasHandlers():
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)


class Config :
    DATABASE_URI = 'sqllite:///./test.db'
    



