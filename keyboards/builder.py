from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types.inline_keyboard_button import InlineKeyboardButton


def inline_builder(text: str | list[str], callback_data: str | list[str], size: int | list[int] | None = None) -> InlineKeyboardBuilder:
    builder = InlineKeyboardBuilder()
    
    text = [text] if isinstance(text, str) else text
    callback_data = [callback_data] if isinstance(callback_data, str) else callback_data
    size = size if isinstance(size, int) else size

    [
        builder.button(text=txt, callback_data=clb)
        for txt, clb in zip(text, callback_data)
    ]

    return builder.as_markup()


def reply_builder(text: str, sizes: int = 2) -> ReplyKeyboardBuilder:
    builder = ReplyKeyboardBuilder()
    builder.button(text = text)
    builder.adjust(sizes)
    return builder.as_markup(resize_keyboard = True)