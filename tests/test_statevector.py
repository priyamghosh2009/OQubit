import numpy as np
import pytest

from oqubit import Qubit, StateVector, X, H, CX


def test_statevector_requires_at_least_one_qubit():
    with pytest.raises(ValueError):
        StateVector([])


def test_statevector_requires_qubit_objects():
    with pytest.raises(TypeError):
        StateVector([Qubit.zero(), 0])


def test_two_qubit_tensor_product():
    state = StateVector(
        [
            Qubit.zero(),
            Qubit.one(),
        ]
    )

    expected = np.array(
        [0, 1, 0, 0],
        dtype=complex,
    )

    assert np.allclose(state.state, expected)


def test_three_qubit_tensor_product():
    state = StateVector(
        [
            Qubit.zero(),
            Qubit.one(),
            Qubit.zero(),
        ]
    )

    expected = np.zeros(8, dtype=complex)
    expected[2] = 1

    assert np.allclose(state.state, expected)


def test_num_qubits():
    state = StateVector(
        [
            Qubit.zero(),
            Qubit.zero(),
            Qubit.zero(),
        ]
    )

    assert state.num_qubits == 3


def test_dimension():
    state = StateVector(
        [
            Qubit.zero(),
            Qubit.zero(),
            Qubit.zero(),
        ]
    )

    assert state.dimension == 8


def test_notation():
    state = StateVector(
        [
            Qubit.zero(),
            Qubit.one(),
        ]
    )

    assert "|01⟩" in state.notation


def test_single_qubit_gate_on_first_qubit():
    state = StateVector(
        [
            Qubit.zero(),
            Qubit.zero(),
        ]
    )

    state.apply(X, targets=0)

    assert np.allclose(
        state.state,
        [0, 0, 1, 0],
    )


def test_single_qubit_gate_on_second_qubit():
    state = StateVector(
        [
            Qubit.zero(),
            Qubit.zero(),
        ]
    )

    state.apply(X, targets=1)

    assert np.allclose(
        state.state,
        [0, 1, 0, 0],
    )


def test_hadamard_creates_superposition():
    state = StateVector(
        [
            Qubit.zero(),
        ]
    )

    state.apply(H, targets=0)

    expected = np.array(
        [
            1 / np.sqrt(2),
            1 / np.sqrt(2),
        ],
        dtype=complex,
    )

    assert np.allclose(state.state, expected)


def test_bell_state():
    state = StateVector(
        [
            Qubit.zero(),
            Qubit.zero(),
        ]
    )

    state.apply(H, targets=0)
    state.apply(CX, controls=0, targets=1)

    expected = np.array(
        [
            1 / np.sqrt(2),
            0,
            0,
            1 / np.sqrt(2),
        ],
        dtype=complex,
    )

    assert np.allclose(state.state, expected)


def test_normalize():
    state = StateVector(
        [
            Qubit.zero(),
            Qubit.zero(),
        ]
    )

    state._state *= 5

    state.normalize()

    assert np.isclose(
        np.linalg.norm(state.state),
        1,
    )


def test_invalid_gate():
    state = StateVector(
        [
            Qubit.zero(),
        ]
    )

    with pytest.raises(TypeError):
        state.apply("X", targets=0)


def test_invalid_target():
    state = StateVector(
        [
            Qubit.zero(),
        ]
    )

    with pytest.raises(IndexError):
        state.apply(X, targets=1)


def test_negative_target():
    state = StateVector(
        [
            Qubit.zero(),
        ]
    )

    with pytest.raises(IndexError):
        state.apply(X, targets=-1)


def test_duplicate_qubits_rejected():
    state = StateVector(
        [
            Qubit.zero(),
            Qubit.zero(),
        ]
    )

    with pytest.raises(ValueError):
        state.apply(
            CX,
            controls=0,
            targets=0,
        )