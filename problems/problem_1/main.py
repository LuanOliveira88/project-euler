def solution(upper):
    return sum(list(filter(lambda n: n%3 == 0 or n%5 == 0, range(upper))))