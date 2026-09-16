"""
Tests for the Deutsch-Jozsa algorithm.
"""

from oqubit.algorithms.deutsch_jozsa import deutsch_jozsa


def constant_zero(bits):
    return 0


def constant_one(bits):
    return 1


def balanced_first_bit(bits):
    return bits[0]


def balanced_parity(bits):
    return sum(bits) % 2


def test_constant_zero():
    result = deutsch_jozsa(constant_zero, 1)
    assert result == "constant"


def test_constant_one():
    result = deutsch_jozsa(constant_one, 1)
    assert result == "constant"


def test_balanced_first_bit():
    result = deutsch_jozsa(balanced_first_bit, 2)
    assert result == "balanced"


def test_balanced_parity():
    result = deutsch_jozsa(balanced_parity, 2)
    assert result == "balanced"
