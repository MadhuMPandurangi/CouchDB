import couchdb
import json

couchserver = couchdb.Server("http://0.0.0.0:5984/")


def delete_data(data):