import bot
from services import APScheduler

from modules import bot as bot_, MemoryStorage

if __name__ == "__main__":
    APScheduler.setup()
    bot.setup(bot_, storage=MemoryStorage)