import typing
import asyncio
from google.protobuf import reflection
from grpclib.client import Channel
from grpclib.exceptions import GRPCError
from rpc.currencies_grpc import CurrenciesServiceStub
from rpc import currencies_pb2
from .settings import *


class ResponseObject(typing.NamedTuple):
    status: str
    description: str


class BaseTask:
    host: str
    port: int = 50051
    stub: typing.Optional
    client: typing.Optional
    timeout: int = 5
    method: typing.Type['reflection.GeneratedProtocolMessageType']
    module = currencies_pb2
    attr = 'header'

    def __init__(self):
        self.client = self.stub(Channel(self.host, self.port))

    async def get_status(self) -> ResponseObject:
        try:
            result = await self._execute()
            header = getattr(result, self.attr)
            result = ResponseObject(
                    self.module.ResponseStatus.Name(header.status),
                    header.description
            )
        except GRPCError as exc:
            result = ResponseObject(
                    exc.status.name,
                    exc.message
            )
        except ConnectionRefusedError as exc:
            result = ResponseObject(
                    self.module.ResponseStatus.Name(self.module.ERROR),
                    ' '.join([f'{arg}'for arg in exc.args])
            )
        return result

    async def _execute(self):
        raise NotImplementedError('Method Not implemented!!')


class CurrenciesTask(BaseTask):
    host = CURRENCIES_HOST
    stub: typing.Type['CurrenciesServiceStub'] = CurrenciesServiceStub
    module = currencies_pb2

    async def _execute(self):
        async with self.client.Health.open(timeout=self.timeout) as stream:
            await stream.send_message(self.module.HealthzRequest())
            return await stream.recv_message()


tasks = [CurrenciesTask()]


async def runner():
    while True:
        await asyncio.sleep(2)
        for task in tasks:
            result: currencies_pb2.HealthzResponse = await task.get_status()
            r = {
                'Service': 'Currencies',
                'Status': result.status,
                'Description': result.description,
                'Host': task.host,
                'Port': task.port,
            }
            print(r)
