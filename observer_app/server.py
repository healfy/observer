import asyncio

from tasks import runner
from utils import (
    init,
    shutdown,
    init_redis
)
from settings.config import conf
from reader import start_reading


def main(loop, redis):
    serv_generator, handler, app = loop.run_until_complete(init(loop))
    serv = loop.run_until_complete(serv_generator)
    loop.create_task(runner(redis))

    print('start server %s' % str(serv.sockets[0].getsockname()))
    try:
        loop.run_forever()
    except KeyboardInterrupt:
        print(' Stop server begin')
    finally:
        loop.run_until_complete(shutdown(serv, app, handler, redis))
        loop.close()
    print('Stop server end')


if __name__ == '__main__':
    ev_loop = asyncio.get_event_loop()
    redis_client = ev_loop.run_until_complete(init_redis())
    if conf['DEBUG']:
        start_reading(ev_loop, redis_client)
    main(ev_loop, redis_client)
