from math import lcm

def solution(upper_bound):
    return lcm(*list(range(1, upper_bound+1)))