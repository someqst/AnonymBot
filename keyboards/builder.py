from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types.inline_keyboard_button import InlineKeyboardButton


def inline_builder(text: str, cb: str) -> InlineKeyboardBuilder:
    builder = InlineKeyboardBuilder([[]])
    builder.row(InlineKeyboardButton(text = text, callback_data=cb))
    return builder.as_markup()


def reply_builder(text: str, sizes: int = 2) -> ReplyKeyboardBuilder:
    builder = ReplyKeyboardBuilder()
    builder.button(text = text)
    builder.adjust(sizes)
    return builder.as_markup(resize_keyboard = True)