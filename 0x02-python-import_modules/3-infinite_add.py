#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv
    a = 0
    b = 0
    for m in argv[1:]:
        b = int(m)
        a += b
    print("{}".format(a))
