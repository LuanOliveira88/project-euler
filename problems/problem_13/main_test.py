from main import solution, get_numbers

def test_get_numbers():

    for number in get_numbers():
        assert isinstance(number, str)
        assert len(number) == 50
        assert len(number[-10:]) == 10
    

def test_solution():
    
    assert solution(10) == 5537376230

    