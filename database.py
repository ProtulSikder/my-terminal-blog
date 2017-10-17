import pymongo

class Database(object):
    uri = "mongodb://127.0.0.1:27017"
    database = None

    @staticmethod
    def initialize():
        client = pymongo.MongoClient(Database.uri)
        Database.database = client['fullstack']

    @staticmethod
    def insert(content,data):
        Database.database[content].insert(data)

    @staticmethod
    def find(content, query):
        return Database.database[content].find(query)

    @staticmethod
    def findOne(content, query):
        return Database.database[content].find_one(query)