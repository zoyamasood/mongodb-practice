#!/usr/bin/env python3

from pymongo import MongoClient, errors
import os
from db import *

stats = client.stats
print(stats)

dbs = client.list_database_names()
print(dbs)

thisdb = client.sample_restaurants
colls = thisdb.list_collection_names()
print(colls)

restaurants = thisdb.restaurants
count = restaurants.count_documents({})
print(count, "restaurants")

italian = restaurants.count_documents({'cuisine': 'Italian'})
print(italian, "Italian restaurants")
