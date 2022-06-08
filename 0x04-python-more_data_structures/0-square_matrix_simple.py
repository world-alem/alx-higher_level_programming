#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []

    for i in matrix:
        temp = []
        for j in i:
            temp.append(j**2)
        new_matrix.append(temp)

    return new_matrix
