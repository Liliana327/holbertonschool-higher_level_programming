#!/usr/bin/python3
"""
function that prints My name
"""

def say_my_name(first_name, last_name=""):

    Error_1 = "first_name must be a string"
    Error_2 = "last_name must be a string"

    if not isinstance(first_name, str):
        raise TypeError(Error_1)
    if not isinstance(last_name, str):
        raise TypeError(Error_2)

    print(first_name, last_name)
