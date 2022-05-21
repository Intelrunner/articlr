import os
from dotenv import load_dotenv
from connect import Connect

load_dotenv()

# Get Mongo config from .env file
mongo_pw = os.getenv("MONGO_PW")
mongo_db = os.getenv("MONGO_DB")
mongo_server = os.getenv("MONGO_SERVER")
mongo_user = os.getenv("MONGO_USER")

def main():    


# set up database and collection 
    server = Connect.client()
    db = server.get_database(mongo_db)
    col =  (db.get_collection('metrics'))
    
    print(col.insert_one({'hum': '0.5'}).inserted_id)

if __name__ == "__main__":
    main()