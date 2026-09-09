import numpy as np
from ..core.statevector import StateVector
def measure(statevector, qubits=None):
    """
    Measure one or more qubits of a StateVector.

    Measurement is performed in the computational basis.

    Parameters
    ----------
    statevector : StateVector
        Quantum state to measure.

    qubits : int or iterable of int, optional
        Qubit index or indices to measure.

        If None, all qubits are measured.

    Returns
    -------
    int or tuple[int, ...]
        Measurement result.

        A single measured qubit returns an integer:

            0 or 1

        Multiple measured qubits return a tuple:

            (0, 1, ...)
    """

    if not isinstance(statevector, StateVector):
        raise TypeError("statevector must be a StateVector object.")
    qubits = _validate_qubits(statevector,qubits)
    probabilities = _measurement_probabilities(statevector,qubits)
    outcomes = list(probabilities.keys())
    weights = list(probabilities.values())
    selected_index = np.random.choice(len(outcomes),p=weights)
    outcome = outcomes[selected_index]
    _collapse(statevector,qubits,outcome)
    if len(outcome) == 1:
        return outcome[0]
    return tuple(outcome)
def _validate_qubits(statevector, qubits):
    if qubits is None:
        qubits = list(range(statevector.num_qubits))
    elif isinstance(qubits, int):
        qubits = [qubits]
    else:
        qubits = list(qubits)
    if not qubits:
        raise ValueError("At least one qubit must be measured.")
    for qubit in qubits:
        if not isinstance(qubit, int):
            raise TypeError("Qubit indices must be integers.")
        if qubit < 0 or qubit >= statevector.num_qubits:
            raise IndexError(f"Qubit index {qubit} is out of range.")
    if len(set(qubits)) != len(qubits):
        raise ValueError("A qubit cannot be measured more than once.")
    return qubits
def _measurement_probabilities(statevector,qubits):
    n = statevector.num_qubits
    num_measured = len(qubits)
    probabilities = {}
    num_outcomes = 2 ** num_measured
    for outcome_index in range(
        num_outcomes):
        outcome = tuple(
            (outcome_index>> (num_measured - i - 1)) & 1
            for i in range(num_measured))
        probability = 0.0
        for state_index, amplitude in enumerate(statevector.state):
            matches = True
            for qubit, bit in zip(qubits,outcome):
                bit_position = (n - qubit - 1)
                state_bit = (state_index>> bit_position) & 1
                if state_bit != bit:
                    matches = False
                    break
            if matches:
                probability += (abs(amplitude) ** 2)
        probabilities[outcome] = probability
    total = sum(probabilities.values())
    if np.isclose(total, 0):
        raise ValueError("Cannot measure a zero state.")
    probabilities = {
        outcome: probability / total
        for outcome, probability
        in probabilities.items()}
    return probabilities
def _collapse(
    statevector,
    qubits,outcome):
    n = statevector.num_qubits
    probability = 0.0
    for state_index, amplitude in enumerate(statevector.state):
        matches = True
        for qubit, bit in zip(qubits,outcome):
            bit_position = (n - qubit - 1)
            state_bit = (state_index>> bit_position) & 1
            if state_bit != bit:
                matches = False
                break
        if matches:
            probability += (abs(amplitude) ** 2)
    if np.isclose(probability, 0):
        raise ValueError("Cannot collapse onto a zero-probability outcome.")
    new_state = np.zeros_like(statevector.state)
    for state_index, amplitude in enumerate(statevector.state):
        matches = True
        for qubit, bit in zip(qubits,outcome):
            bit_position = (n - qubit - 1)
            state_bit = (state_index>> bit_position) & 1
            if state_bit != bit:
                matches = False
                break
        if matches:
            new_state[state_index] = amplitude
    norm = np.linalg.norm(new_state)
    if np.isclose(norm, 0):
        raise ValueError("Measurement produced a zero state.")
    statevector._state = (new_state / norm)
__all__ = ["measure"]