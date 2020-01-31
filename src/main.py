import asyncio

import uvloop
from aiohttp import web
from aiohttp.web_app import Application

from conf import settings
from conf.setup_routes import setup_routes
from utils.db_utils import setup_database


async def build_application() -> Application:
    app = Application()
    await setup_database(app)
    setup_routes(app)
    app.app_settings = settings

    return app


if __name__ == '__main__':
    asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
    loop = asyncio.get_event_loop()
    web_app = loop.run_until_complete(build_application())
    web.run_app(web_app, host=settings.HOST, port=settings.PORT)
    loop.close()
