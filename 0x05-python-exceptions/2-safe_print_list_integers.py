#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    m_list = 0
    for m in range(x):
        try:
            print('''{:d}'''.format(my_list[m]), end='')
            m_list += 1
        except TypeError:
            pass
        except ValueError:
            pass
    print('')
    return m_list
