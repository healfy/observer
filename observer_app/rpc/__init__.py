import sys
import os

sys.path.extend((os.path.abspath('..'), os.path.abspath('../..'), os.path.abspath('.'),  os.path.abspath('observer_app/rpc'),))

from rpc.currencies_pb2_grpc import currencies__pb2 as currencies_pb2
from rpc.blockchain_gateway_pb2_grpc import blockchain__gateway__pb2 as blockchain_gateway_pb2
from rpc.loan_pb2_grpc import loan__pb2 as loan_pb2
from rpc.wallets_pb2_grpc import wallets__pb2 as wallets_pb2
from rpc.gasstation_pb2_grpc import gasstation__pb2 as gasstation_pb2
from rpc.transactions_pb2_grpc import transactions__pb2 as transactions_pb2
