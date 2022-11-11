from modules import * 

from .user import inline as user_inline, text as user_text, state as user_state
from .admin import inline as admin_inline, text as admin_text, state as admin_state

def get_state_vars(state_string: str):
	if state_string != None:
		return {
			"state_type": eval(f"states.{state_string.split(':')[0]}.state_type"),
			"handler_type": eval(f"states.{state_string.split(':')[0]}.handler_type")
		} 

	else:
		return {
			"state_type": 'user',
			"handler_type": 'text'
		} 

async def run_handler(handler_type, state_type, update, state):
	function = eval(f"{state_type}_{handler_type}.handler")
	await function(update, state)

async def message_handler(message: aiogram.types.Message, state: FSMContext):
	state_string = await state.get_state()
	state_vars = get_state_vars(state_string)
	
	await run_handler(**state_vars, update=message, state=state)

async def callback_query(call: aiogram.types.CallbackQuery, state: FSMContext):
	state_string = await state.get_state()
	state_vars = get_state_vars(state_string)

	if state_string == None: state_vars =  {
		"state_type": 'user',
		"handler_type": 'inline'
	} 
	
	await run_handler(**state_vars, update=call, state=state)