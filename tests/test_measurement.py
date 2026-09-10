import numpy as np
import pytest

import oqubit


def test_measure_zero():
    state = oqubit.StateVector(
        [
            oqubit.Qubit.zero(),
        ]
    )

    result = oqubit.measure(state)

    assert result == 0


def test_measure_one():
    state = oqubit.StateVector(
        [
            oqubit.Qubit.one(),
        ]
    )

    result = oqubit.measure(state)

    assert result == 1


def test_measurement_collapses_state():
    state = oqubit.StateVector(
        [
            oqubit.Qubit.zero(),
            oqubit.Qubit.zero(),
        ]
    )

    state.apply(
        oqubit.H,
        targets=0,
    )

    state.apply(
        oqubit.CX,
        controls=0,
        targets=1,
    )

    result = oqubit.measure(state)

    assert result in [
        (0, 0),
        (1, 1),
    ]

    assert np.isclose(
        np.linalg.norm(state.state),
        1,
    )


def test_measurement_selected_qubit():
    state = oqubit.StateVector(
        [
            oqubit.Qubit.zero(),
            oqubit.Qubit.one(),
        ]
    )

    assert oqubit.measure(
        state,
        qubits=0,
    ) == 0

    state = oqubit.StateVector(
        [
            oqubit.Qubit.zero(),
            oqubit.Qubit.one(),
        ]
    )

    assert oqubit.measure(
        state,
        qubits=1,
    ) == 1


def test_sample_does_not_modify_state():
    state = oqubit.StateVector(
        [
            oqubit.Qubit.zero(),
        ]
    )

    before = state.state.copy()

    counts = oqubit.sample(
        state,
        shots=100,
    )

    assert np.allclose(
        state.state,
        before,
    )

    assert sum(
        counts.values()
    ) == 100


def test_sample_zero():
    state = oqubit.StateVector(
        [
            oqubit.Qubit.zero(),
        ]
    )

    counts = oqubit.sample(
        state,
        shots=100,
    )

    assert counts == {
        "0": 100
    }


def test_sample_one():
    state = oqubit.StateVector(
        [
            oqubit.Qubit.one(),
        ]
    )

    counts = oqubit.sample(
        state,
        shots=100,
    )

    assert counts == {
        "1": 100
    }


def test_bell_state_sampling():
    state = oqubit.StateVector(
        [
            oqubit.Qubit.zero(),
            oqubit.Qubit.zero(),
        ]
    )

    state.apply(
        oqubit.H,
        targets=0,
    )

    state.apply(
        oqubit.CX,
        controls=0,
        targets=1,
    )

    counts = oqubit.sample(
        state,
        shots=1000,
    )

    assert set(counts).issubset(
        {
            "00",
            "11",
        }
    )

    assert sum(
        counts.values()
    ) == 1000

    assert 400 < counts.get("00", 0) < 600
    assert 400 < counts.get("11", 0) < 600


def test_invalid_shots():
    state = oqubit.StateVector(
        [
            oqubit.Qubit.zero(),
        ]
    )

    with pytest.raises(
        (ValueError, TypeError)
    ):
        oqubit.sample(
            state,
            shots=0,
        )


def test_negative_shots():
    state = oqubit.StateVector(
        [
            oqubit.Qubit.zero(),
        ]
    )

    with pytest.raises(
        (ValueError, TypeError)
    ):
        oqubit.sample(
            state,
            shots=-10,
        )