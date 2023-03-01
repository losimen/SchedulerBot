from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

import config
import logging


logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %H:%M:%S')
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

storage = MemoryStorage()

bot = Bot(token=config.TOKEN, parse_mode='HTML')
dp = Dispatcher(bot, storage=storage)
