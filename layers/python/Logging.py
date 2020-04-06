import logging


def get_logger():
    print("Loading function")
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    return logger
