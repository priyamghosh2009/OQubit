"""
Tests for the Bernstein-Vazirani algorithm.
"""
from oqubit.algorithms.bernstein_vazirani import bernstein_vazirani
def test_bernstein_vazirani_1011():
    result = bernstein_vazirani("1011")
    assert result == "1011"
def test_bernstein_vazirani_0000():
    result = bernstein_vazirani("0000")
    assert result == "0000"
def test_bernstein_vazirani_1111():
    result = bernstein_vazirani("1111")
    assert result == "1111"