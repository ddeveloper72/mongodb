import os
import pymongo
from dotenv import load_dotenv

load_dotenv()

MONGODB_URI = os.getenv("MONGO_URI")

DBS_NAME = "mytestdb"
COLLECTION_NAME = "myFirstMDB"


def mongo_connect(url):
    try:
        conn = pymongo.MongoClient(url)
        print("Mongo is connected!")
        return conn
    except pymongo.errors.ConnectionFailure as e:
        print("Could not connect to MongoDB: %s") % e

conn = mongo_connect(MONGODB_URI)

coll = conn[DBS_NAME][COLLECTION_NAME]

# New document to be added
new_doc = {
    'first': 'saoirse',
    'last': 'ronan',
    'dob': '12/04/1994',
    'hair_colour': 'blond',
    'gender': 'f',
    'occupation': 'actress',
    'nationality': 'irish'
}

coll.insert_one(new_doc)

documents = coll.find()

for doc in documents:
    print(doc)
