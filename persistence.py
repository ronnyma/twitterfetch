from pymongo import MongoClient

def init():
    client = MongoClient('mongodb', 27017)
    db = client['pk']
    coll = db['tweets']

    return coll


def insert(coll, doc):
    coll.insert_one(doc)



