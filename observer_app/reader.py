import asyncio
from aioredis import Redis
from aioredis.pubsub import Channel
from tasks import all_tasks


def start_reading(loop: asyncio.AbstractEventLoop, redis: Redis):
    """
    Simple functions to monitoring data from channels for debug
    Works if DEBUG mode is enabled
    """
    channels = []

    for t in all_tasks:
        res = loop.run_until_complete(
            redis.subscribe(f'channel:{t.redis_channel}'))
        channels.append(res[0])

    for ch in channels:
        loop.create_task(reader(ch))


async def reader(ch: Channel):
    while await ch.wait_message():
        msg = await ch.get_json()
        print(f" {ch.name.upper()} got message:", msg)

