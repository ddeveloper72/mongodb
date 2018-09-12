import pymongo
import os

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

new_docs = [{'first': 'terry', 'last': 'pratchett', 'dob': '28/04/1948', 
'gender': 'm', 'hair_colour': 'not much', 'occupation': 'writer',
'nationality': 'english'}, {'first': 'george', 'last': 'rr martin',
'dob': '20/09/1948', 'gender': 'm', 'hair_colour': 'white', 'occupation': 'writer',
'nationality': 'american'}]

coll.insert_many(new_docs)

documents = coll.find()

for doc in documents:
    print(doc)
    

