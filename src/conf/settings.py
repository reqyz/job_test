from os.path import isfile

from envparse import env

if isfile('.env'):
    env.read_envfile('.env')

DATABASE_URL = env('DATABASE_URL')
MIN_CONNECTION_POOL_SIZE = env('MIN_CONNECTION_POOL_SIZE', 1)
MAX_CONNECTION_POOL_SIZE = env('MAX_CONNECTION_POOL_SIZE', 2)

HOST = env('HOST', '0.0.0.0')
PORT = env('PORT', '8001')
