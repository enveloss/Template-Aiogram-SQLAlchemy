import aiogram, logging

from aiogram import Bot, Dispatcher, executor
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove

from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types.message import ContentType

#from aiogram.contrib.fsm_storage.mongo import MongoStorage
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from settings import config
from utils. middlewares import add_users

from utils import keyboards, states
from utils.db_toolkit import db_toolkit as db

# logger setuping
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(name)s - %(message)s")
logger.info('bot is started')

# init settings
settings = config.settings

# bot setuping
bot = Bot(token=config.BOT_TOKEN)

# keyboards setuping
MENU = ReplyKeyboardMarkup(keyboards.menu(KeyboardButton), True, False) 
ADMIN = ReplyKeyboardMarkup(keyboards.admin(KeyboardButton), True, False) 
BACK = ReplyKeyboardMarkup(keyboards.back(KeyboardButton), True, False)
