#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv
    if len(argv) == 1:
        s = "arguments."
    elif len(argv) == 2:
        s = "argument:"
    else:
        s = "arguments:"
    print("{} {}".format(len(argv) - 1, s))
    number = 1
    for m in argv[1:]:
        print("{}: {}".format(number, m))
        number += 1
