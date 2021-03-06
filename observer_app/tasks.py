import json
import typing
import asyncio
import aioredis
from grpclib.client import Channel
from grpclib.exceptions import GRPCError

from rpc import (
    loan_grpc,
    wallets_grpc,
    currencies_grpc,
    gasstation_grpc,
    transactions_grpc,
    blockchain_gateway_grpc,
)

from rpc import (
    loan_pb2,
    wallets_pb2,
    currencies_pb2,
    gasstation_pb2,
    transactions_pb2,
    blockchain_gateway_pb2,
)
from settings.config import conf


class ResponseObject(typing.NamedTuple):
    status: str
    description: str


class BaseTask:

    """
    Base class that implement logic of sending request to external services
    by Stream message. Handling errors.
    params:
        NAME: str ; name of service
        host: str ; address(or dns) of service
        attr = 'header'; expected attr in response from where parsed status
        timeout: int = 5 ; timeout of response
        port: int = 50051; port of service
        redis_channel: str; name of redis channel
        module: typing.Any;  pb2 module generated by grpc libs
        stub: typing.Optional; service Stub generated by grpc libs
        client: typing.Optional; client connected to service
        ResponseStatus: typing.Any; enum Object to parse status from response

    example:
        class BaseTask:
            NAME = 'Currencies'
            module = currencies_pb2
            redis_channel = 'currencies'
            host = conf['CURRENCIES_HOST']
            stub = currencies_grpc.CurrenciesServiceStub
            ResponseStatus = module.ResponseStatus
    """

    NAME: str
    host: str
    attr = 'header'
    timeout: int = 5
    port: int = 50051
    redis_channel: str
    module: typing.Any
    stub: typing.Optional
    client: typing.Optional
    ResponseStatus: typing.Any

    def __init__(self):
        self.client = self.stub(Channel(self.host, self.port))

    async def get_status(self) -> str:
        """
        Method to get Health status from external service and handle error
        if it necessary

        return: Json string

        example:
            "{'Service': 'Currencies',
            'Status': 'ERROR',
            'Description': "111 Connect call failed ('0.0.0.0', 50051)",
            'Host': '0.0.0.0',
            'Port': 50051}"
        """
        try:
            result = await self._execute()
            header = getattr(result, self.attr)
            result = ResponseObject(
                    self.ResponseStatus.Name(header.status),
                    header.description
            )
        except GRPCError as exc:
            result = ResponseObject(
                    exc.status.name,
                    exc.message
            )
        except ConnectionRefusedError as exc:
            result = ResponseObject(
                    self.ResponseStatus.Name(self.module.ERROR),
                    ' '.join([f'{arg}'for arg in exc.args])
            )
        return json.dumps({
                'Service': self.NAME,
                'Status': result.status,
                'Description': result.description,
                'Host': self.host,
                'Port': self.port,
            }, indent=4)

    async def _execute(self):
        raise NotImplementedError('Method Not implemented!!')

    async def publish(self, redis: aioredis.Redis):
        """
        Method that publish data to redis
        """
        data = await self.get_status()
        await redis.publish(f'channel:{self.redis_channel}', data)


class CurrenciesTask(BaseTask):
    NAME = 'Currencies'
    module = currencies_pb2
    redis_channel = 'currencies'
    host = conf['CURRENCIES_HOST']
    ResponseStatus = module.ResponseStatus
    stub = currencies_grpc.CurrenciesServiceStub

    async def _execute(self):
        async with self.client.Health.open(timeout=self.timeout) as stream:
            await stream.send_message(self.module.HealthzRequest())
            return await stream.recv_message()


class BGWTask(BaseTask):
    attr = 'status'
    host = conf['BGW_HOST']
    NAME = 'Blockchain-gateway'
    module = blockchain_gateway_pb2
    redis_channel = 'blockchain-gateway'
    ResponseStatus = module.ResponseStatus
    stub = blockchain_gateway_grpc.BlockchainGatewayServiceStub

    async def _execute(self):
        async with self.client.Health.open(timeout=self.timeout) as stream:
            await stream.send_message(self.module.EmptyRequest())
            return await stream.recv_message()


class LoansTask(BaseTask):
    NAME = 'Loans'
    module = loan_pb2
    redis_channel = 'loans'
    host = conf['LOANS_HOST']
    stub = loan_grpc.LoanServiceStub
    ResponseStatus = module.ResponseResult

    async def _execute(self):
        async with self.client.Healthz.open(timeout=self.timeout) as stream:
            await stream.send_message(self.module.HealthzRequest())
            return await stream.recv_message()


class WalletsTask(LoansTask):
    NAME = 'Wallets'
    module = wallets_pb2
    redis_channel = 'wallets'
    host = conf['WALLETS_HOST']
    stub = wallets_grpc.WalletsStub
    ResponseStatus = module.ResponseStatus


class TransactionsTask(WalletsTask):
    NAME = 'Transactions'
    module = transactions_pb2
    redis_channel = 'transactions'
    host = conf['TRANSACTIONS_HOST']
    stub = transactions_grpc.TransactionsStub


class GasStationTask(WalletsTask):
    NAME = 'GasStation'
    module = gasstation_pb2
    redis_channel = 'gasStation'
    host = conf['GASSTATION_HOST']
    stub = gasstation_grpc.GasStationServiceStub


all_tasks = [
    BGWTask,
    LoansTask,
    WalletsTask,
    GasStationTask,
    CurrenciesTask,
    TransactionsTask,
]


async def get_task(iterable: typing.Iterable):
    """
    async iterable python
    """
    for i in iterable:
        await asyncio.sleep(0.0001)
        yield i


async def runner(redis):
    """
    Simple coroutine that release logic of monitoring services
    """
    while True:
        await asyncio.sleep(conf['DELAY_FOR_RUNNER'])
        async for task in get_task(all_tasks):
            await task().publish(redis)
