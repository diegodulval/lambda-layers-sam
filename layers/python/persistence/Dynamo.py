import boto3
import uuid
from persistence.Persistence import Persistence


class Dynamo(Persistence):
    def __init__(
        self, tablename, endpoint_url=None,
    ):
        if endpoint_url is not None:
            self.person_table = boto3.resource(
                "dynamodb", endpoint_url=endpoint_url
            ).Table(tablename)
        else:
            self.person_table = boto3.resource("dynamodb").Table(tablename)

    def create(self, item):
        PersonId = str(uuid.uuid4())
        user = {"Id": PersonId, **item}
        self.person_table.put_item(Item=user)
        return user

    def read_by_id(self, id):
        response = self.person_table.get_item(Key={"Id": id})
        item = response["Item"]
        return item

    def read_all(self):
        response = self.person_table.scan()
        items = response["Items"]
        return items
