#!/usr/bin/python3
def uniq_add(my_list=[]):
    temp = []
    sum = 0
    for item in my_list:
        if temp.count(item) == 0:
            temp.append(item)

    for item in temp:
        sum += item

    return sum
