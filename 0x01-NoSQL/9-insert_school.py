#!/usr/bin/env python3

"""Contains the insert_school module"""

from pymongo import MongoClient, collection
from typing import List, Dict


def insert_school(mongo_collection: collection.Collection, **kwargs: Dict) -> int:
    """
    Inserts a Document to a mongodb collection
    Args:
        mongo_collection: pymongo collection
        kwargs: A Dict of document to be inserted
    Returns: Document Id
    """
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
