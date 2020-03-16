import sys
import os

sys.path.extend((os.path.abspath('..'), os.path.abspath('../..'), os.path.abspath('.'),  os.path.abspath('observer_app/rpc'),))

from .currencies_pb2_grpc import currencies__pb2 as currencies_pb2
