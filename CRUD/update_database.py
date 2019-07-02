import couchdb
import json

couchserver = couchdb.Server("http://127.0.0.1:5984/")


def update_db(data):
    database = data['Database name']
    if database in couchserver:
       doc = data['Content']
       db = couchserver[database]
       db.save(doc)
    else:
        print("Database "+database+" doesnot exist")    