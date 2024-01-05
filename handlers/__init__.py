from aiogram import Router 


def setup_message_routers() -> Router:
    from . import start, search, user_messages
    router = Router()
    router.include_router(start.router)
    router.include_router(search.router)
    router.include_router(user_messages.router)
    return router