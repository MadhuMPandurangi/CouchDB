import couchdb
import json

couchserver = couchdb.Server("http://127.0.0.1:5984/")


def create_db(data):
    database = data['Database name']
    if database in couchserver:
        print("Database with the name "+ database +" already exist")
    else:
        db = couchserver.create(database)
        print("Database "+database+" created successfully")