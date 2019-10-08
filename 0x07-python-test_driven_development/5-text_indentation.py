#!/usr/bin/python3
"""
function that prints a text with 2 new lines
after each of these characters: ., ? and :
"""


def text_indentation(text):

    if not isinstance(text, str):
        raise TypeError('''text must be a string''')

    string = list(text)
    for M in range(0, len(string)):
        try:
            if string[M] is '.' or string[M] is '?' or string[M] is ':':
                string.insert(M + 1, '\n')
        except:
            continue

    string = "".join(string).split('\n')
    for M in string:
        print(M.strip())
        print() 

