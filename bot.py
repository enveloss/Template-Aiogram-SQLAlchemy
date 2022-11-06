from modules import *
from handlers import handlers

def setup(bot: Bot, storage) -> aiogram.Bot:
	dp = Dispatcher(bot, storage=storage())

	# setuping handlers
	dp.register_message_handler(callback=handlers.message_handler, content_types=aiogram.types.ContentType.all(), state='*')
	dp.register_callback_query_handler(callback=handlers.callback_query, state='*')

	# setuping middlewares
	add_users.setup_middleware(dp, db.users.add_user, db.users.get_user_by_id)

	# run executor
	executor.start_polling(dp, skip_updates=True)