import oqubit


def test_x_gate_8_qubits(benchmark):
    state = oqubit.StateVector(
        [
            oqubit.Qubit.zero()
            for _ in range(8)
        ]
    )

    def apply_x():
        state.apply(
            oqubit.X,
            targets=0,
        )

    benchmark(apply_x)


def test_h_gate_8_qubits(benchmark):
    state = oqubit.StateVector(
        [
            oqubit.Qubit.zero()
            for _ in range(8)
        ]
    )

    def apply_h():
        state.apply(
            oqubit.H,
            targets=0,
        )

    benchmark(apply_h)


def test_cx_gate_8_qubits(benchmark):
    state = oqubit.StateVector(
        [
            oqubit.Qubit.zero()
            for _ in range(8)
        ]
    )

    def apply_cx():
        state.apply(
            oqubit.CX,
            controls=0,
            targets=1,
        )

    benchmark(apply_cx)