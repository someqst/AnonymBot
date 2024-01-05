from loader import bot 
from data.config_reader import admins_id

async def notify_admins():
    for admin in admins_id:
        await bot.send_message(admin, '*Произошел* *старт*')