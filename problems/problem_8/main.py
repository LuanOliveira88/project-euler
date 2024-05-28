from math import prod


def solution(n_adj):
    with open(".\\problems\\problem_8\\input.txt", "r") as file:
        number = file.read().replace("\n", "").strip()

        parts = [tuple(map(int, number[i:i+n_adj])) for i in range(len(number)) if i+n_adj < len(number)]
        products = list(map(prod, parts))
        max_prod = max(products)
        return max_prod
        