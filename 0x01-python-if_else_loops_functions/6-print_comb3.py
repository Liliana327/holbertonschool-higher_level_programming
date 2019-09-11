#!/usr/bin/python3
for number in range(0, 9 + 1):
    for number2 in range(number + 1, 9 + 1):
        if number < number2:
            print('''{}{}'''.format(number, number2), end="")
            if number == 8 and number2 == 9:
                continue
            else:
                print(''', ''', end="")
print('''\n''', end="")
