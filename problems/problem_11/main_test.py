from main import process_horizontal, process_vertical, process_diagonal, process_antidiagonal, solution
import numpy as np


def test_get_directions():

    directions = [tuple(direction) for direction in process_horizontal()]
    assert (8, 2, 22, 97) in directions
    assert (50, 77, 91, 8) in directions
    assert (1, 70, 54, 71) in directions
    assert (89, 19, 67, 48) in directions

    directions = [tuple(direction) for direction in process_vertical()]
    assert (8, 49, 81, 52) in directions
    assert (8, 0, 65, 91) in directions
    assert (4, 20, 20, 1) in directions
    assert (36, 16, 54, 48) in directions

    
    directions = [tuple(direction) for direction in process_diagonal()]
    assert (8, 49, 31, 23) in directions
    assert (50, 56, 36, 91) in directions
    assert (4, 69, 35, 71) in directions
    assert (40, 4, 5, 48) in directions

    directions = [tuple(direction) for direction in process_antidiagonal()]
    assert (52, 49, 99, 97) in directions
    assert (37, 13, 62, 8) in directions
    assert (1, 73, 36, 73) in directions
    assert (89, 57, 36, 36) in directions

    assert solution() == 70600674