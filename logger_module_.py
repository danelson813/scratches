import logging
import colorlog


logger = logging.getLogger("my_logger")
logger.setLevel(logging.NOTSET)

file_handler = logging.FileHandler("info.log")
file_handler.setLevel(logging.INFO)
file_handler.setFormatter(logging.Formatter("%(white)%(asctime)s%(reset)s | %(log_color)%(pathname)s%(reset)s - %(lineno)d | %(levelname)s: %(log_color)%(message)s%(reset)s"))
logger.addHandler(file_handler)

stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.ERROR)
stream_handler.setFormatter(logging.Formatter("%(asctime)s | %(levelname)s: %(message)s"))
logger.addHandler(stream_handler)

logger.info("This is an info message")
logger.error("This is an error message")
logger.warning("This is a warning message")
logger.debug("This is a debug message")
logger.critical("This is a critical message")
