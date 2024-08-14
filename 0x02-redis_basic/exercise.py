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
        key = str(uuid.uuid1())
        self._redis.set(key, data)
        return key

    def get(
        self, key: str, fn: Optional[Callable] = None
    ) -> Union[str, int, bytes, float]:
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
            return fn(data)
        return data

    def get_str(self, key: str) -> str:
        """Retrives a string format"""
        return self.get(key, str)

    def get_int(self, key: str) -> int:
        """Retrives an int format"""
        return self.get(key, int)
