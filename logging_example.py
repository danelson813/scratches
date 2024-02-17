import logging


logger = logging.getLogger('my_app')
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler = logging.FileHandler('my_app.log')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

logger.warning('This is a warning')
logger.info('This is info about the app')