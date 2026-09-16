from oqubit.algorithms.deutsch_jozsa import deutsch_jozsa


def constant_zero(bits):
    return 0


def constant_one(bits):
    return 1


def balanced_first_bit(bits):
    return bits[0]


def balanced_parity(bits):
    return sum(bits) % 2


def test_deutsch_jozsa_constant_zero(benchmark):
    benchmark(deutsch_jozsa, constant_zero, 1)


def test_deutsch_jozsa_constant_one(benchmark):
    benchmark(deutsch_jozsa, constant_one, 1)


def test_deutsch_jozsa_balanced_first_bit(benchmark):
    benchmark(deutsch_jozsa, balanced_first_bit, 2)


def test_deutsch_jozsa_balanced_parity(benchmark):
    benchmark(deutsch_jozsa, balanced_parity, 2)