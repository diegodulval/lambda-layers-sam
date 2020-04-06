import os
from aws_xray_sdk.core import xray_recorder, patch_all

from persistence.Dynamo import Dynamo
from Logging import get_logger

logger = get_logger()
patch_all()

if "DEBUG" in os.environ:
    from helpers import start_debbuger

    start_debbuger()


def get_event_user(event):
    return {
        "FirstName": event["name"],
        "LastName": event["lastname"],
        "Age": event["age"],
    }


def define_xray_subsegment(name, function, arg):
    xray_recorder.begin_subsegment(name)
    response = function(arg)
    xray_recorder.end_subsegment()
    return response


@xray_recorder.capture("lambda_handler")
def lambda_handler(event, context):
    user = get_event_user(event)

    def save_user(user):
        endpoint_url = (
            os.environ["DATABSE_URL"] if "DATABASE_URL" in os.environ else None
        )
        dynamo = Dynamo(endpoint_url=endpoint_url,
                        tablename=os.environ["TABLE"])
        created_user = dynamo.create(item=user)
        logger.info("Success to create and find user")
        return created_user

    user_created = define_xray_subsegment("save_user", save_user, user)
    return user_created
