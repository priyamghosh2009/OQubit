import numpy as np
import pytest

from oqubit import Qubit


def test_zero_state():
    q = Qubit.zero()

    assert np.allclose(q.state, [1, 0])
    assert np.isclose(q.prob_0, 1)
    assert np.isclose(q.prob_1, 0)


def test_one_state():
    q = Qubit.one()

    assert np.allclose(q.state, [0, 1])
    assert np.isclose(q.prob_0, 0)
    assert np.isclose(q.prob_1, 1)


@pytest.mark.parametrize(
    "factory",
    [
        Qubit.plus,
        Qubit.minus,
        Qubit.i,
        Qubit.minus_i,
    ],
)
def test_predefined_states_are_normalized(factory):
    q = factory()

    norm = abs(q.alpha) ** 2 + abs(q.beta) ** 2

    assert np.isclose(norm, 1)


def test_custom_state_without_normalization():
    q = Qubit(3, 4, normalize=False)

    assert q.alpha == 3
    assert q.beta == 4

    assert np.isclose(q.prob_0, 9 / 25)
    assert np.isclose(q.prob_1, 16 / 25)


def test_custom_state_with_normalization():
    q = Qubit(3, 4)

    norm = abs(q.alpha) ** 2 + abs(q.beta) ** 2

    assert np.isclose(norm, 1)


def test_state_property():
    q = Qubit.zero()

    assert isinstance(q.state, np.ndarray)
    assert q.state.dtype == complex
    assert np.allclose(q.state, [1, 0])


def test_probabilities_sum_to_one():
    q = Qubit(3, 4, normalize=False)

    assert np.isclose(q.prob_0 + q.prob_1, 1)


def test_zero_state_probability_error():
    q = Qubit(0, 0, normalize=False)

    with pytest.raises(ValueError):
        _ = q.prob_0

    with pytest.raises(ValueError):
        _ = q.prob_1


def test_apply_gate():
    import oqubit

    q = Qubit.zero()

    q.apply(oqubit.X)

    assert np.allclose(q.state, [0, 1])