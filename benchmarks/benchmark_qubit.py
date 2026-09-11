import oqubit


def test_qubit_creation(benchmark):
    benchmark(
        oqubit.Qubit,
        1,
        0,
    )


def test_qubit_zero(benchmark):
    benchmark(
        oqubit.Qubit.zero,
    )


def test_qubit_probability(benchmark):
    qubit = oqubit.Qubit(1, 1)

    benchmark(
        lambda: qubit.prob_0,
    )