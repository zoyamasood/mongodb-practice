#!/usr/bin/env python3

from pymongo import MongoClient, errors
from bson.json_util import dumps
import os
from db import *

# Updates a single record - the first matching criteria
# using the $set operator


# Update a single record - add tags
# using the $push operator


# The full list of mongodb operators is here:
# https://docs.mongodb.com/manual/reference/operator/

get_record = restaurants.find({"name":"Mama Gina's Classy Kitchen"})
print(dumps(get_record, indent=2))