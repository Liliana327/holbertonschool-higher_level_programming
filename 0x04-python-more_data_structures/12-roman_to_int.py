#!/usr/bin/python3
def roman_to_int(roman_string):
    numerals = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
    }
    arabic = 0
    if type(roman_string) is not str or roman_string is None:
        return 0
    for first_c, second_c in zip(roman_string, roman_string[1:]):
        if numerals[first_c] < numerals[second_c]:
            arabic -= numerals[first_c]
        else:
            arabic += numerals[first_c]
    arabic += numerals[roman_string[-1]]
    return arabic
