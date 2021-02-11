import pytest
from calc_itog import comp

def test_comp():
    listt,a=[20,5],30
    result=[30]
    assert comp(listt,a)==result
