#!/usr/bin/python3
def remove_char_at(str, number):
    if number < len(str) and number >= 0:
        new_string = str[:number] + str[number + 1:]
        return (new_string)
    else:
        return (str)
