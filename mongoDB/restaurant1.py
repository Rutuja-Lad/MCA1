# -*- coding: utf-8 -*-
"""
Created on Sun Jul  9 02:28:46 2023

@author: srushti
"""



import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")
database = client["Restaurant"]


restaurant_details = database["Restaurant_details"]


rest_emp_details = database["Rest_emp_details"]

invoice_details = database["Invoice_details"]


rest_emp_details.insert_many([
    {
        "rest_empid": 1,
        "rest_empname": "Rajesh",
        "rest_empemail": "rajesh@example.com",
        "rest_empaddress": "Pune",
        "rest_empsalary": 800
    },
    {
        "rest_empid": 2,
        "rest_empname": "kartik",
        "rest_empemail": "kk@example.com",
        "rest_empaddress": "Mumbai",
        "rest_empsalary": 6000
    },
    {
        "rest_empid": 3,
        "rest_empname": "vedika",
        "rest_empemail": "vv@example.com",
        "rest_empaddress": "Pune",
        "rest_empsalary": 800
    },
    {
        "rest_empid":4 ,
        "rest_empname": "Kajal",
        "rest_empemail": "kk@example.com",
        "rest_empaddress": "Pune",
        "rest_empsalary": 800
    },
    {
        "rest_empid": 5,
        "rest_empname": "Ankit",
        "rest_empemail": "aa@example.com",
        "rest_empaddress": "Mumbai",
        "rest_empsalary": 3000
    },
    {
        "rest_empid": 6,
        "rest_empname": "Tejas",
        "rest_empemail": "tt@example.com",
        "rest_empaddress": "Kolhapur",
        "rest_empsalary": 5000
    },
    {
        "rest_empid":7 ,
        "rest_empname": "Srush",
        "rest_empemail": "ss@example.com",
        "rest_empaddress": "Kolhapur",
        "rest_empsalary": 4000
    },
    {
        "rest_empid": 8,
        "rest_empname": "shrav",
        "rest_empemail": "ss@example.com",
        "rest_empaddress": "Pune",
        "rest_empsalary": 6000
    },
    {
        "rest_empid": 9,
        "rest_empname": "shravan",
        "rest_empemail": "ss@example.com",
        "rest_empaddress": "Pune",
        "rest_empsalary": 9000
    },
    {
        "rest_empid": 10,
        "rest_empname": "Satyam",
        "rest_empemail": "ss@example.com",
        "rest_empaddress": "Pune",
        "rest_empsalary": 18000
    }

])

restaurant_details.find()

query = {"rest_empsalary": {"$gt": 7000}}
results = rest_emp_details.find(query)
for result in results:
    print(result)


query = {"rest_empsalary": {"$gt": 55000}}
update = {"$set": {
    "rest_empname": "Vedant",
    "rest_contactdetails": "987654345",
    "rest_empsalary": 9000
}}
rest_emp_details.update_one(query, update)
