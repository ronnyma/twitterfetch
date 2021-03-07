from pymongo import MongoClient


class Persistence:

    def __init__(self):
        self.client = MongoClient('localhost', 27017)
        db = self.client['pk']
        self.coll = db['tweets']

    def insert(self, doc):
        self.coll.insert_one(doc)

    def close(self):
        self.client.close()
