#!/usr/bin/env python3

"""Contains the update_topics module"""

from typing import List
from pymongo import MongoClient, collection


def update_topics(
    mongo_collection: collection.Collection, name: str, topics: List[str]
) -> None:
    """
    Updates or changes all topics of a document
        Args:
            mongo_collection: pymongo collection
            name: name of the document to recieve the changes
            topics: changes to be made
    """
    query_filter = {"name": name}
    update_operation = {"$set": {"topics": topics}}
    mongo_collection.update_many(
        query_filter, update_operation, bypass_document_validation=True
    )
