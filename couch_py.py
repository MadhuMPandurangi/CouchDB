import couchdb
import json
couchserver = couchdb.Server("http://127.0.0.1:5984/")

#fucntion to create db and store date in db
def create_db():
    
    if 'db_test' in couchserver:
        db = couchserver['db_test']
    else:
        db = couchserver.create('db_test')
            
    
    doc = {
    'id':111,
    'content':{
        'name':'madhu',
        'mailid':'madhumpandurangi@gmail.com'
        }
    }

    db.save(doc)


#uploading data for the current db
def upload_db():

    db = couchserver['db_test']

    doc = {
    'id':112,
    'content':{
        'name':'madhurimp',
        'mailid':'madhurimpandurangi@gmail.com'
        }
    }

    db.save(doc)


#retrieving data from couchdb
def retrieve_from_db():

    db = couchserver['db_test']

    i = 1
    content = dict()
    for item in db.view('_design/content/_view/content'):
        content.update({i:item.key}) 
        i+=1 

    print(content[2]['name'])


#deleting data from couchdb
def delete_data_from_db():
    db = couchserver['db_test']
    couchserver.delete('db_test')
    print("Data base deleted")


create_db()
retrieve_from_db()
upload_db()
delete_data_from_db()    