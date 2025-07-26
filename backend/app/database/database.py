import os
from pymongo import MongoClient, errors
from dotenv import load_dotenv

load_dotenv()

# Get MongoDB configuration from environment variables
MONGODB_URL = os.getenv("MONGODB_URL", "mongodb://localhost:27017")
DATABASE_NAME = os.getenv("DATABASE_NAME", "fimoney_inventory")

db = None
try:
    client = MongoClient(MONGODB_URI, serverSelectionTimeoutMS=5000)
    # Force connection on a request as the
    # connect=True parameter of MongoClient seems
    # to be useless here
    client.server_info()  # Will throw if cannot connect
    db = client[DATABASE_NAME]
    print(f"MongoDB connected successfully to database: {DATABASE_NAME}")
except errors.ServerSelectionTimeoutError as err:
    print(f"MongoDB connection error: {err}")
    print("Please ensure MongoDB is running and the connection string is correct.")
except Exception as err:
    print(f"Database error: {err}") 