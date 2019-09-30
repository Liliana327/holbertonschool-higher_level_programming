#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        m = 0
        while m < x:
            print('''{}'''.format(my_list[m]), end='')
            m += 1
        print('')
        return m
    except IndexError:
        print('')
        return m
