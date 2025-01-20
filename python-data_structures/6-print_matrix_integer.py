#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for i in range(len(matrix)):
        if len(matrix[i]) > 0:
            for j in range(len(matrix[i])):
                end = ' ' if j < len(matrix[j]) - 1 else '\n'
                print('{:d}'.format(matrix[i][j]), end=end)
        else:
            print("")
