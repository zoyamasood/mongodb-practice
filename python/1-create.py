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

# Now insert and pull the new document out using find()