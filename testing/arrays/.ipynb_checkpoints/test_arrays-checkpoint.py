import pytest

from arrays import add_arrays, subtract_arrays

@pytest.fixture
def pair_of_lists():
    return [1, 2, 3], [4, 5, 6]


def test_add_arrays(pair_of_lists):
    a, b = pair_of_lists
    expect = [5, 7, 9]
    
    output = add_arrays(a, b)
    
    assert output == expect


def test_subtract_arrays(pair_of_lists):
    a, b = pair_of_lists
    expect = [-3, -3, -3]
    
    output = subtract_arrays(a, b)
    
    assert output == expect
