import couchdb
import json

couchserver = couchdb.Server("http://0.0.0.0:5984/")


def update_db(data):
    database = data['Database name']
    db = couchserver[database]
    if database in couchserver:
      id_list = list()

      #getting id of the  documents 
      for item in db.view('_all_docs'):
        id_list.append(item.id)

      
      for item in data['Update']:
        if((data['Update'][item]['_id']) in id_list):                       #checking availability of doctor_id
          keys_to_be_updated_list = list(data['Update'][item].keys())       #keys of the data to be updated
          keys_to_be_updated_list.remove("_id")
          doc = db.get(data['Update'][item]['_id'])
          for key in keys_to_be_updated_list:
             doc[key] = data['Update'][item][key]
             db.save(doc)
          print("Database is successfully updated")      
        else:
          print("Doctor-ID: \""+data['Update'][item]['_id']+"\" does not not exist")     


    else:
        print("Database "+database+" doesnot exist")

   