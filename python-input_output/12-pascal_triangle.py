#!/usr/bin/python3
"""
This is module docstring
"""


def pascal_triangle(n):
    if n <= 0:
        return []

    if n == 1:
        return [1]

    triangle = [[1]]

    for i in range(1, n):
        prev_row = triangle[i - 1]
        
        row = [1] * (i + 1)

        for j in range(i):
            if j > 0:
                row[j] = prev_row[j - 1] + prev_row[j]

        triangle.append(row)

    return triangle
