import numpy as np
from ..core.operators import Operator,Gate
"""
These are Qubit gates which require more than two contorls or targets to operate and change the state of an Qubit.

Qubit gates such as SWAP, ISWAP , SQRT_SWAP, CCX, CSWAP Gates are present.

I hope you will enjoy learning creating new logical interpretation by using various series of Quantum Gates to Encode and Decode Informations.
"""
SWAP = Gate([[1, 0, 0, 0],[0, 0, 1, 0],[0, 1, 0, 0],[0, 0, 0, 1],],"SWAP",num_qubits=2,num_targets=2,)
ISWAP = Gate([[1, 0, 0, 0],[0, 0, 1j, 0],[0, 1j, 0, 0],[0, 0, 0, 1],],"iSWAP",num_qubits=2,num_targets=2,)
SQRT_SWAP = Gate(0.5 * np.array([[2, 0, 0, 0],[0, 1 + 1j, 1 - 1j, 0],[0, 1 - 1j, 1 + 1j, 0],[0, 0, 0, 2],]),"SQRT_SWAP",num_qubits=2,num_targets=2,)
CCX = Gate([[1, 0, 0, 0, 0, 0, 0, 0],[0, 1, 0, 0, 0, 0, 0, 0],[0, 0, 1, 0, 0, 0, 0, 0],[0, 0, 0, 1, 0, 0, 0, 0],[0, 0, 0, 0, 1, 0, 0, 0],[0, 0, 0, 0, 0, 1, 0, 0],[0, 0, 0, 0, 0, 0, 0, 1],[0, 0, 0, 0, 0, 0, 1, 0],],"CCX",num_qubits=3,num_controls=2,num_targets=1,)
CSWAP = Gate([[1, 0, 0, 0, 0, 0, 0, 0],[0, 1, 0, 0, 0, 0, 0, 0],[0, 0, 1, 0, 0, 0, 0, 0],[0, 0, 0, 1, 0, 0, 0, 0],[0, 0, 0, 0, 1, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 1],[0, 0, 0, 0, 0, 1, 0, 0],[0, 0, 0, 0, 0, 0, 0, 1],],"CSWAP",num_qubits=3,num_controls=1,num_targets=2,)
__all__ = ["SWAP","ISWAP","SQRT_SWAP","CCX","CSWAP"]