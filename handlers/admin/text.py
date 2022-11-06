from modules import *

async def handler(message: aiogram.types.Message, state: FSMContext):	
	if message.text == '/exit':
		await state.finish()
		await message.answer('<b>Меню</b>', reply_markup=MENU)