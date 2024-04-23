import os
import dotenv
from pymongo import MongoClient
from pymongo.collection import Collection

dotenv.load_dotenv(".env")

api_id = os.environ.get('API_ID', '10471716')
api_hash = os.environ.get('API_HASH', 'f8a1b21a13af154596e2ff5bed164860')
bot_token = os.environ.get('BOT_TOKEN', '6999401413:AAHgF1ZpUsCT5MgWX1Wky7GbegyeHvzi2AU')
db_url = os.environ.get('MONGO_DB_URL', 'mongodb+srv://appuz:chrijismiappuz@cluster0.yngvhc2.mongodb.net/?retryWrites=true&w=majority')
database_name = os.environ.get('DATABASE_NAME', 'Cluster0')
owner_id = int(os.environ.get('OWNER_ID', '6883997969'))
bot_username = os.environ.get('BOT_USERNAME', 'Io_TesterBot')

client = MongoClient(db_url, tls=True)
config_collection = Collection(client[database_name], 'ConfigDB')

# Check if the document exists
existing_document = config_collection.find_one({"_id": "GogoAnime"})

# If the document doesn't exist, create it with default values
if existing_document is None:
    default_data = {
        "_id": "GogoAnime",
        "gogoanime": "default_gogoanime_token",
        "auth": "default_auth_token",
        "url": "default_host_url"
    }
    config_collection.insert_one(default_data)

# Retrieve the document
data = config_collection.find_one({"_id": "GogoAnime"})

# Now you can safely access the data
gogoanime_token = data.get("gogoanime", "default_gogoanime_token")
auth_token = data.get("auth", "default_auth_token")
host_url = data.get("url", "default_host_url")
