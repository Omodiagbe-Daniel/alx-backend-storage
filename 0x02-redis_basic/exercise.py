#!/usr/bin/env python3
"""defines the class Cache and store"""
import redis
from typing import Union
import uuid


class Cache:
    """class Cache with instance property _redis"""
    def __init__(self):
        """initializing the class"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """store method that takes a data and returns a string"""
        redis_key = str(uuid.uuid4())
        self._redis.set(redis_key, data)
        return redis_key
