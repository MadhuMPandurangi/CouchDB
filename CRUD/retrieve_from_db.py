import couchdb
import json

couchserver = couchdb.Server("http://127.0.0.1:5984/")


def cretrieve_from_db(data):