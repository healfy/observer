import asyncio
from tasks import runner
from tasks import reader
from utils import init, shutdown, init_redis
from settings import log


def main():
    loop = asyncio.get_event_loop()
    redis = loop.run_until_complete(init_redis())
    sub = loop.run_until_complete(init_redis())
    res = loop.run_until_complete(sub.subscribe('channel:currencies'))
    ch1 = res[0]

    serv_generator, handler, app = loop.run_until_complete(init(loop))
    serv = loop.run_until_complete(serv_generator)
    loop.create_task(runner(redis))
    loop.create_task(reader(ch1))
    log.debug('start server %s' % str(serv.sockets[0].getsockname()))
    try:
        loop.run_forever()
    except KeyboardInterrupt:
        log.debug(' Stop server begin')
    finally:
        loop.run_until_complete(shutdown(serv, app, handler, redis))
        loop.close()
    log.debug('Stop server end')


if __name__ == '__main__':
    main()
