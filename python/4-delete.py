#!/usr/bin/env python3

from pymongo import MongoClient, errors
from bson.json_util import dumps
import os
from db import *


# Deletes first one it finds matching criteria
restaurants.delete_one({"name":"Mama Gina's Classy Kitchen"}

## Deletes all documents w/ found matching criteria
# restaurants.delete_many({"borough":"Brooklyn"})

## Delete all documents in a collection
# restaurants.delete_many({})
