import numpy as np
from ..core.operators import Gate
"""
These are Qubit gates which the Qubit to change the state of that Qubit. These Gates does not need any control Qubit logic to act on the Qubit rather performs a straight operation on the target Qubit.

Qubit gates such as X, Y, Z, H (also known as Hardamard), S , T, SX  Gates are present.

I hope you will enjoy learning creating new logical interpretation by using various series of Quantum Gates to Encode and Decode Informations.
"""
X = Gate([[0, 1],[1, 0]],"X",num_qubits=1,num_targets=1)
Y = Gate([[0, -1j],[1j, 0]],"Y",num_qubits=1,num_targets=1)
Z = Gate([[1, 0],[0, -1]],"Z",num_qubits=1,num_targets=1)
H = Gate((1 / np.sqrt(2)) * np.array([[1, 1],[1, -1]]),"H",num_qubits=1,num_targets=1)
S = Gate([[1, 0],[0, 1j]],"S",num_qubits=1,num_targets=1)
T = Gate([[1, 0],[0, np.exp(1j * np.pi / 4)]],"T",num_qubits=1,num_targets=1)
SX = Gate(0.5 * np.array([[1 + 1j, 1 - 1j],[1 - 1j, 1 + 1j]]),"SX",num_qubits=1,num_targets=1)
__all__=["X","Y","Z","H","S","T","SX"]