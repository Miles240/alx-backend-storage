#!/usr/bin/env pytho3

"""Contains the top_students module"""

from pymongo import MongoClient, collection


def top_students(mongo_collection: collection.Collection) -> collection.Collection:
    """
    Add a new field 'averageScore' that calculates the average of the 'scores' array
    """
    return mongo_collection.aggregate(
        [
            {"$project": {"name": "$name", "averageScore": {"$avg": "$topics.score"}}},
            {"$sort": {"averageScore": -1}},
        ]
    )
