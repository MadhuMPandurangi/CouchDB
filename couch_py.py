import couchdb
import json
couchserver = couchdb.Server("http://127.0.0.1:5984/")

#fucntion to create db and store date in db
def create_db():

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

    rows =  db.view('_all_docs',include_docs=True)
    data = [row['doc'] for row in rows]

    #converting to json
    jsondata = json.dumps(data)

    #splitting and converting to list 
    split1 = jsondata.split('{')

    #converting to string
    str1 = str(split1[2])

    #splitting and converting to list
    split2 = str1.split('}')
    print(split2[0])


#deleting data from couchdb
def delete_data_from_db():
    db = couchserver['db_test']
    couchserver.delete('db_test')
    print("Data base deleted")


create_db()
retrieve_from_db()
upload_db()
delete_data_from_db()    