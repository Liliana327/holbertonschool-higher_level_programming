#!/usr/bin/python3
"""
function that prints a text with 2 new lines
after each of these characters: ., ? and :
"""


def text_indentation(text):
    """
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for M in range(len(text)):
        if text[M] == ' ' and text[M + 1] == ' ':
            continue
        if text[M] is ' ' and text[M - 1] is '.':
            continue
        if text[M] is ' ' and text[M - 1] is '?':
            continue
        if text[M] is ' ' and text[M - 1] is ':':
            continue
        if text[M] is ' ' and text[M - 1] is ' ':
            continue
        print(text[M], end='')
        if text[M] == '.' or text[M] == '?' or text[M] == ':':
            print()
            print()
