import couchdb,json,sys
from CRUD import create_database,initial_upload,update_data,retrieve_from_db

couchserver = couchdb.Server("http://0.0.0.0:5984/")


with open(sys.argv[1], 'r')as f:
    data = f.read()
    data = json.loads(data)

    
    #Check and create a database
    if(data['Instruction'] == 'create'):
        create_database.create_db(data)

    #Check and update or enter the details
    if(data['Instruction'] == 'upload'):
        initial_upload.update_db(data)

    #update the data (modifying the database)
    if(data['Instruction'] == 'update'):
        update_data.update_db(data)

    #retrieving data from db
    if(data["Instruction"] == 'retrieve'):
        retrieve_from_db.retrieve_from_db(data)