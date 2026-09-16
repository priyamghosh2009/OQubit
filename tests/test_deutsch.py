
"""
User-level test for the Deutsch algorithm.
"""

from oqubit.algorithms.deutsch import deutsch


def constant_zero(x):
    return 0


def constant_one(x):
    return 1


def balanced_identity(x):
    return x


def balanced_not(x):
    return 1 - x


print("Deutsch Algorithm")
print("=" * 40)

print("f(x) = 0")
print("Result:", deutsch(constant_zero))

print("\nf(x) = 1")
print("Result:", deutsch(constant_one))

print("\nf(x) = x")
print("Result:", deutsch(balanced_identity))

print("\nf(x) = 1 - x")
print("Result:", deutsch(balanced_not))
