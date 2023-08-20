# -*- coding: utf-8 -*-
"""
Created on Sun Jul  9 02:20:55 2023

@author: srushti
"""

import pymongo

# Establish a connection to MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")
database = client["Restaurant"]

# Create the "Restaurant_details" collection
restaurant_details = database["Restaurant_details"]

# Create the "Rest_emp_details" collection
rest_emp_details = database["Rest_emp_details"]

# Create the "Invoice_details" collection
invoice_details = database["Invoice_details"]

# Insert 10 records into the "Rest_emp_details" collection
rest_emp_details.insert_many([
    {
        "rest_empid": 1,
        "rest_empname": "Rajesh",
        "rest_empemail": "rajesh@example.com",
        "rest_empaddress": "Pune",
        "rest_empsalary": 8000
    },
    {
        "rest_empid": 2,
        "rest_empname": "kartik",
        "rest_empemail": "kk@example.com",
        "rest_empaddress": "Mumbai",
        "rest_empsalary": 6000
    }

])

# Query and display the employee records with a salary greater than 7000
query = {"rest_empsalary": {"$gt": 7000}}
results = rest_emp_details.find(query)
for result in results:
    print(result)

# Perform update on "rest_empname", "rest_contactdetails", and "rest_empsalary" fields in the "Rest_emp_details" collection
query = {"rest_empsalary": {"$gt": 7000}}
update = {"$set": {
    "rest_empname": "Vedant",
    "rest_contactdetails": "987654345",
    "rest_empsalary": 9000
}}
rest_emp_details.update_many(query, update)
