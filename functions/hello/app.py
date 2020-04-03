from Dynamo import Dynamo
from helpers import start_debbuger, start_logger


logger = start_logger()
start_debbuger()


def respond(err, res=None):
    return {
        'statusCode': '400' if err else '200',
        'body': err if err else res,
        'headers': {'Content-Type': 'application/json'},
    }


def lambda_handler(event, context):
    user = {'FirstName': 'John', 'LastName': 'Due', 'Age': 24}
    try:
        dynamo = Dynamo(env=True, tablename='PersonTable')
        PersonId = dynamo.create(item=user)
        item = dynamo.read_by_id(id=PersonId)
        logger.info('Success to create and find user')
        return respond(None, {'user': item})
    except Exception as e:
        logger.error(e)
        return respond('Failed')
