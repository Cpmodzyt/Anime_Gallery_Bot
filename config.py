import os
import dotenv
from telethon import TelegramClient
from pymongo import MongoClient
from API.gogoanimeapi import Gogo
from pymongo.collection import Collection

dotenv.load_dotenv(".env")

api_id = os.environ.get('API_ID', '10471716')
api_hash = os.environ.get('API_HASH', 'f8a1b21a13af154596e2ff5bed164860')
bot_token = os.environ.get('BOT_TOKEN', '6999401413:AAHgF1ZpUsCT5MgWX1Wky7GbegyeHvzi2AU')
db_url = os.environ.get('MONGO_DB_URL', 'mongodb+srv://appuz:chrijismiappuz@cluster0.yngvhc2.mongodb.net/?retryWrites=true&w=majority')
database_name = os.environ.get('DATABASE_NAME', 'Cluster0')
owner_id = int(os.environ.get('OWNER_ID', '6883997969'))
bot_username = os.environ.get('BOT_USERNAME', 'Io_TesterBot')

def initialize():
    bot = TelegramClient('bot', api_id, api_hash).start(bot_token=bot_token)
    client = MongoClient(db_url, tls=True)
    data = Collection(client[database_name], 'ConfigDB').find_one({"_id":"GogoAnime"})
    gogo = Gogo(
        gogoanime_token=data["gogoanime"],
        auth_token=data["auth"],
        host=data["url"]
    )
    return bot, gogo
