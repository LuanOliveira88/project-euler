#TODO: Melhorar a performance. Considere refatorar

from collections import deque

def next_number(n):
    if n%2: # odd
        return 3*n+1
    else:
        return n//2


def collatz_sequence(n):
    sequence = deque()
    while n != 1:
        sequence.append(n)
        n = next_number(n)
    sequence.append(1)
    return sequence


def main():
    file = open(".\\problems\\problem_14\\output.txt", "w")
    
    for n in range(1, 1_000_000):
        print(n, len(collatz_sequence(n)), file=file)     
    
    print('acabei!')

    file.close()

def get_longest_chain():

    with open(".\\problems\\problem_14\\output.txt", "r") as file:
        max_value = 0
        lines = file.readlines()
        for line in lines:
            pair:list[int, int] = list(map(int, line.removesuffix("\n").split(" ")))
            if pair[1] > max_value:
                max_value = pair[1]
                starting_number = pair[0]
        
        return starting_number

