import os
from redis import StrictRedis

REDIS_HOST = os.environ.get('REDIS_HOST')
REDIS_PORT = os.environ.get('REDIS_PORT')
REDIS_PW = os.environ.get('REDIS_PW')
cache = StrictRedis()
