import numpy as np
import pytest

import oqubit


SINGLE_GATES = [
    oqubit.X,
    oqubit.Y,
    oqubit.Z,
    oqubit.H,
    oqubit.S,
    oqubit.T,
    oqubit.SX,
]

CONTROLLED_GATES = [
    oqubit.CX,
    oqubit.CY,
    oqubit.CZ,
    oqubit.CS,
    oqubit.CH,
    oqubit.CT,
    oqubit.CSX,
]

MULTI_GATES = [
    oqubit.SWAP,
    oqubit.ISWAP,
    oqubit.SQRT_SWAP,
    oqubit.CCX,
    oqubit.CSWAP,
]


# ============================================================
# Single-qubit gates
# ============================================================

@pytest.mark.parametrize("gate", SINGLE_GATES)
def test_single_qubit_gate_metadata(gate):
    assert gate.num_qubits == 1
    assert gate.num_controls == 0
    assert gate.num_targets == 1


# ============================================================
# Controlled gates
# ============================================================

@pytest.mark.parametrize("gate", CONTROLLED_GATES)
def test_controlled_gate_metadata(gate):
    assert gate.num_qubits == 2
    assert gate.num_controls == 1
    assert gate.num_targets == 1


# ============================================================
# Multi-qubit gates
# ============================================================

@pytest.mark.parametrize("gate", MULTI_GATES)
def test_multi_qubit_gate_metadata(gate):
    if gate is oqubit.CCX:
        assert gate.num_qubits == 3
        assert gate.num_controls == 2
        assert gate.num_targets == 1

    elif gate is oqubit.CSWAP:
        assert gate.num_qubits == 3
        assert gate.num_controls == 1
        assert gate.num_targets == 2

    else:
        assert gate.num_qubits == 2
        assert gate.num_controls == 0
        assert gate.num_targets == 2


# ============================================================
# Matrix properties
# ============================================================

@pytest.mark.parametrize(
    "gate",
    SINGLE_GATES + CONTROLLED_GATES + MULTI_GATES,
)
def test_gate_matrix_is_square(gate):
    rows, columns = gate.matrix.shape

    assert rows == columns


@pytest.mark.parametrize(
    "gate",
    SINGLE_GATES + CONTROLLED_GATES + MULTI_GATES,
)
def test_gate_matrix_is_unitary(gate):
    identity = np.eye(
        gate.matrix.shape[0],
        dtype=complex,
    )

    assert np.allclose(
        gate.matrix.conj().T @ gate.matrix,
        identity,
    )


# ============================================================
# X gate
# ============================================================

def test_x_gate_flips_zero():
    state = oqubit.StateVector(
        [
            oqubit.Qubit.zero(),
        ]
    )

    state.apply(
        oqubit.X,
        targets=0,
    )

    assert np.allclose(
        state.state,
        [0, 1],
    )


def test_x_gate_flips_one():
    state = oqubit.StateVector(
        [
            oqubit.Qubit.one(),
        ]
    )

    state.apply(
        oqubit.X,
        targets=0,
    )

    assert np.allclose(
        state.state,
        [1, 0],
    )


# ============================================================
# Hadamard gate
# ============================================================

def test_h_gate_creates_plus_state():
    state = oqubit.StateVector(
        [
            oqubit.Qubit.zero(),
        ]
    )

    state.apply(
        oqubit.H,
        targets=0,
    )

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


# ============================================================
# Controlled-X / CNOT
# ============================================================

def test_cx_does_not_flip_target_when_control_is_zero():
    state = oqubit.StateVector(
        [
            oqubit.Qubit.zero(),
            oqubit.Qubit.zero(),
        ]
    )

    state.apply(
        oqubit.CX,
        controls=0,
        targets=1,
    )

    # |00> remains |00>
    assert np.allclose(
        state.state,
        [1, 0, 0, 0],
    )


def test_cx_flips_target_when_control_is_one():
    state = oqubit.StateVector(
        [
            oqubit.Qubit.one(),
            oqubit.Qubit.zero(),
        ]
    )

    state.apply(
        oqubit.CX,
        controls=0,
        targets=1,
    )

    # MSB-first ordering:
    #
    # |10> -> |11>
    #
    # Basis ordering:
    # |00> -> index 0
    # |01> -> index 1
    # |10> -> index 2
    # |11> -> index 3

    assert np.allclose(
        state.state,
        [0, 0, 0, 1],
    )


# ============================================================
# SWAP
# ============================================================

def test_swap_exchanges_qubits():
    state = oqubit.StateVector(
        [
            oqubit.Qubit.one(),
            oqubit.Qubit.zero(),
        ]
    )

    state.apply(
        oqubit.SWAP,
        targets=[0, 1],
    )

    # |10> -> |01>
    assert np.allclose(
        state.state,
        [0, 1, 0, 0],
    )


# ============================================================
# CCX / Toffoli
# ============================================================

def test_ccx_flips_target_when_both_controls_are_one():
    state = oqubit.StateVector(
        [
            oqubit.Qubit.one(),
            oqubit.Qubit.one(),
            oqubit.Qubit.zero(),
        ]
    )

    state.apply(
        oqubit.CCX,
        controls=[0, 1],
        targets=2,
    )

    # |110> -> |111>
    assert np.allclose(
        state.state,
        [0, 0, 0, 0, 0, 0, 0, 1],
    )


def test_ccx_does_not_flip_target_when_control_is_zero():
    state = oqubit.StateVector(
        [
            oqubit.Qubit.one(),
            oqubit.Qubit.zero(),
            oqubit.Qubit.zero(),
        ]
    )

    state.apply(
        oqubit.CCX,
        controls=[0, 1],
        targets=2,
    )

    # |100> remains |100>
    assert np.allclose(
        state.state,
        [0, 0, 0, 0, 1, 0, 0, 0],
    )


# ============================================================
# CSWAP / Fredkin
# ============================================================

def test_cswap_does_not_swap_when_control_is_zero():
    state = oqubit.StateVector(
        [
            oqubit.Qubit.zero(),
            oqubit.Qubit.one(),
            oqubit.Qubit.zero(),
        ]
    )

    state.apply(
        oqubit.CSWAP,
        controls=0,
        targets=[1, 2],
    )

    # |010> remains |010>
    assert np.allclose(
        state.state,
        [0, 0, 1, 0, 0, 0, 0, 0],
    )


def test_cswap_swaps_targets_when_control_is_one():
    state = oqubit.StateVector(
        [
            oqubit.Qubit.one(),
            oqubit.Qubit.zero(),
            oqubit.Qubit.one(),
        ]
    )

    state.apply(
        oqubit.CSWAP,
        controls=0,
        targets=[1, 2],
    )

    # |101> -> |110>
    assert np.allclose(
        state.state,
        [0, 0, 0, 0, 0, 0, 1, 0],
    )