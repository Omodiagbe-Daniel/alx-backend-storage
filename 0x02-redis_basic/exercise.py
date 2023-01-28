#!/usr/bin/env python3
"""defines the class Cache and store"""
import redis
from typing import Union, Optional, Callable
import uuid
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """a decorator that takes a single method argument"""
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """wrapper function"""
        key = method.__qualname__
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper


def call_history(method: Callable) -> Callable:
    """decorator function that takes a single method argument"""
    key = method.__qualname__
    input = f"{key}:inputs"
    output = f"{key}:outputs"

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """wrapper function"""
        self._redis.rpush(input, str(args))
        outp = method(self, *args, **kwargs)
        self._redis.rpush(output, outp)
        return outp
    return wrapper


class Cache:
    """class Cache with instance property _redis"""
    def __init__(self):
        """initializing the class"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """store method that takes a data and returns a string"""
        redis_key = str(uuid.uuid4())
        self._redis.set(redis_key, data)
        return redis_key

    def get(self, key: str, fn: Optional[Callable] = None) -> (
            Union[str, bytes, int, float]):
        key1 = self._redis.get(key)
        if fn:
            return fn(self._redis.get(key))
        else:
            return key1

    def get_str(self):
        """returns a string"""
        return (str).decode(utf-8)

    def get_int(self):
        """return an integer"""
        return (int).decode(utf-8)


"""cache = Cache()

TEST_CASES = {
    b"foo": None,
    123: int,
    "bar": lambda d: d.decode("utf-8")
}

for value, fn in TEST_CASES.items():
    key = cache.store(value)
    assert cache.get(key, fn=fn) == value
"""
