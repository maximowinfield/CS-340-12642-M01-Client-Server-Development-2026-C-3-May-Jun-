from pymongo import MongoClient
from pymongo.errors import PyMongoError


class AnimalShelter(object):
    """CRUD operations for the Austin Animal Center animals collection."""

    def __init__(self, username="aacuser", password="SNHU"):
        """Initialize the MongoDB connection."""

        HOST = "localhost"
        PORT = 27017
        DB = "aac"
        COL = "animals"

        self.client = MongoClient(
            "mongodb://%s:%s@%s:%d/?authSource=%s"
            % (username, password, HOST, PORT, DB)
        )

        self.database = self.client[DB]
        self.collection = self.database[COL]

    def create(self, data):
        """Insert one document into the animals collection."""

        if data is None or not isinstance(data, dict):
            return False

        try:
            result = self.collection.insert_one(data)
            return result.acknowledged
        except PyMongoError as error:
            print("Create error:", error)
            return False

    def read(self, query):
        """Read documents from the animals collection."""

        if query is None:
            query = {}

        try:
            return list(self.collection.find(query))
        except PyMongoError as error:
            print("Read error:", error)
            return []