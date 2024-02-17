import logging
import time

# Setup logging
logger = logging.getLogger('task_runner')
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler('task_runner.log')
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)


logger.info("Task started")
try:
    # Some magic happens here
    time.sleep(2)
    # And then the error occurs, so we can give a MS style error message to piss everyone off
    raise ValueError("Something went wrong") # Don't be like them in the real world
except Exception as e:
    logger.error(f"Task failed: {e}")
else:
    logger.info("Task completed successfully")
finally:
    logger.info("Task ended")