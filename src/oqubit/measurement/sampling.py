import numpy as np
from ..core.statevector import StateVector
from .measurement import _validate_qubits, _measurement_probabilities
def sample(statevector,shots=1024,qubits=None):
    """
    Sample a quantum state repeatedly.

    Parameters
    ----------
    statevector : StateVector
        Quantum state to sample.

    shots : int, default=1024
        Number of measurement shots.

    qubits : int or iterable of int, optional
        Qubit index or indices to measure.

        If None, all qubits are measured.

    Returns
    -------
    dict[str, int]
        Dictionary containing measurement outcomes and
        their occurrence counts.
    """
    if not isinstance(statevector,StateVector):
        raise TypeError("statevector must be a StateVector object.")
    if not isinstance(shots,int):
        raise TypeError("shots must be an integer.")
    if shots < 1:
        raise ValueError("shots must be at least 1.")
    qubits = _validate_qubits(statevector,qubits)
    probabilities = _measurement_probabilities(statevector,qubits)
    outcomes = list(probabilities.keys())
    weights = np.array(list(probabilities.values()),dtype=float)
    samples = np.random.choice(len(outcomes),size=shots,p=weights)
    counts = {}
    for index in samples:
        outcome = outcomes[index]
        bitstring = "".join(
            str(bit)
            for bit in outcome)
        counts[bitstring] = (counts.get(bitstring, 0) + 1)
    return counts
__all__ = ["sample",]