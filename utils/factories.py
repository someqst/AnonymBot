from aiogram.filters.callback_data import CallbackData


class Accepter(CallbackData, prefix = 'accept'):
    action: str = 'accept_note'
    value: str | None = None