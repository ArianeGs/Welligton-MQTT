import requests
from rq import Queue
from redis import Redis
from somewhere import count_words_at_url
import time

def count_words_at_url(url):
    resp = requests.get(url)
    return len(resp.text.split())



# Tell RQ what Redis connection to use
redis_conn = Redis()
q = Queue(connection=redis_conn)  # no args implies the default queue

# Delay execution of count_words_at_url('http://nvie.com')
job = q.enqueue(count_words_at_url, 'http://nvie.com')
print(job.result)   # => None

# Now, wait a while, until the worker is finished
time.sleep(2)
print(job.result)   # => 889

q = Queue('low', connection=redis_conn)
q.enqueue(count_words_at_url, 'http://nvie.com')