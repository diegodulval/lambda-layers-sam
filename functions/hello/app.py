from Dynamo import Dynamo
from helpers import start_debbuger, start_logger
import os


table_name = os.environ["TABLE"]
aws_environment = os.environ["AWSENV"]
dev_environment = os.environ["DEVENV"]

logger = start_logger()

if aws_environment == "LOCAL":
    start_debbuger()

print(aws_environment)


def respond(err, res=None):
    return {
        "statusCode": "400" if err else "200",
        "body": err if err else res,
        "headers": {"Content-Type": "application/json"},
    }


def lambda_handler(event, context):
    user = {"FirstName": "Ditinho", "LastName": "Due", "Age": 24}
    try:
        dynamo = Dynamo(env=aws_environment == "LOCAL", tablename=table_name)
        PersonId = dynamo.create(item=user)
        item = dynamo.read_by_id(id=PersonId)
        logger.info("Success to create and find user")
        return respond(None, {"user": item})
    except Exception as e:
        logger.error(e)
        return respond("Failed")
