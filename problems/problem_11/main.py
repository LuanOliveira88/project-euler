from math import prod
import numpy as np

def get_matrix() -> np.array:
    file = ".\\problems\\problem_11\\input.txt"
    with open(file, 'r') as file:
        matrix = []
        for line in file.readlines():
            arr = line.removesuffix("\n").split(" ")
            matrix.append(list(map(int, arr)))
        return np.array(matrix)

matrix = get_matrix()
L = len(matrix)

def process_horizontal():
    
    for row in range(L):
        for col in range(L-3):
            part = matrix[row,col:col+4]
            yield part 

def process_vertical():
    
    for row in range(L-3):
        for col in range(L):
            part = matrix[row:row+4, col]
            yield part

def process_diagonal():
    
    for row in range(L-3):
        for col in range(L-3):
            part = [matrix[row+index, col+index] for index in range(4)]
            yield part

def process_antidiagonal():
    
    for row in range(3, L):
        for col in range(L-3):
            part = [matrix[row-index, col+index] for index in range(4)]
            yield part



def solution():
    
    directions_mapping = {
    'horizontal':process_horizontal, 
    'vertical':process_vertical, 
    'diagonal':process_diagonal, 
    'antidiagonal':process_antidiagonal
    }
    products = []

    for direction in directions_mapping.keys():
        for p in directions_mapping[direction]():
            products.append((p, np.prod(p)))


    return max(products, key=lambda p: p[1])[1]

 


