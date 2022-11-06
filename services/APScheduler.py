from apscheduler.schedulers.asyncio import AsyncIOScheduler

scheduler = AsyncIOScheduler(timezone='Europe/Moscow')

async def some_work(): 
	print('I`m Working!')

def setup():
	scheduler.add_job(some_work, 'interval', seconds=5)
	#cheduler.add_job(some_work, 'cron', hour=0, minute=0)

	scheduler.start()