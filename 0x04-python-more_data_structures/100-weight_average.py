#!/usr/bin/python3
def weight_average(my_list=[]):
    weight_sum = 0
    total_score = 0

    for i in my_list:
        total_score += i[1] * i[0]
        weight_sum += i[1]

    return total_score / weight_sum if weight_sum else 0
