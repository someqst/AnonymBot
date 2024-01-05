from aiogram import Dispatcher, Bot
from aiogram.enums import ParseMode 
from data.config_reader import config
from database.core import DataBase
# from tgadmin.ugc.models import Profile

bot = Bot(config.BOT_TOKEN.get_secret_value(), parse_mode=ParseMode.MARKDOWN)
dp = Dispatcher()
db = DataBase((config.DBUSER.get_secret_value(), config.DBPASS.get_secret_value(), config.DBHOST.get_secret_value(), config.DBNAME.get_secret_value()))

# def add_django(user_id, username):
#     Profile.objects.get_or_create(
#         external_id = user_id,
#         defaults = {
#             'name': username
#         }
#     )