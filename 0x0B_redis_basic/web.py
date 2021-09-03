#!/usr/bin/env python3
""" Module that holds implementing an
    expiring web cache and tracker
"""


from typing import Callable
from functools import wraps
import redis
import requests


def url_request(method: Callable) -> Callable:
    """ Method that holds a url_request function
    """
    @wraps(method)
    def wrapper(*args, **kwds):
        """ Method that holds a wrapped function,
            which allows access to the Redis instance
        """
        self._redis = redis.Redis()
        self._redis.incr('count:' + args[0])
        new_url = self._redis.get(args[0])
        if new_url:
            return new_url
        else:
            new_url = method(*args, **kwds)
            self._redis.setex(args[0], 10, new_url)
    return wrapper


@countURL
def get_page(url: str) -> str:
    """ Method that the request module uses to get
        the HTML content of a particular URL, it tracks
        how many times that URL was accessed,
        caches the result, and returns it
    """
    access_url = requests.get(new_url)
    return access_url.text
