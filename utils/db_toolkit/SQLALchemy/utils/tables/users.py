from ....db_toolkit import *
from ..databases import *

class Users(Helper):
	def __init__(self, database: Database) -> None:
		Helper.__init__(self)
		self.table = database.users
		self.db = database
	
	async def add_user(self, user_id):
		async with self.db.engine.connect() as conn:
			await conn.execute(
				insert(self.table).values(
					user_id=user_id
				)
			)

			await conn.commit()
	
	async def get_user_by_id(self, user_id=None, all=False):
		async with self.db.engine.connect() as conn:
			if not all: data = await conn.execute(
				select(self.table).where(
					self.table.c.user_id == user_id
				)
			)

			else: data = await conn.execute(
					select(self.table)
				)

			return data.fetchall() if all else data.fetchone()

	async def get_status(self, user_id):
		return (await self.get_user_by_id(user_id))['status']

	async def set_status(self, user_id, data):
		async with self.db.engine.connect() as conn:
			await conn.execute(
				update(self.table).where(
					self.table.c.user_id == user_id 
				).values(
					status=data
				)
			)

			await conn.commit()

	async def delete_user(self, user_id):
		async with self.db.engine.connect() as conn:
			await conn.execute(
				delete(self.table).where(
					self.table.c.user_id == user_id
				)
			)

			await conn.commit()
		