#!/usr/bin/python3
"""
"""


def number_of_lines(filename=""):

    contador = 0
    with open(filename, mode='r', encoding="utf-8") as f:
        while f.readline():
            contador += 1
    return contador
