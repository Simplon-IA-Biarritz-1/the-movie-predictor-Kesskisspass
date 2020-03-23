from pymongo import MongoClient


class DB:
    def __init__(self, db_name):
        self.client = MongoClient('localhost', 27017)
        self.db_name = db_name


