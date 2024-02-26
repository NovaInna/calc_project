import pytest

from calc_rep.calc import sum as calc_sum
from calc_rep.calc import mul as calc_mul
from calc_rep.calc import div as calc_div
from calc_rep.calc import sub as calc_sub

test_data_sum = [
    (1,1,2),
    (2,3,5),
    (-1, 1, 0),
    (0,0,0),
    (12.2, 34.3, 46.5)
]

test_data_mul = [
    (1,1,1),
    (1,0,0),
    (-1, 5, -5),
    (0.5, 2, 1)
]

test_data_div = [
    (4,2,2),
    (0, 3, 0),
    (5,1,5),
    (5,2,2.5)
]

test_data_sub = [
    (6,2,4),
    (1,5,-4)
]

@pytest.mark.parametrize("a,b,expected_result", test_data_sum)
def test_sum(a,b,expected_result):
    fact_result = calc_sum(a,b)
    assert expected_result == fact_result

@pytest.mark.parametrize("a,b,expected_result", test_data_mul)
def test_mul(a,b,expected_result):
    fact_result = calc_mul(a,b)
    assert expected_result == fact_result


@pytest.mark.parametrize("a,b,expected_result", test_data_div)
def test_div(a,b,expected_result):
    fact_result = calc_div(a,b)
    assert expected_result == fact_result

@pytest.mark.parametrize("a,b,expected_result", test_data_sub)
def test_sub(a,b,expected_result):
    fact_result = calc_sub(a,b)
    assert expected_result == fact_result