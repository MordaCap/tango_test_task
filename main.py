import os
from flask import Flask
from cachetools import TTLCache
import redis


redis_host = os.environ.get('REDISHOST', 'localhost')
redis_port = int(os.environ.get('REDISPORT', 6379))
redis_client = redis.Redis(host=redis_host, port=redis_port)

ttl_cache = TTLCache(maxsize=100, ttl=5)

app = Flask(__name__)


def cache(func):
    def store_cache(uid):
        ttl_cache['uid'] = f'{uid}, {uid[::-1]}'
        redis_client.set('uid', f'{uid}, {uid[::-1]}')
        result = func(uid)
        return result
    return store_cache


def get_cache():
    if ttl_cache.get('uid'):
        return f"ttl_cache: {ttl_cache.get('uid')}"
    else:
        ttl_cache['uid'] = redis_client.get('uid')
        return f"redis_cache: {redis_client.get('uid')}"


@app.route('/')
def hello():
    return 'Hello'


@app.route('/ping', methods=['GET'])
def ping():
    return 'pong'


@app.route('/test/<uid>', methods=['POST'])
@cache
def test(uid):
    return uid


@app.route('/get_test', methods=['GET'])
def get_test():
    return get_cache()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
