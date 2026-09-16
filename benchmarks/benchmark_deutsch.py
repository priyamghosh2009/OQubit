from oqubit.algorithms.deutsch import deutsch
def constant_zero(x):
    return 0
def constant_one(x):
    return 1
def balanced_identity(x):
    return x
def test_deutsch_constant_zero(benchmark):
    benchmark(deutsch, constant_zero)
def test_deutsch_constant_one(benchmark):
    benchmark(deutsch, constant_one)
def test_deutsch_balanced(benchmark):
    benchmark(deutsch, balanced_identity)