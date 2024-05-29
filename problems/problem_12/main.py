from sympy import divisor_count

def T(n):
    return n*(n+1)//2


def solution(n_divisors=5):

    n = 1
    while divisor_count(T(n)) <= n_divisors:
        n += 1
    
    return T(n)
