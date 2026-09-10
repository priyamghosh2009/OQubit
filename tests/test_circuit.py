import numpy as np
import pytest

import oqubit


def test_circuit_creation():
    circuit = oqubit.Circuit(3)

    assert circuit.num_qubits == 3
    assert len(circuit) == 0
    assert circuit.size == 0
    assert circuit.depth == 0


def test_circuit_requires_positive_qubit_count():
    with pytest.raises(
        (ValueError, TypeError)
    ):
        oqubit.Circuit(0)


def test_circuit_rejects_negative_qubit_count():
    with pytest.raises(
        (ValueError, TypeError)
    ):
        oqubit.Circuit(-1)


def test_circuit_adds_instruction():
    circuit = oqubit.Circuit(1)

    circuit.h(0)

    assert len(circuit) == 1
    assert circuit.size == 1
    assert circuit.depth == 1


def test_circuit_method_chaining():
    circuit = oqubit.Circuit(2)

    result = (
        circuit
        .h(0)
        .cx(0, 1)
    )

    assert result is circuit
    assert len(circuit) == 2


def test_circuit_instruction_properties():
    circuit = oqubit.Circuit(2)

    circuit.cx(0, 1)

    instruction = circuit.instructions[0]

    assert instruction.gate is oqubit.CX
    assert instruction.controls == [0]
    assert instruction.targets == [1]
    assert instruction.qubits == [0, 1]


def test_bell_circuit():
    circuit = oqubit.Circuit(2)

    circuit.h(0)
    circuit.cx(0, 1)

    state = circuit.run()

    expected = np.array(
        [
            1 / np.sqrt(2),
            0,
            0,
            1 / np.sqrt(2),
        ],
        dtype=complex,
    )

    assert np.allclose(
        state.state,
        expected,
    )


def test_circuit_run_returns_statevector():
    circuit = oqubit.Circuit(2)

    state = circuit.run()

    assert isinstance(
        state,
        oqubit.StateVector,
    )

    assert state.num_qubits == 2


def test_circuit_initial_state_is_zero():
    circuit = oqubit.Circuit(3)

    state = circuit.run()

    assert np.isclose(
        state.state[0],
        1,
    )

    assert (
        np.count_nonzero(
            np.abs(state.state) > 1e-12
        )
        == 1
    )


def test_circuit_x():
    circuit = oqubit.Circuit(1)

    circuit.x(0)

    state = circuit.run()

    assert np.allclose(
        state.state,
        [0, 1],
    )


def test_circuit_h():
    circuit = oqubit.Circuit(1)

    circuit.h(0)

    state = circuit.run()

    expected = np.array(
        [
            1 / np.sqrt(2),
            1 / np.sqrt(2),
        ],
        dtype=complex,
    )

    assert np.allclose(
        state.state,
        expected,
    )


def test_circuit_measure():
    circuit = oqubit.Circuit(1)

    circuit.x(0)

    result = circuit.measure()

    assert result == 1


def test_circuit_sample():
    circuit = oqubit.Circuit(1)

    circuit.x(0)

    counts = circuit.sample(
        shots=100,
    )

    assert counts == {
        "1": 100
    }


def test_circuit_clear():
    circuit = oqubit.Circuit(2)

    circuit.h(0)
    circuit.cx(0, 1)

    circuit.clear()

    assert len(circuit) == 0
    assert circuit.size == 0


def test_circuit_invalid_qubit():
    circuit = oqubit.Circuit(2)

    with pytest.raises(IndexError):
        circuit.h(2)


def test_circuit_negative_qubit():
    circuit = oqubit.Circuit(2)

    with pytest.raises(IndexError):
        circuit.h(-1)


def test_circuit_state_qubit_count_mismatch():
    circuit = oqubit.Circuit(2)

    state = oqubit.StateVector(
        [
            oqubit.Qubit.zero(),
        ]
    )

    with pytest.raises(ValueError):
        circuit.run(state)


def test_circuit_custom_initial_state():
    circuit = oqubit.Circuit(1)

    initial = oqubit.StateVector(
        [
            oqubit.Qubit.one(),
        ]
    )

    state = circuit.run(initial)

    assert np.allclose(
        state.state,
        [0, 1],
    )