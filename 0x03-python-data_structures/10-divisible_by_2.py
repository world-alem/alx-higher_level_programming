#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    temp = []
    for i in my_list:
        temp.append(i % 2 == 0)
    return temp
