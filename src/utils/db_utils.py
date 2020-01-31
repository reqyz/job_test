import asyncpg

from conf import settings
from utils.exeptions import NotFoundException, AlreadyExists


async def make_database_connection_pool(**kwargs):
    return await asyncpg.create_pool(
        min_size=settings.MIN_CONNECTION_POOL_SIZE,
        max_size=settings.MAX_CONNECTION_POOL_SIZE,
        dsn=settings.DATABASE_URL,
        **kwargs
    )


async def setup_database(app, **kwargs):
    app.pool = await make_database_connection_pool(**kwargs)


class DBRepository:

    def __init__(self, pool: asyncpg.pool.Pool):
        self._pool = pool

    async def __base_simple_execute(self, sql: str, method: str, *args):
        async with self._pool.acquire() as con:
            return await getattr(con, method)(sql, *args)

    async def _simple_execute(self, sql: str, *args):
        try:
            return await self.__base_simple_execute(sql, 'execute', *args)
        except asyncpg.UniqueViolationError:
            raise AlreadyExists

    async def _select_one(self, sql: str, *args):
        rv = await self.__base_simple_execute(sql, 'fetchrow', *args)
        if not rv:
            raise NotFoundException
        return rv

    async def _select_all(self, sql: str, *args):
        rv = await self.__base_simple_execute(sql, 'fetch', *args)
        return rv
