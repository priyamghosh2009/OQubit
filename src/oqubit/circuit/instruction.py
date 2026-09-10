from ..core.operators import Gate
class Instruction:
    """
    Represents a single gate operation in a quantum circuit.

    Parameters
    ----------
    gate : Gate
        Gate to apply.
    controls : int | list[int] | None
        Control qubit index or indices.
    targets : int | list[int] | None
        Target qubit index or indices.
    """

    def __init__(self, gate, controls=None, targets=None):
        if not isinstance(gate, Gate):
            raise TypeError("gate must be a Gate object.")

        self.gate = gate
        self.controls = self._normalize_qubits(controls)
        self.targets = self._normalize_qubits(targets)

        if len(self.controls) != gate.num_controls:
            raise ValueError(
                f"{gate.name} requires {gate.num_controls} control qubit(s), "
                f"got {len(self.controls)}."
            )

        if len(self.targets) != gate.num_targets:
            raise ValueError(
                f"{gate.name} requires {gate.num_targets} target qubit(s), "
                f"got {len(self.targets)}."
            )

        qubits = self.controls + self.targets

        if len(set(qubits)) != len(qubits):
            raise ValueError(
                "A qubit cannot be used more than once in the same instruction."
            )

    @staticmethod
    def _normalize_qubits(qubits):
        if qubits is None:
            return []

        if isinstance(qubits, int):
            return [qubits]

        return list(qubits)

    @property
    def qubits(self):
        return self.controls + self.targets

    def __repr__(self):
        return (
            f"Instruction("
            f"gate={self.gate.name!r}, "
            f"controls={self.controls}, "
            f"targets={self.targets})"
        )
__all__ = ["Instruction"]