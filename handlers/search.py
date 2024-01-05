from aiogram.types import Message
from aiogram import F, Router 
from loader import db, bot
from keyboards.builder import reply_builder
from aiogram.filters import Command, or_f


router = Router()


@router.message(or_f(F.text.lower() == 'начать поиск', Command("search")))
async def search_user(message: Message):
    founder = message.from_user.id
    await db.start_search(founder)
    found_user = await db.search_user(founder)
    if not found_user:
        await message.reply('Вы в поиске собеседника', reply_markup=reply_builder('Отменить'))
    else:
        await db.write_founded(founder, found_user)
        for user in founder, found_user:
            await bot.send_message(user, 'Собеседник найден. Общайтесь', reply_markup=reply_builder('Выйти'))


@router.message(or_f(F.text.lower() == 'выйти', Command("leave")))
async def search_user(message: Message):
    chat_user = await db.chating_user(message.from_user.id)
    leaver = message.from_user.id
    await db.leave_conversation(leaver, chat_user)
    for user in leaver, chat_user:
        if user == leaver:
            await bot.send_message(user, 'Вы вышли из диалога', reply_markup=reply_builder('Начать поиск'))
        else:
            await bot.send_message(user, 'Собеседник завершил диалог', reply_markup=reply_builder('Начать поиск'))


@router.message(or_f(F.text.lower() == 'отменить', Command("stop")))
async def search_user(message: Message):
    await db.stop_search(message.from_user.id)
    await message.reply('Поиск остановлен', reply_markup=reply_builder('Начать поиск'))
        