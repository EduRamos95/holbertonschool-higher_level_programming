#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix is None or matrix == "":
        print()
    row_total = len(matrix)
    for row in range(row_total):
        for col in range(len(matrix[row])):
            print('{:d}'.format(matrix[row][col]), end='')
            if col is not (len(matrix[row]) - 1):
                print(end=" ")
        print("")
