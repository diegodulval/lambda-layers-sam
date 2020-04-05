import sys
import logging
from aws_xray_sdk.core import patch_all


def start_debbuger():
    import ptvsd

    ptvsd.enable_attach(address=("0.0.0.0", 5678), redirect_output=True)
    print("waiting for debugger to attach...")
    sys.stdout.flush()
    ptvsd.wait_for_attach()


def start_logger():
    print("Loading function")
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    patch_all()
    return logger
