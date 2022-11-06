from dotenv import load_dotenv 
from os import getenv
from configparser import ConfigParser

load_dotenv('./settings/.env')
SETTINGS_PATH = "./settings/.settings.ini"

# getting
BOT_TOKEN = getenv('BOT_TOKEN')
CONN_STRING = getenv('CONN_STRING')

_settings = ConfigParser()
def settings():
	_settings.read(SETTINGS_PATH)
	return _settings