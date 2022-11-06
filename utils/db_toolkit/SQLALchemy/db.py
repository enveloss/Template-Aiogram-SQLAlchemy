from .utils.tables.users import Users

from .utils.databases import *

database = Database()
users = Users(database=database)