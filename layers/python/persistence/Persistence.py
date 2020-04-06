from abc import ABC


class Persistence(ABC):
    def create(self, item):
        ...

    def read(self, id):
        ...

    def read_all():
        ...
