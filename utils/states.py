from modules import *

# USER STATES
class SomeState(StatesGroup):
	state_type = 'user'
	handler_type = 'state'
	
	value = State()

# ADMINS STATES
class Admin(StatesGroup):
	state_type = 'admin'
	handler_type = 'text'

	_ = State()