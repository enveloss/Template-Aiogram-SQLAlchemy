from modules import *

async def handler(state: FSMContext, message: aiogram.types.Message):
	state_data = await state.get_state()
	
	if message.text == '/restart':
		await state.finish()
		await message.answer('<b>Меню</b>', reply_markup=MENU)
	
	elif 'Form:' in state_data:
		action = state_data.split(':')[1]

		if action == '_':
			pass