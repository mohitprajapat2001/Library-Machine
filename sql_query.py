from database_connector import *
def db_query(query):
    mycursor.execute(f'{query}')
    return mycursor