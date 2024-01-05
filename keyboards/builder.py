from aiogram.utils.keyboard import ReplyKeyboardBuilder

def reply_builder(text: str, sizes: int = 2) -> ReplyKeyboardBuilder:
    builder = ReplyKeyboardBuilder()
    builder.button(text = text)
    builder.adjust(sizes)
    return builder.as_markup(resize_keyboard = True)