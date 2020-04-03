import ptvsd
import sys
import logging


def start_debbuger():
    ptvsd.enable_attach(address=('0.0.0.0', 5678), redirect_output=True)
    print('waiting for debugger to attach...')
    sys.stdout.flush()
    ptvsd.wait_for_attach()


def start_logger():
    print('Loading function')
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    return logger
