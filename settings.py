from os.path import isfile
import logging


__all__ = [
    'CURRENCIES_HOST',
    'BGW_HOST',
    'EXCHANGER_GRPC_HOST',
    'WALLETS_HOST',
    'TRANSACTIONS_HOST',
    'GAS_STATION_HOST',
    'log',
]

log = logging.getLogger('app')
log.setLevel(logging.DEBUG)

f = logging.Formatter('[L:%(lineno)d]# %(levelname)-8s [%(asctime)s]  %(message)s', datefmt='%d-%m-%Y %H:%M:%S')
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
ch.setFormatter(f)
log.addHandler(ch)


DEBUG = True
SITE_HOST = "0.0.0.0"
SITE_PORT = "8000"
SECRET_KEY = 'SECRET_KEY'

CURRENCIES_HOST = ''
BGW_HOST = ''
EXCHANGER_GRPC_HOST = ''
LOANS_HOST = ''
WALLETS_HOST = ''
TRANSACTIONS_HOST = ''
GAS_STATION_HOST = ''

# MONGO_HOST = env.str('MONGO_HOST')
# MONGO_DB_NAME = env.str('MONGO_DB_NAME')

# MESSAGE_COLLECTION = 'messages'
# USER_COLLECTION = 'users'
