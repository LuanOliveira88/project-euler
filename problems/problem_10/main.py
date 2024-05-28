from sympy import isprime


def solution(N):
    odds = range(1, N, 2)
    primes = filter(isprime, odds)
    return sum(primes) + 2
