import numpy as np

from .qubit import Qubit


class StateVector:
    """
    Represents the quantum state of an n-qubit system.
    """

    def __init__(self, qubits):
        self.qubits = list(qubits)

        if not self.qubits:
            raise ValueError("StateVector requires at least one qubit.")

        if not all(isinstance(q, Qubit) for q in self.qubits):
            raise TypeError("All elements must be Qubit objects.")

        self._state = self._build_state()

    def _build_state(self):
        state = self.qubits[0].state

        for qubit in self.qubits[1:]:
            state = np.kron(state, qubit.state)

        return state

    @property
    def state(self):
        return self._state

    @property
    def num_qubits(self):
        return len(self.qubits)

    @property
    def dimension(self):
        return 2 ** self.num_qubits

    def normalize(self):
        norm = np.linalg.norm(self._state)

        if np.isclose(norm, 0):
            raise ValueError("Cannot normalize zero state.")

        self._state = self._state / norm
    @property
    def notation(self):
        terms = []

        for index, amplitude in enumerate(self._state):
            if np.isclose(amplitude, 0):
                continue
            basis = format(index, f"0{self.num_qubits}b")
            terms.append(f"{amplitude}|{basis}⟩")

        return " + ".join(terms)
    def __repr__(self):
        return (
            f"StateVector("
            f"num_qubits={self.num_qubits}, "
            f"dimension={self.dimension})"
        )