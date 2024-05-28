def solution(upper_bound):
    square_of_sum = lambda n: (n*(n+1)//2)**2
    sum_of_squares = lambda n: (n*(n+1)*(2*n+1)//6)

    return square_of_sum(upper_bound) - sum_of_squares(upper_bound)