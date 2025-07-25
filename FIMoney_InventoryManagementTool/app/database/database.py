import os
from pymongo import MongoClient, errors
from dotenv import load_dotenv

load_dotenv()
MONGODB_URI = os.getenv("MONGODB_URI")

db = None
try:
    client = MongoClient(MONGODB_URI, serverSelectionTimeoutMS=5000)
    # Force connection on a request as the
    # connect=True parameter of MongoClient seems
    # to be useless here
    client.server_info()  # Will throw if cannot connect
    db = client.get_default_database()
    print("MongoDB connected successfully.")
except errors.ServerSelectionTimeoutError as err:
    print(f"MongoDB connection error: {err}") 