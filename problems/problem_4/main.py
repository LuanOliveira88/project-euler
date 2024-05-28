from itertools import product
from math import prod

def solution(n_digits):
    max_prod = 0
    is_palindrome = lambda num: str(num) == str(num)[::-1]
    for pair in product(range(10**(n_digits - 1), 10**n_digits), repeat=2):
        if prod(pair) > max_prod and is_palindrome(prod(pair)):
            max_prod = prod(pair)
    return max_prod
