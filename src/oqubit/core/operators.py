"""
Core operator definitions for OQubit.

This module provides the base Operator class for linear operators
and the Gate class for quantum gates.
"""
import numpy as np
class Operator:
    """
    Represents a linear operator acting on a quantum state.

    Parameters
    ----------
    matrix : array-like
        Square matrix representing the operator.
    """

    def __init__(self, matrix):
        self.matrix = np.asarray(matrix, dtype=complex)
        if self.matrix.ndim != 2:
            raise ValueError("Operator matrix must be two-dimensional.")
        if self.matrix.shape[0] != self.matrix.shape[1]:
            raise ValueError("Operator matrix must be square.")
    @property
    def dimension(self):
        """Return the dimension of the operator."""
        return self.matrix.shape[0]
    def __matmul__(self, other):
        """Apply the operator using the @ operator."""
        return self.matrix @ other
    def __repr__(self):
        return (f"Operator("f"dimension={self.dimension})")
class Gate(Operator):
    """
    Represents a quantum gate.

    A Gate is a specialized Operator that also describes
    how many qubits it acts on and its control/target structure.

    Parameters
    ----------
    matrix : array-like
        Square matrix representing the quantum gate.

    name : str
        Name of the gate.

    num_qubits : int
        Number of qubits the gate acts on.

    num_controls : int, default=0
        Number of control qubits.

    num_targets : int, default=0
        Number of target qubits.
    """

    def __init__(self,matrix,name,num_qubits,num_controls=0,num_targets=0,):
        super().__init__(matrix)
        if not isinstance(name, str):
            raise TypeError("Gate name must be a string.")
        if not isinstance(num_qubits, int) or num_qubits < 1:
            raise ValueError("num_qubits must be a positive integer.")
        if not isinstance(num_controls, int) or num_controls < 0:
            raise ValueError("num_controls must be a non-negative integer.")
        if not isinstance(num_targets, int) or num_targets < 0:
            raise ValueError("num_targets must be a non-negative integer.")
        if num_controls + num_targets != num_qubits:
            raise ValueError("num_controls + num_targets must equal num_qubits.")
        expected_dimension = 2 ** num_qubits
        if self.dimension != expected_dimension:
            raise ValueError(f"{name} is a {num_qubits}-qubit gate, "f"so its matrix must be "f"{expected_dimension}x{expected_dimension}.")
        self.name = name
        self.num_qubits = num_qubits
        self.num_controls = num_controls
        self.num_targets = num_targets
    def __repr__(self):
        return (f"Gate("f"name='{self.name}', "f"num_qubits={self.num_qubits}, "f"num_controls={self.num_controls}, "f"num_targets={self.num_targets})")
__all__ = ["Operator","Gate",]