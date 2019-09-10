#!/usr/bin/python3
for alfabet in range(ord('a'), ord('z') + 1):
    if alfabet != ord('e') and alfabet != ord('q'):
        print('''{}'''.format(chr(alfabet)), end="")
