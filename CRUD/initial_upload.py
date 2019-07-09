import couchdb
import json
import pprint

couchserver = couchdb.Server("http://0.0.0.0:5984/")


def update_db(data):
    database = data['Database name']
    if database in couchserver:
        for i in data['Content']:
            doc = data['Content'][i]
            db = couchserver[database]
            db.save(doc)

        print("Uploaded data to "+database+ " database successfully")
    else:
        print("Database "+database+" doesnot exist")        