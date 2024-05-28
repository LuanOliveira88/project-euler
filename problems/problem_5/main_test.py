from main import solution

def test_solution():
    assert solution(upper_bound=10) == 2520
    assert solution(upper_bound=20) == 232792560
