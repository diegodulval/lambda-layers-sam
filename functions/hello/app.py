import os
from aws_xray_sdk.core import xray_recorder

from Dynamo import Dynamo

from helpers import start_debbuger, start_logger

table_name = os.environ["TABLE"]
aws_environment = os.environ["AWSENV"]
is_local_env = aws_environment == "LOCAL"

logger = start_logger()

if aws_environment == "DEBUG":
    start_debbuger()


def respond(err, res=None):
    return {
        "statusCode": "400" if err else "200",
        "body": err if err else res,
        "headers": {"Content-Type": "application/json"},
    }


@xray_recorder.capture("lambda_handler")
def lambda_handler(event, context):
    user = {"FirstName": "Ditinho", "LastName": "Due", "Age": 24}
    try:
        xray_recorder.begin_subsegment("dynamo_layer")
        dynamo = Dynamo(is_local_env=is_local_env, tablename=table_name)
        PersonId = dynamo.create(item=user)
        item = dynamo.read_by_id(id=PersonId)
        logger.info("Success to create and find user")
        xray_recorder.end_subsegment()
        return respond(None, {"user": item})
    except Exception as e:
        logger.error(e)
        return respond("Failed")
