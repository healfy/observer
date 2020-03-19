import aioredis

from aiohttp import web
from aiohttp.web_runner import AppRunner

from settings.config import conf


async def shutdown(server, app, handler, redis):
    server.close()
    await server.wait_closed()
    await app.shutdown()
    await handler.shutdown(10.0)
    await app.cleanup()
    redis.close()
    await redis.wait_closed()


async def init(loop):
    app = web.Application(loop=loop)
    runner: web.AppRunner = AppRunner(app)
    await runner.setup()
    handler_svc: web.Server = runner.server
    serv_generator = loop.create_server(
        handler_svc, conf['SITE_HOST'], conf['SITE_PORT'])
    return serv_generator, handler_svc, app


async def init_redis() -> aioredis.Redis:
    return await aioredis.create_redis_pool(f'redis://{conf["REDIS_HOST"]}')
