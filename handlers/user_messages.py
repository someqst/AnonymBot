from loader import db, bot
from aiogram import F, Router
from aiogram.types import Message, CallbackQuery
from keyboards.builder import reply_builder, inline_builder
from utils.factories import Accepter


router = Router()


@router.edited_message()
async def edit_messages(message: Message):
    reciever = await db.chating_user(message.from_user.id)
    if message.text:
        await bot.edit_message_text(text = message.text, chat_id = reciever, message_id = message.message_id + 1, entities = message.entities)
    elif message.caption:
        await bot.edit_message_caption(caption = message.caption, chat_id = reciever, message_id = message.message_id + 1, caption_entities = message.caption_entities, parse_mode = None)


@router.message(F.content_type.in_(
    ["text", "audio", "voice", "sticker", "document", "photo", "video", "animation", "video_note"]
))
async def echo(message: Message):
    reciever = await db.chating_user(message.from_user.id)
    if reciever is not None and reciever is not False:
        reply = None
        if message.reply_to_message:
            if message.reply_to_message.from_user.id == message.from_user.id:
                reply = message.reply_to_message.message_id + 1
            else:
                reply = message.reply_to_message.message_id - 1

        if message.content_type == 'text':
            await bot.send_message(chat_id=reciever, text=message.text, reply_to_message_id=reply)

        if message.content_type == 'photo':
            await bot.send_photo(reciever, message.photo[-1].file_id, caption=message.caption, caption_entities=message.caption_entities, reply_to_message_id = reply, has_spoiler = True, parse_mode=None)
        
        if message.content_type == 'voice':
            await bot.send_voice(reciever, message.voice.file_id, caption=message.caption, caption_entities=message.caption_entities, reply_to_message_id = reply, parse_mode=None)
        
        if message.content_type == 'audio':
            await bot.send_audio(reciever, message.audio.file_id, caption=message.caption, caption_entities=message.caption_entities, reply_to_message_id = reply, parse_mode=None)

        if message.content_type == 'video':
            await bot.send_video(reciever, message.video.file_id, caption=message.caption, caption_entities=message.caption_entities, reply_to_message_id = reply, has_spoiler=True, parse_mode=None)

        if message.content_type == 'document':
            await bot.send_document(reciever, message.document.file_id, caption=message.caption, caption_entities=message.caption_entities, reply_to_message_id = reply, parse_mode=None)

        if message.content_type == 'sticker':
            await bot.send_sticker(reciever, message.sticker.file_id, reply_to_message_id=reply)

        if message.content_type == 'animation':
            await bot.send_animation(reciever, message.animation.file_id, caption=message.caption, caption_entities=message.caption_entities, reply_to_message_id = reply, parse_mode=None)

        if message.content_type == 'video_note':
            if await db.video_notes_val(reciever) == 1:
                await bot.send_video_note(reciever, message.video_note.file_id, reply_to_message_id = reply)
            else:
                option = '🔴'
                await bot.send_message(reciever, 'Вам хотели отправить кружок. Включите возможность их принимать (можно отключить)',
                                        reply_markup=inline_builder(f'Принимать {option}', Accepter().pack()))
                await bot.send_message(message.chat.id, 'У пользователя отключена возможность принимать кружочки')
    else:
        await message.reply('У вас нет собеседника, нажмите кнопку ниже для поиска', reply_markup=reply_builder('Начать поиск'))


@router.callback_query(Accepter.filter(F.action == 'accept_note'))
async def accept_notes(call: CallbackQuery, callback_data: Accepter):
    await call.answer()
    if await db.video_notes_val(call.message.chat.id) == 0:
        await db.accept_video_note(call.from_user.id, 1)
        option = '🟢'
    else:
        await db.accept_video_note(call.from_user.id, 0)
        option = '🔴'
    
    await call.message.edit_reply_markup(reply_markup=inline_builder(f'Принимать {option}', Accepter().pack()))

