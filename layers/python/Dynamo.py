import boto3
import uuid
from Persistence import Persistence


class Dynamo(Persistence):
    def __init__(
        self, tablename, is_local_env=False,
    ):
        if is_local_env:
            self.person_table = boto3.resource(
                "dynamodb", endpoint_url="http://dynamo:8000/"
            ).Table(tablename)
        else:
            self.person_table = boto3.resource("dynamodb").Table(tablename)

    def create(self, item):
        PersonId = str(uuid.uuid4())
        self.person_table.put_item(Item={"Id": PersonId, **item})
        return PersonId

    def read_by_id(self, id):
        response = self.person_table.get_item(Key={"Id": id})
        item = response["Item"]
        return item

    def read_all(self):
        response = self.person_table.scan()
        items = response["Items"]
        return items
