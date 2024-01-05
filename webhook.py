# app = FastAPI()
# WEBHOOK_PATH = f'/bot/{config.BOT_TOKEN.get_secret_value()}'
# WEBHOOK_URL = f'{config.NGROK.get_secret_value()}{WEBHOOK_PATH}'

# print(WEBHOOK_URL)

# @app.on_event('startup')
# async def on_startup():
#     message_routers = setup_message_routers()
#     dp.include_router(message_routers)
#     await bot.delete_webhook()
#     webhook_info = await bot.get_webhook_info()
#     if webhook_info.url != WEBHOOK_URL:
#         await bot.set_webhook(WEBHOOK_URL)
#     await set_bot_cmd()
#     await notify_admins()
#     print('bot started')


# @app.post(WEBHOOK_PATH)
# async def bot_webhook(update: dict):
#     print('сука')
#     telegram_update = Update(**update)
#     await dp.feed_update(bot = bot, update = telegram_update)


# @app.on_event('shutdown')
# async def on_shutdown():
#     await bot.session.close()
#     print('bot down')

# if __name__ == '__main__':
#     uvicorn.run(app)