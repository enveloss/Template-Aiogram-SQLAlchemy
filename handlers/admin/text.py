from modules import *
from handlers.admin import inline

async def handler(message: aiogram.types.Message, state: FSMContext):	
	if type(message) == aiogram.types.CallbackQuery: return inline.handler(message, state) 

	if message.text == '/exit':
		await state.finish()
		await message.answer('<b>Меню</b>', reply_markup=MENU)