import oqubit


def test_statevector_4_qubits(benchmark):
    def create_state():
        state = oqubit.StateVector(
            [
                oqubit.Qubit.zero(),
                oqubit.Qubit.zero(),
                oqubit.Qubit.zero(),
                oqubit.Qubit.zero(),
            ]
        )
        return state

    benchmark(create_state)


def test_statevector_8_qubits(benchmark):
    def create_state():
        state = oqubit.StateVector(
            [
                oqubit.Qubit.zero()
                for _ in range(8)
            ]
        )
        return state

    benchmark(create_state)