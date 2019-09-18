#!/usr/bin/python3
def no_c(my_string):
    my_string = list(my_string)
    for m in my_string:
        if m == 'c':
            my_string.remove('c')
        elif m == 'C':
            my_string.remove('C')
        else:
            continue
    return ''.join(my_string)
