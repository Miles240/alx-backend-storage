#!/usr/bin/env python3

"""Contains the scholls_by_topic module"""

from typing import List
from pymongo import MongoClient, collection


def schools_by_topic(mongo_collection: collection.Collection, topic: str) -> List:
    """
    Finds and returns the list of schools having a specific topic
    Args:
        mongo_collection (collection): pymongo collection
        topic (String): topic to be searched for
    Return (List): a list of the topics
    """
    schools = mongo_collection.find({"topics": topic})
    return schools
