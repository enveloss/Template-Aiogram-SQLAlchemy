from aiogram.dispatcher.handler import CancelHandler
from aiogram.dispatcher.middlewares import BaseMiddleware
from aiogram import types

class Config:
    testers = []

class BotMiddlewere(BaseMiddleware):
    async def on_process_update(self, update: types.Update, data: dict):
        if update.message:
            user_id = update.message.from_user.id 
        elif update.callback_query:
            user_id = update.callback_query.from_user.id 
        else:
            return

        if not user_id in Config.testers:
            if update.message: await update.message.answer('⚒ <b>Бот на тех. обслуживании!</b>')
            raise CancelHandler()

def setup_middleware(dp, testers):
    Config.testers = testers
    dp.middleware.setup(BotMiddlewere())