def fibonacci(a_1, a_2, N):
    value = a_1
    sum_ = 0
    while value < N:
        if value % 2 == 0:
            sum_ += value
        a_1, a_2 = a_2, a_1 + a_2
        value = a_1
    return sum_