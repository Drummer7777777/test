import pytest
from calc_itog import summ,razn,umn,chast

def test_summ():
    a,b=20,5
    result=25
    assert summ(a,b)==result 

def test_razn():
    a,b=20,5
    result=15
    assert razn(a,b)==result 

def test_umn():
    a,b=20,5
    result=100
    assert umn(a,b)==result

def test_chast():
    a,b=5,20
    result=4
    assert chast(20,5)==result