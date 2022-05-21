from connect import Connect
import os
from dotenv import load_dotenv



# WRANGLE SOME ENV VARS
load_dotenv()
col = os.getenv("MONGO_COL")

# DB is set in connection class
connection = Connect.get_connection()

# Setting collection
collection = connection[col]

connection.count_documents({})

