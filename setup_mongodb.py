"""
Script to add custom database and collection properties that needed to be added first, but only once
"""

import pymongo

def initialize_database():
    """
        Custom Field: Username as a unique text index
    """
    client = pymongo.MongoClient()
    database = client['mongodb_tutorial']
    users = database['users']
    users.create_index([("username", pymongo.TEXT)], unique=True)

if __name__ == "__main__":
    initialize_database()
