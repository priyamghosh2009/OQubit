"""
User-level test for the Superdense Coding algorithm.
"""
from oqubit.algorithms.superdense_coding import encode, decode
print("Superdense Coding")
print("=" * 40)
messages = [
    (0, 0),
    (0, 1),
    (1, 0),
    (1, 1),
]
for bit_a, bit_b in messages:
    encoded = encode(bit_a, bit_b)
    decoded = decode(encoded)
    print(f"{bit_a}{bit_b} -> {decoded}")