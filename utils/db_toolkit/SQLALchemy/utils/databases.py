import asyncio

from os import getenv

import sqlalchemy 
from sqlalchemy import Date, func, insert, text, update, delete, select
from sqlalchemy.ext.asyncio import create_async_engine, AsyncEngine

from . import models

import configparser

class Config:
	path = "settings/settings.ini"
	_config = configparser.ConfigParser()

	def get():
		Config._config.read(Config.path)
		return Config._config

class Database:
	def __init__(self, conn_string: str=getenv('CONN_STRING')) -> None:
		'''
conn_string: dialect+driver://username:password@host:port/database
		'''

		self.engine: AsyncEngine = create_async_engine(conn_string)
		self.metadata: sqlalchemy.MetaData = sqlalchemy.MetaData()

		self.users = models.Users(self.metadata).get_table()

		asyncio.get_event_loop().run_until_complete(self.create_all()) # create tables

	async def create_all(self):
		async with self.engine.begin() as conn:
			await conn.run_sync(self.metadata.create_all)