# -*- coding: utf-8 -*-
"""
Created on Thu Aug 10 09:05:44 2023

@author: srushti
"""

# Python3 program to check
# URL is valid or not
# using regular expression
import re

# Function to validate URL
# using regular expression
def isValidURL(str):

	# Regex to check valid URL
	regex = ("((http|https)://)(www.)?" +
			"[a-zA-Z0-9@:%._\\+~#?&//=]" +
			"{2,256}\\.[a-z]" +
			"{2,6}\\b([-a-zA-Z0-9@:%" +
			"._\\+~#?&//=]*)")
	
	# Compile the ReGex
	p = re.compile(regex)

	# If the string is empty
	# return false
	if (str == None):
		return False

	# Return if the string
	# matched the ReGex
	if(re.search(p, str)):
		return True
	else:
		return False

# Driver code

# Test Case 1:
url = "https://www.geeksforgeeks.org"

if(isValidURL(url) == True):
	print("Yes")
else:
	print("No")

# This code is contributed by avanitrachhadiya2155
