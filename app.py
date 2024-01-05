import asyncio
from loader import dp, bot
from utils.notify import notify_admins
from handlers import setup_message_routers
from utils.set_commands import set_bot_cmd





async def main() -> None:
    message_routers = setup_message_routers()
    await set_bot_cmd()
    await notify_admins()
    dp.include_router(message_routers)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())