import os
import dotenv
from telethon import TelegramClient
from pymongo import MongoClient
from API.gogoanimeapi import Gogo
from pymongo.collection import Collection

dotenv.load_dotenv(".env")

__all__ = ['bot', 'gogo', 'api_id', 'api_hash', 'bot_token', 'db_url', 'database_name', 'owner_id', 'bot_username']

api_id = os.environ.get('API_ID', '23023343')
api_hash = os.environ.get('API_HASH', '2b79fd2d2c83173807a039325e7e166f')
bot_token = os.environ.get('BOT_TOKEN', '7778353740:AAE6el1IOh_YyOTfXoK9ZKkwgN7V6NKGEXM')
db_url = os.environ.get('MONGO_DB_URL', 'mongodb+srv://AnimeFlix:Itzmecp@cluster0.qxdxy.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')
database_name = os.environ.get('DATABASE_NAME', 'Cluster0')
owner_id = int(os.environ.get('OWNER_ID', '7717701360'))
bot_username = os.environ.get('BOT_USERNAME', 'AnimeFlixUploaderobot')

bot = TelegramClient('bot', api_id, api_hash).start(bot_token=bot_token)
client = MongoClient(db_url, tls=True)
data = Collection(client[database_name], 'ConfigDB').find_one({"_id":"GogoAnime"})

gogo = Gogo(
        gogoanime_token=data["gogoanime"],
        auth_token=data["auth"],
        host=data["url"]
    )
