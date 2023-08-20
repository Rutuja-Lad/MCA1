# -*- coding: utf-8 -*-
"""
Created on Sun Jul  9 03:20:41 2023

@author: srushti
"""

import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")
database = client["Restaurant"]


restaurant_details = database["Restaurant_details"]


rest_emp_details = database["Rest_emp_details"]

invoice_details = database["Invoice_details"]

query = {"rest_empsalary": {"$gt": 1000}}
update = {"$set": {
    "rest_empname": "Vedant",
    "rest_contactdetails": "987654345",
    "rest_empsalary": 9000
}}
rest_emp_details.update_one(query, update)