from pymongo import MongoClient


class DB:
    def __init__(self, dbname,collection):
        self.client = MongoClient('localhost', 27017)
        self.dbase = self.client[dbname]
        self.collection = self.dbase[collection]

    def add(self,data):
        self.collection.insert_many(data)

