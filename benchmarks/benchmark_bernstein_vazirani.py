from oqubit.algorithms.bernstein_vazirani import bernstein_vazirani
def test_bernstein_vazirani_1011(benchmark):
    benchmark(bernstein_vazirani, "1011")
def test_bernstein_vazirani_0000(benchmark):
    benchmark(bernstein_vazirani, "0000")
def test_bernstein_vazirani_1111(benchmark):
    benchmark(bernstein_vazirani, "1111")
def test_bernstein_vazirani_10101010(benchmark):
    benchmark(bernstein_vazirani, "10101010")