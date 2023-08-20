# -*- coding: utf-8 -*-
"""
Created on Wed Aug  9 16:35:32 2023

@author: srushti
"""

import pymongo

client=pymongo.MongoClient("mongodb://localhost:27017/")

db=client["Demo"]
mycol=db["Emp"]

mylist=[
        {"name":"pratiksha","address":"nashik"},
        {"name":"pooja","address":"sangali"},
        {"name":"rutuja","address":"jalgaon"},
        {"name":"darshana","address":"buldhana"}
    ]

mycol.insert_many(mylist)

for x in mycol.find():
 print(x)
        