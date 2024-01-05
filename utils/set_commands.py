from loader import bot 
from aiogram.types import BotCommand


async def set_bot_cmd():
    await bot.set_my_commands([
        BotCommand(command = 'search', description = 'Начать поиск'),
        BotCommand(command = 'stop', description = 'Отменить поиск'),
        BotCommand(command = 'leave', description = 'Выйти из диалога')
    ])