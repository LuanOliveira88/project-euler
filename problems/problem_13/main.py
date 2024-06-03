
def get_numbers(file_: str=".\\problems\\problem_13\\input.txt")->list:
    
    with open(file=file_, mode='r') as file:
        
        numbers: list[str] = list(map(lambda s: s.removesuffix('\n'), file.readlines()))
        
        return numbers
        

def solution(n_digits=10):

    sum_ = 0

    for number in get_numbers():
        sum_ += int(number)
    
    return int(str(sum_)[:n_digits])
