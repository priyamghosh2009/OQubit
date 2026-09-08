from ..core.operators import Gate,Operators
import numpy as np
"""
These are Qubit gates which are cotrolled and requires atleast one Qubit control state to change the state of the other Qubit.

Qubit gates such as CX (also known as CNOT), CY ,CZ , CH, CS, CT, CSX Gates are present.

I hope you will enjoy learning creating new logical interpretation by using various series of Quantum Gates to Encode and Decode Informations.
"""
CX = Gate([[1, 0, 0, 0],[0, 1, 0, 0],[0, 0, 0, 1],[0, 0, 1, 0],],"CX",num_qubits=2,num_controls=1,num_targets=1,)
CY = Gate([[1, 0, 0, 0],[0, 1, 0, 0],[0, 0, 0, -1j],[0, 0, 1j, 0],],"CY",num_qubits=2,num_controls=1,num_targets=1,)
CZ = Gate([[1, 0, 0, 0],[0, 1, 0, 0],[0, 0, 1, 0],[0, 0, 0, -1],],"CZ",num_qubits=2,num_controls=1,num_targets=1,)
CH = Gate([[1, 0, 0, 0],[0, 1, 0, 0],[0, 0, 1 / np.sqrt(2), 1 / np.sqrt(2)],[0, 0, 1 / np.sqrt(2), -1 / np.sqrt(2)],],"CH",num_qubits=2,num_controls=1,num_targets=1,)
CS = Gate([[1, 0, 0, 0],[0, 1, 0, 0],[0, 0, 1, 0],[0, 0, 0, 1j],],"CS",num_qubits=2,num_controls=1,num_targets=1,)
CT = Gate([[1, 0, 0, 0],[0, 1, 0, 0],[0, 0, 1, 0],[0, 0, 0, np.exp(1j * np.pi / 4)],],"CT",num_qubits=2,num_controls=1,num_targets=1,)
CSX = Gate([[1, 0, 0, 0],[0, 1, 0, 0],[0, 0, (1 + 1j) / 2, (1 - 1j) / 2],[0, 0, (1 - 1j) / 2, (1 + 1j) / 2],],"CSX",num_qubits=2,num_controls=1,num_targets=1,)
__all__ = ["CX","CY","CZ","CH","CS","CT","CSX"]