#!/usr/bin/env python3

"""Contains the list_all module"""

from typing import Dict, List
from pymongo import MongoClient


def list_all(mongo_collection: List) -> List:
    """
    List all documents in a MongoDB collection.
    Args:
        mongo_collection: The pymongo collection object.
    Returns:
        A list of documents. Returns an empty list if no document is found.
    """
    document = list(mongo_collection.find())
    if not document:
        return []
    return document
