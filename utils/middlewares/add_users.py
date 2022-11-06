from aiogram.dispatcher.middlewares import BaseMiddleware
from aiogram.dispatcher.handler import CancelHandler
from aiogram import types

class Config:
    add_user = None
    get_user = None

class BotMiddlewere(BaseMiddleware):
    async def on_pre_process_update(self, update: types.Update, data: dict):
        if update.message:
            user_id = update.message.from_user.id 
        elif update.callback_query:
            user_id = update.callback_query.from_user.id 
        else:
            return

        try: 
            if await Config.get_user(user_id) == None:
                await Config.add_user(user_id)
        
        except CancelHandler:
            raise CancelHandler()

        except Exception as e: 
            await update.message.answer("<b>Произошла ошибка!</b>\nСвяжитесь с администрацией для ее решения")
            raise CancelHandler()

def setup_middleware(dp, add_user_func, get_user):
    Config.add_user = add_user_func
    Config.get_user = get_user
    dp.middleware.setup(BotMiddlewere())