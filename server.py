import asyncio
from tasks import runner
from utils import init, log, shutdown


def main():
    loop = asyncio.get_event_loop()
    serv_generator, handler, app = loop.run_until_complete(init(loop))
    serv = loop.run_until_complete(serv_generator)
    loop.create_task(runner())
    log.debug('start server %s' % str(serv.sockets[0].getsockname()))
    try:
        loop.run_forever()
    except KeyboardInterrupt:
        log.debug(' Stop server begin')
    finally:
        loop.run_until_complete(shutdown(serv, app, handler))
        loop.close()
    log.debug('Stop server end')


if __name__ == '__main__':
    main()
