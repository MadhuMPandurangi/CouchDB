import couchdb,json,sys
from CRUD import create_database,update_database
couchserver = couchdb.Server("http://127.0.0.1:5984/")


with open(sys.argv[1], 'r')as f:
    data = f.read()
    data = json.loads(data)
    
    #Check and create a database
    if(data['Instruction'] == 'create'):
        create_database.create_db(data)

    #Check and update or enter the details
    if(data['Instruction'] == 'upload'):
        update_database.update_db(data)
