# from os import getenv

from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.redis import RedisStorage2

bot = Bot(token='6803792823:AAHcezYfCtEFtB05-t_nJGvZKTn3w1V8LDk', parse_mode=types.ParseMode.HTML)
storage = RedisStorage2(port=6379)
dp = Dispatcher(bot, storage=storage)
