#!/usr/bin/python3
def uppercase(str):
    temp = ''
    for s in str:
        if (ord(s) >= 97 and ord(s) <= 97+26):
            temp += chr(ord(s)-(97-65))
        else:
            temp += s
    print("{}".format(temp))
