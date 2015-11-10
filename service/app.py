import socket

from flask import Flask
from redis import Redis


app = Flask(__name__)
redis = Redis(host='redis', port=6379)
hostname = socket.gethostname()


@app.route('/')
def hello():
    redis.incr('hits')

    return 'This is %s! There have been %s total hits.' % (
        hostname,
        redis.get('hits'),
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
