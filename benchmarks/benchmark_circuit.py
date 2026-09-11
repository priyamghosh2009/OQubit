import oqubit


def test_bell_circuit(benchmark):
    circuit = oqubit.Circuit(2)

    circuit.h(0)
    circuit.cx(0, 1)

    benchmark(circuit.run)


def test_8_qubit_circuit(benchmark):
    circuit = oqubit.Circuit(8)

    for i in range(8):
        circuit.h(i)

    for i in range(7):
        circuit.cx(i, i + 1)

    benchmark(circuit.run)