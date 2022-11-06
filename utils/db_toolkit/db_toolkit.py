from typing import Any, Dict

from datetime import datetime, timedelta

from random import randint, random, choice
from time import sleep

import string
import configparser

from uuid import uuid4

class Config:
	path = "settings/config.ini"
	_config = configparser.ConfigParser()

	def get():
		Config._config.read(Config.path)
		return Config._config

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
	
	def get_admins(self) -> list:
		return [int(admin) for admin in Config.get()['MAIN']['admins'].split()]

helper = Helper()
date_helper = DateHelper()

from .SQLALchemy.db import *