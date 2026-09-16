from oqubit.algorithms.superdense_coding import encode,decode
def test_encode_00(benchmark):
    benchmark(encode, 0,0)
def test_encode_01(benchmark):
    benchmark(encode, 0,1)
def test_encode_10(benchmark):
    benchmark(encode, 1,0)
def test_encode_11(benchmark):
    benchmark(encode, 1,1)
def test_decode_00(benchmark):
    circuit=encode(0,0)
    benchmark(decode, circuit)
def test_decode_01(benchmark):
    circuit=encode(0,1)
    benchmark(decode, circuit)
def test_decode_10(benchmark):
    circuit=encode(1,0)
    benchmark(decode, circuit)
def test_decode_11(benchmark):
    circuit=encode(1,1)
    benchmark(decode, circuit)