#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last = abs(number) % 10
if number < 0:
    lastStr = "and is less than 6 and not 0"
    last = -last
elif last == 0:
    lastStr = "and is 0"
else:
    lastStr = "and is greater than 5"
str = f"Last digit of {number:d} is {last:d} {lastStr}"
print(str)
