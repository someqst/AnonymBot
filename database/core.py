import datetime
from sqlalchemy import text, update, insert, delete, select
from sqlalchemy.ext.asyncio import create_async_engine
from database.models import metadata_obj, users



class DataBase:
    def __init__(self, db) -> None:
        self.conf = db
        self.async_engine = create_async_engine(
            url = f"postgresql+asyncpg://{self.conf[0]}:{self.conf[1]}@{self.conf[2]}/{self.conf[3]}",
            echo = False,
        )


    async def stm(self, stmt):
        async with self.async_engine.connect() as conn:
            try:
                await conn.execute(stmt)
                await conn.commit()
            except:
                pass

    async def qry_fone(self, query):
        async with self.async_engine.connect() as conn:
            result = await conn.execute(query)
            try:
                res = result.fetchone()[0]
                return res
            except:
                pass


    async def qry_fall(self, query):
        async with self.async_engine.connect() as conn:
            result = await conn.execute(query)
            res = result.fetchall()
            return [res[0] for res in res]



    async def create_table(self):
        async with self.async_engine.connect() as conn:
            await conn.run_sync(metadata_obj.create_all)
            await conn.commit()

    async def start_user(self, user_id, username, first_name, time_start):
        stmt = insert(users).values(user_id = user_id, username = username, first_name = first_name, time_start = time_start, active = 1)
        await self.stm(stmt)

    async def start_search(self, user_id):
        stmt = update(users).where(users.c.user_id == user_id).values(ready = 1)
        await self.stm(stmt)

    async def stop_search(self, user_id):
        stmt = update(users).where(users.c.user_id == user_id).values(ready = 0)
        await self.stm(stmt)

    async def search_user(self, user_id):
        query = select(users.c.user_id).where((users.c.ready == 1) & (users.c.user_id != user_id))
        return await self.qry_fone(query)
    
    async def leave_conversation(self, leaver, chat_user):
        for user in leaver, chat_user:
            stmt = update(users).where(users.c.user_id == user).values(ready = 0, chating_user = None)
            await self.stm(stmt)
        
    async def chating_user(self, user_id):
        query = select(users.c.chating_user).where(users.c.user_id == user_id)
        return await self.qry_fone(query)

    async def write_founded(self, founder, found_user):
        for user in founder, found_user:
            if user == founder:
                writable = found_user
            else:
                writable = founder
            stmt = update(users).where(users.c.user_id == user).values(chating_user = writable, ready = 2)
            await self.stm(stmt)
