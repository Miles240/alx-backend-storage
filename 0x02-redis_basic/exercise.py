#!/usr/bin/env python3

"""Contains the Cache class"""

import redis
import uuid
from typing import Union, Callable, Optional


class Cache:
    """Cache class"""

    def __init__(self):
        self._redis = redis.Redis(decode_responses=True)
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Stores the input data in Redis using a random key and returns the key
        Args:
            data(Union[str, byte, int, float]): input data
        Returns:
            key(string): uuuid string
        """
        rkey = str(uuid.uuid1())
        self._redis.set(rkey, data)
        return rkey

    def get(
        self, key: str, fn: Optional[Callable] = None
    ) -> Optional[Union[str, int, bytes, float]]:
        """
        Retrieves data from Redis and applies an optional function to transform the data.
        Args:
            key(str): The key to retrieve data from Redis.
            fn(Optional[Callable]): A function to apply to the retrieved data.
        Returns:
            Transformed data or the raw data if no function is provided.
        """

        data = self._redis.get(key)
        if data is None:
            return None
        if fn:
            data = fn(data)
        return data

    def get_str(self, key: str) -> str:
        """Retrives a string format"""
        data = self._redis.get(key)
        return data.decode("utf-8")

    def get_int(self, key: str) -> int:
        """Retrives an int format"""
        data = self._redis.get(key)
        try:
            data = int(data.decode("utf-8"))
        except Exception:
            data = 0
        return data


cache = Cache()

TEST_CASES = {b"foo": None, 123: int, "bar": lambda d: d.decode("utf-8")}

for value, fn in TEST_CASES.items():
    key = cache.store(value)
    assert cache.get(key, fn=fn) == value
