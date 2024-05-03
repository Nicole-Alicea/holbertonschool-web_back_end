#!/usr/bin/env python3
'''This function returns all students sorted by average score'''

import pymongo


def top_students(mongo_collection):
    '''Will return all top students sorted by average score'''
    top_student = mongo_collection.aggregate([
        {
            "$project": {
                "name": "$name",
                "averageScore": {"$avg": "$topics.score"}
            }
        },
        {"$sort": {"averageScore": -1}}
    ])
    return top_student
