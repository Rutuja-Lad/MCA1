# -*- coding: utf-8 -*-
"""
Created on Thu Aug 10 09:06:21 2023

@author: srushti
"""

import re  
  
def validate_password(password):  
    if len(password) < 8:  
        return False  
    if not re.search("[a-z]", password):  
        return False  
    if not re.search("[A-Z]", password):  
        return False  
    if not re.search("[0-9]", password):  
        return False  
    return True  
  
password = "P@ssw0rd"  
if validate_password(password):  
    print("Valid password")  
else:  
    print("Invalid password")  