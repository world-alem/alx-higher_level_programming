#!/usr/bin/python3
for i in range(97, 97+26):
    if (i == 97+4 or i == 97+16):
        continue
    print("{}".format(chr(i)), end="")
