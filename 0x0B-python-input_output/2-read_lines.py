#!/usr/bin/python3
"""
"""


def read_lines(filename="", nb_lines=0):
    with open(filename, mode='r', encoding="utf-8") as f:
        if nb_lines <= 0:
            print(f.read(), end='')
        else:
            while nb_lines:
                print(f.readline(), end='')
                nb_lines -= 1
