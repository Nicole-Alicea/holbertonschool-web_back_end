#!/usr/bin/env python3
'''This function returns a list'''

import pymongo


def schools_by_topic(mongo_collection, topic):
    '''Will return the list of school having a specific topic'''

    return [x for x in mongo_collection.find({'topics': topic})]
