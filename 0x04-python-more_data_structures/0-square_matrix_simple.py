#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = [[items * items for items in row] for row in matrix]
    return new_matrix
