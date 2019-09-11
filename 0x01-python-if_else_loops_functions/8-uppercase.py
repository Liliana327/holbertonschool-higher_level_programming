#!/usr/bin/python3
def uppercase(str):
    for string in range(len(str)):
        m = ord(str[string])
        if str[string].islower():
            m = m - 32
        m = chr(m)
        print('''{}'''.format(m), end="")
    print()
