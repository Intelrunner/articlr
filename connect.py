from pymongo import MongoClient
from dotenv import load_dotenv
import os
from pymongo.server_api import ServerApi

load_dotenv()

mongo_user = os.getenv("MONGO_USER")
mongo_server = os.getenv("MONGO_SERVER")
mongo_db = os.getenv("MONGO_DB")
mongo_col = os.getenv("MONGO_COL")
mongo_pw = os.getenv("MONGO_PW")
# establish a connection to the database

load_dotenv()

class Connect():
    @staticmethod    
    def client():
        return MongoClient("mongodb+srv://{}:{}@{}/{}?retryWrites=true&w=majority".format(mongo_user,mongo_pw,mongo_server,mongo_db),server_api=ServerApi('1'))