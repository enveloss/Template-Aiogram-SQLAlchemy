from typing import Any, Dict

from datetime import datetime, timedelta

from random import randint, random, choice
from time import sleep

import string, json

from uuid import uuid4

class DateHelper:
	def __init__(self) -> None:
		self.TIME_FORMAT = '%Y-%m-%d %H:%M:%S'

	def get_date_now(self, t='%Y-%m-%d %H:%M:%S'):
		return datetime.now().strftime(t)

	def get_date_from_timestamp(self, timestamp, t='%Y-%m-%d %H:%M:%S'):
		return datetime.fromtimestamp(timestamp).strftime(t)

	def get_timestamp(self, date, t='%Y-%m-%d %H:%M:%S'):
		return datetime.strptime(date, t).timestamp()

	def get_next_date(self, days=None, hours=None, minutes=None, seconds=None, t='%Y-%m-%d %H:%M:%S'):
		now = datetime.now()

		if days != None: next_date = now + timedelta(days=days)
		if hours != None: next_date = now + timedelta(hours=hours)
		if minutes != None: next_date = now + timedelta(minutes=minutes)
		if seconds != None: next_date = now + timedelta(seconds=seconds)

		return next_date.strftime(t)

	def get_strptime(self, date, t='%Y-%m-%d %H:%M:%S'):
		return datetime.strptime(date, t)

class Helper:
	def __init__(self) -> None:
		pass

	def create_string(self, size=8):
		chars=string.ascii_uppercase + string.ascii_lowercase + string.digits
		return ''.join(choice(chars) for _ in range(0, size))		

class JSONConfig:
	def __init__(self, path='./settings/config.json') -> None:
		self.path = path
	
	def get_data(self) -> dict:
		with open(self.path, encoding='utf-8') as file:
			return json.load(file)

	def _save_data(self, data: dict) -> None:
		with open(self.path, 'w', encoding='utf-8') as file:
			return json.dump(data, file, indent=4, ensure_ascii=False)

	def _get_pretty_path(self, path: str) -> str:
		path = ".".join([f"'{key}'" for key in path.split('.')])
		path =  f"[{path.replace('.', '][')}]"

		return path
	
	def set_value(self, path: str, value) -> None:
		data = self.get_data()
		exec(f"data{self._get_pretty_path(path)} = {value}")
		self._save_data(data)
	
	def get_value(self, path: str) -> None:
		return eval(f"{self.get_data()}{self._get_pretty_path(path)}")
	
	def getAdmins(self):
		return self.get_value('admins')

helper = Helper()
date_helper = DateHelper()
json_config = JSONConfig()

from .SQLALchemy.db import *