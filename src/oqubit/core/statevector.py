import numpy as np
from .qubit import Qubit
from .operators import Gate
class StateVector:
    """
    Represents the quantum state of an n-qubit system.

    A state vector is a complex vector containing the probability
    amplitudes of all computational basis states.

    For example, a two-qubit state can be written as:

        |ψ⟩ = α|00⟩ + β|01⟩ + γ|10⟩ + δ|11⟩

    The amplitudes satisfy:

        |α|² + |β|² + |γ|² + |δ|² = 1

    for a normalized state.

    Qubit ordering follows the order supplied to StateVector:

        StateVector([q0, q1, q2])

    corresponds to:

        |q0 q1 q2⟩
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
    def apply(self, gate, controls=None, targets=None):
        if not isinstance(gate, Gate):
            raise TypeError("gate must be a Gate object.")
        if gate.num_qubits > self.num_qubits:
            raise ValueError(
                f"{gate.name} requires {gate.num_qubits} qubits, "
                f"but the state contains only "
                f"{self.num_qubits} qubits."
            )
        if controls is None:
            controls = []
        elif isinstance(controls, int):
            controls = [controls]
        else:
            controls = list(controls)
        if targets is None:
            targets = []
        elif isinstance(targets, int):
            targets = [targets]
        else:
            targets = list(targets)
        if len(controls) != gate.num_controls:
            raise ValueError(f"{gate.name} requires "f"{gate.num_controls} control qubits, "f"but {len(controls)} were provided.")
        if len(targets) != gate.num_targets:
            raise ValueError(f"{gate.name} requires "f"{gate.num_targets} target qubits, "f"but {len(targets)} were provided.")
        qubits = controls + targets
        if len(qubits) != gate.num_qubits:
            raise ValueError(f"{gate.name} requires "f"{gate.num_qubits} qubits.")
        for index in qubits:
            if not isinstance(index, int):
                raise TypeError("Qubit indices must be integers.")
            if index < 0 or index >= self.num_qubits:
                raise IndexError(f"Qubit index {index} is out of range.")
        if len(set(qubits)) != len(qubits):
            raise ValueError("A qubit cannot be used more than once in the same gate.")
        if gate.num_qubits == 1:
            self._apply_single_qubit_gate(gate,targets[0])
            return self
        self._apply_multi_qubit_gate(gate,qubits)
        return self
    def _apply_single_qubit_gate(self, gate, target):
        matrix = gate.matrix
        step = 2 ** (self.num_qubits - target - 1)
        block = step * 2
        old_state = self._state.copy()
        for start in range(0,len(old_state),block):
            for offset in range(step):
                i0 = start + offset
                i1 = i0 + step
                a = old_state[i0]
                b = old_state[i1]
                self._state[i0] = (matrix[0, 0] * a+ matrix[0, 1] * b)
                self._state[i1] = (matrix[1, 0] * a+ matrix[1, 1] * b)
    def _apply_multi_qubit_gate(self, gate, qubits):
        n = self.num_qubits
        k = gate.num_qubits
        matrix = gate.matrix
        old_state = self._state.copy()
        new_state = np.zeros_like(old_state)
        bit_positions = [n - qubit - 1
            for qubit in qubits
        ]
        untouched_positions = [position
            for position in range(n)
            if position not in bit_positions
        ]
        for base in range(2 ** len(untouched_positions)):
            base_index = 0
            for i, position in enumerate(untouched_positions):
                bit = (base >> i) & 1
                base_index |= (bit << position)
            indices = []
            for local_index in range(2 ** k):
                index = base_index
                for j, position in enumerate(bit_positions):
                    bit = (local_index>> (k - j - 1)) & 1
                    index |= (bit << position)
                indices.append(index)
            amplitudes = old_state[indices]
            transformed = (matrix @ amplitudes)
            for i, index in enumerate(indices):
                new_state[index] = (transformed[i])
        self._state = new_state
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
        self._state = (self._state / norm)
        return self
    @property
    def notation(self):
        terms = []
        for index, amplitude in enumerate(self._state):
            if np.isclose(amplitude,0):
                continue
            basis = format(index,f"0{self.num_qubits}b")
            terms.append(f"{amplitude}|{basis}⟩")
        return " + ".join(terms)
    def __repr__(self):
        return (f"StateVector("f"num_qubits={self.num_qubits}, "f"dimension={self.dimension})")
__all__ = ["StateVector"]