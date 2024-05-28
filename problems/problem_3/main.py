from sympy import primefactors

def solution(num):
    return max(primefactors(num))