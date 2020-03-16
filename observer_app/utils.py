import aioredis
import aiohttp_jinja2
import aiohttp_debugtoolbar
import jinja2
from aiohttp.web_runner import AppRunner
from aiohttp import web

from settings import SITE_HOST
from settings import SITE_PORT
from settings import REDIS_HOST


async def on_shutdown(app):
    for ws in app['websockets']:
        await ws.close(code=1001, message='Server shutdown')


async def shutdown(server, app, handler, redis):
    server.close()
    await server.wait_closed()
    await app.shutdown()
    await handler.shutdown(10.0)
    await app.cleanup()
    redis.close()
    await redis.wait_closed()


async def init(loop):
    app = web.Application(loop=loop, middlewares=[
        # session_middleware(EncryptedCookieStorage(SECRET_KEY)),
        aiohttp_debugtoolbar.middleware,
    ])
    app.on_shutdown.append(on_shutdown)
    app['websockets'] = []
    runner: web.AppRunner = AppRunner(app)
    await runner.setup()
    handler_svc: web.Server = runner.server
    aiohttp_jinja2.setup(app, loader=jinja2.FileSystemLoader('templates'))

    # route part
    # for route in routes:
    #     app.router.add_route(route[0], route[1], route[2], name=route[3])
    # app.router.add_static('/static', 'static', name='static')
    # end route part
    serv_generator = loop.create_server(handler_svc, SITE_HOST, SITE_PORT)
    return serv_generator, handler_svc, app


async def init_redis() -> aioredis.Redis:
    return await aioredis.create_redis_pool(f'redis://{REDIS_HOST}/')
