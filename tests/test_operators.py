import numpy as np
import pytest

from oqubit import Operator, Gate


def test_operator_creation():
    matrix = np.eye(
        2,
        dtype=complex,
    )

    operator = Operator(matrix)

    assert np.allclose(
        operator.matrix,
        matrix,
    )


def test_operator_matrix_is_numpy_array():
    operator = Operator(
        np.eye(2)
    )

    assert isinstance(
        operator.matrix,
        np.ndarray,
    )


def test_operator_matrix_is_complex():
    operator = Operator(
        np.eye(2)
    )

    assert operator.matrix.dtype == complex


def test_gate_is_operator():
    gate = Gate(
        np.eye(2, dtype=complex),
        num_qubits=1,
    num_controls=0,
    num_targets=1,
        name="I",
    )

    assert isinstance(
        gate,
        Operator,
    )

    assert isinstance(
        gate,
        Gate,
    )


def test_gate_name():
    gate = Gate(
        np.eye(2, dtype=complex),
        num_qubits=1,
    num_controls=0,
    num_targets=1,
        name="I",
    )

    assert gate.name == "I"


def test_single_qubit_gate_properties():
    gate = Gate(
        np.eye(2, dtype=complex),
        num_qubits=1,
    num_controls=0,
    num_targets=1,
        name="I",
    )

    assert gate.num_qubits == 1
    assert gate.num_controls == 0
    assert gate.num_targets == 1


def test_gate_matrix_shape():
    gate = Gate(
        np.eye(2, dtype=complex),
       num_qubits=1,
    num_controls=0,
    num_targets=1,
        name="I",
    )

    assert gate.matrix.shape == (2, 2)


def test_operator_rejects_non_square_matrix():
    with pytest.raises(
        (ValueError, TypeError)
    ):
        Operator(
            np.ones((2, 3))
        )


def test_gate_rejects_non_square_matrix():
    with pytest.raises(
        (ValueError, TypeError)
    ):
        Gate(
            np.ones((2, 3)),
            name="bad",
        )