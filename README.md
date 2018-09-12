# How Python Talks to Data in...
# Data Centric Development


Welcome to my Python project on Cloud9 IDE!  Yes I've taken over the default Readme
to add in a few more bits about what this [Code Institute](https://courses.codeinstitute.net/) tutorial was all about.

This tutoral focused on creating python apps which perform CRUD operations on a simple database
hosted on [mLab](https://mlab.com/)

Remember, CRUD -> ```Create, Read, Update, Delete```

The Learning Outcomes Are:

1 The Twitter API Introcreating a MongoDB database in the cloud

   * Register and account with [mLab](https://mlab.com/), 
   * Creating a test database
    
2 Twitter API Accessusing MongoDB command line tools to manipulate data

   * Connect using the mongo shell 


3 Connecting to MongoDB using Python

   * Connect using a driver via the standard MongoDB URI
    
4 Create a menu driven database system.

   * Build helper functions that will allow us to use a command line menu to:
   
        1. Add a record
        2. Find a record by name
        3. Edit a record
        4. Delete a record
        5. Exit the program


## Setting up MongoDB in Cloud9:
1 Update MongoDB in Cloud9 from the CLI:

```wget -q https://git.io/vFb1J -O /tmp/setupmongodb.sh && source /tmp/setupmongodb.sh```

2 Connect to MonngoDB on mlab:

```mongo ds249992.mlab.com:49992/mytestdb -u <dbuser> -p <dbpassword>```

3 To see colections:
```show collections```

4 Create a short variable name for a collection:

```<short_name> = db.<collection_name>;```
eg.
```coll = db.myFirstMDB;```

5 To enable Ptython to work with our MongoDB, install the libraries first

```sudo apt-get install build-essential python-dev```

6 Then install pymongo

```sudo pip3 install pymongo```

## Setting up the Python app:

Add the imports:

```python
import pymongo
import os
```

Setup the environmental variables for connecting to the database.

```python
MONGODB_URI = os.getenv("MONGO_URI")
DBS_NAME = "mytestdb"
COLLECTION_NAME = "myFirstMDB"

def mongo_connect(url):
    try:
        conn = pymongo.MongoClient(url)
        return conn
    except pymongo.errors.ConnectionFailure as e:
        print("Could not connect to MongoDB: %s") % e
```
Our App menu:

```python
def show_menu(): # CRUD Create, Read, Update, Delete
    print("")
    print("1. Add a record")
    print("2. Find a record by name")
    print("3. Edit a record")
    print("4. Delete a record")
    print("5. Exit")
    
    option = input ("Enter option: ")
    return option
```

Get the records from the database if they exist:
(this function is called by the functions below)

```python
def get_record():
    print("")
    first = input("Enter first name > ")
    last = input("Enter last name > ")
    
    try:
        doc = coll.find_one({'first': first.lower(), 'last': last.lower()})
    except:
        print("Error accessing the database")
        
    if not doc:
        print("")
        print("Error! No record found.")
    
    return doc
```

Add a set of records:

```python
def add_record():
    print("")
    first = input("Enter first name > ")
    last = input("Enter last name > ")
    dob = input("Enter date of birth > ")
    gender = input("Enter gender a 'm' or 'f' > ")
    hair_colour = input("Enter hair colour > ")
    occupation = input("Enter occupation > ")
    nationality = input("Enter nationality > ")
    
    new_doc = {'first': first.lower(), 'last': last.lower(), 'dob': dob, 
        'gender': gender, 'hair_colour': hair_colour, 'occupation': occupation, 
        'nationality': nationality}
    
    try:
        coll.insert(new_doc)
        print("")
        print("Document inserted")
    except:
        print("Error accessing the database")
```

Find a set of records:

```python
def find_record():
    doc = get_record()
    if doc:
        print("")
        for k,v in doc.items():
            if k != "_id":
                print(k.capitalize() + ": " + v.capitalize())
```

Edit a set of records:

```python
def edit_record():
    doc = get_record()
    if doc:
        update_doc={}
        print("")
        for k,v in doc.items():
            if k != "_id":
                update_doc[k] = input(k.capitalize() + " [" + v + "] > ")
                
                if update_doc[k] == "":
                    update_doc[k] = v

        try:
            coll.update_one(doc, {'$set': update_doc})
            print("")
        except:
            print("Error accessing the database")
```

Find a record and get confirmation befor deletion:

```python
def delete_record():
    doc = get_record()
    if doc:
        print("")
        for k,v in doc.items():
            if k != "_id":
                print(k.capitalize() + ": " + v.capitalize())
                
        print("")
        confirmation = input("Is this the document you want to delete?\nY or N > ")
        
        if confirmation.lower() == 'y':
            try:
                coll.remove(doc)
                print("Document deleted")
            except:
                print("Error accessing the database")
        else:
            print("Document not deleted")
```

Main app loop:

```python
def main_loop():
    while True:
        option = show_menu()
        if option == "1":
            add_record()
        elif option == "2":
            find_record()
        elif option == "3":
            edit_record()
        elif option == "4":
            delete_record()
        elif option == "5":
            conn.close()
            break
        else:
            print("Invalid option")
        print("")
```

Connect the python app to our database in the cloud:

```python
conn = mongo_connect(MONGODB_URI)

coll = conn[DBS_NAME][COLLECTION_NAME]
```

Without it, our app would never be called:

```python
main_loop()
```