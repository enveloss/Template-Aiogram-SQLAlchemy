from dotenv import load_dotenv 
from os import getenv

load_dotenv('./settings/.env')

# getting
BOT_TOKEN = getenv('BOT_TOKEN')
CONN_STRING = getenv('CONN_STRING')