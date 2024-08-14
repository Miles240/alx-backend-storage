#!/usr/bin/env python3

"""Contains the Cache class"""

import redis
import uuid
from typing import Union


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
        self.key = str(uuid.uuid1())
        self._redis.set(self.key, data)
        return self.key
