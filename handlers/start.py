from aiogram import F, Router
import datetime
from aiogram.types import Message
from aiogram.filters import CommandStart
from loader import db
import pytz
from keyboards.builder import reply_builder


router = Router()

@router.message(CommandStart())
async def start_cmd(message: Message):
    await message.answer('Приветик, сладкий. Жми /search, чтобы найти собеседника!')
    time_start = datetime.datetime.now(pytz.timezone('Europe/Moscow')).strftime('%d-%m-%Y, %H:%M:%S')
    await db.start_user(message.from_user.id, message.from_user.username, message.from_user.first_name, time_start)