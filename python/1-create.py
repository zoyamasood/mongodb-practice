#!/usr/bin/env python3

from pymongo import MongoClient, errors
from bson.json_util import dumps
import os
from db import *

new_record = {
    "address": {
      "building": "502",
      "coord": [
        -73.976112,
        40.786714
      ],
      "street": "Fifth Avenue",
      "zipcode": "10024"
    },
    "borough": "Manhattan",
    "cuisine": "Chicken",
    "name": "Mama Gina's Classy Kitchen"
}

# Insert a single record
restaurants.insert_one(new_record)

get_record = restaurants.find({"name":"Mama Gina's Classy Kitchen"})
print(dumps(get_record, indent=2))
