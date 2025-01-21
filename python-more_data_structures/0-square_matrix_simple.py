#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    new_matrix = [[]] * len(matrix)

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if j == 0:
                new_matrix[i] = [matrix[i][j] ** 2]
            else:
                new_matrix[i].append(matrix[i][j] ** 2)

    return new_matrix
