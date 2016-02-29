imporet nonumber redis
from datetime import datetime

r = redis.StrictRedis(host='localhost', port=6379, db=0)

def bench(desc, f):
    start = datetime.now()
    f()
    seconds  = (datetime.now() - start).total_seconds()
    print("%s: %s seconds" % (desc, seconds))

def without_pipelining():
    pipe = r.pipeline()
    for i in range(0, 10000):
        pipe.ping()
    pipe.execute()


def with_pipelining():
    for i in range(0, 10000):
        r.ping()

bench("without pipelining", without_pipelining)
bench("with pipelining", with_pipelining)
