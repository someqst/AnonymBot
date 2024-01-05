from database.core import DataBase
from aiogram.enums import ParseMode 
from aiogram import Dispatcher, Bot
from data.config_reader import config
from aiogram.fsm.storage.memory import MemoryStorage
# from tgadmin.ugc.models import Profile

bot = Bot(config.BOT_TOKEN.get_secret_value(), parse_mode=ParseMode.MARKDOWN)
dp = Dispatcher(storage=MemoryStorage())
db = DataBase((config.DBUSER.get_secret_value(), config.DBPASS.get_secret_value(), config.DBHOST.get_secret_value(), config.DBNAME.get_secret_value()))

# def add_django(user_id, username):
#     Profile.objects.get_or_create(
#         external_id = user_id,
#         defaults = {
#             'name': username
#         }
#     )