import os
from flask import Flask, url_for
from cachetools import TTLCache
import redis


redis_host = os.environ.get('REDISHOST', 'localhost')
redis_port = int(os.environ.get('REDISPORT', 6379))
redis_client = redis.Redis(host=redis_host, port=redis_port)

ttl_cache = TTLCache(maxsize=100, ttl=5)

app = Flask(__name__)
# tell Flask to use the above defined config


def cache(func):
    def store_cache(uid):
        ttl_cache['uid'] = (uid, uid[::-1])
        redis_client.set('uid', (uid, uid[::-1]))
        result = func(uid)
        return result
    return store_cache


def get_cache():
    return redis_client.get('uid'), ttl_cache.get('uid')


@app.route('/ping', methods=['GET'])
def ping():
    return 'pong'


@app.route('/test/<uid>', methods=['POST'])
@cache
def test(uid):
    return uid


@app.route('/get_test', methods=['GET'])
def get_test():
    return f'{get_cache()}'


if __name__ == '__main__':
    # This is used when running locally. Gunicorn is used to run the
    # application on Google App Engine and Cloud Run.
    # See entrypoint in app.yaml or Dockerfile.
    app.run(host='0.0.0.0', port=5000, debug=True)
