import couchdb,couchdb.design
import json

couchserver = couchdb.Server("http://0.0.0.0:5984/")


def create_db(data):
    database = data['Database name']
    if database in couchserver:
        print("Database with the name "+ database +" already exist")
    else:
        db = couchserver.create(database)
        print("Database "+database+" created successfully")
        
        #writing views
        count_map = '''function(doc) 
                        { 
                            emit(doc.id, 1); 
                        }
                        '''
        count_reduce = '''function(keys, values) 
                          { 
                              return sum(values); 
                           }'''
        view = couchdb.design.ViewDefinition('doctor', 'count', count_map, reduce_fun=count_reduce)
        view.sync(db)
        get_values = ''' function(doc) 
                        { 
                            emit(("0000000000000000000"+doc.id).slice(-19), doc); 
                        }
                        '''
        view = couchdb.design.ViewDefinition('doctor', 'get_values', get_values)
        view.sync(db)    
    
    