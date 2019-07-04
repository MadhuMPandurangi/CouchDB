import couchdb
import json

couchserver = couchdb.Server("http://127.0.0.1:5984/")


def retrieve_from_db(data):
    database = data['Database name']
    db = couchserver[database]
    if database in couchserver:
        i = 1
        content = dict()
        for item in db.view('_design/get_full_data/_view/get_full_data'):
          content.update({i:item.key}) 
          i+=1

        #getting id of the document 
        doc=db.get(content[1]['_id'])
        print(doc['Content'])