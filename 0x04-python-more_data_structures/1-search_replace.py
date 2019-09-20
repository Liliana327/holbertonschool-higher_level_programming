#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = my_list.copy()
    for m, items in enumerate(my_list):
        if items == search:
            new_list[m] = replace
    return new_list
