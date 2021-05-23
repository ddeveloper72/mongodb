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

# Updates a single document within the collection based on the filter
coll.update_one(
    {
        'nationality': 'american'
    },
    {
        '$set': {
            'hair_colour': 'maroon'
        }
    }
)

documents = coll.find({'nationality': 'american'})

for doc in documents:
    print(doc)
