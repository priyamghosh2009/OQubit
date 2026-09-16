"""
Superdense Coding algorithm.

Superdense coding transmits two classical bits using one qubit
and a previously shared entangled Bell pair.
"""
from ..circuit import Circuit
__all__ = ["encode", "decode"]
def encode(bit0, bit1):
    if bit0 not in (0, 1):
        raise ValueError("bit0 must be 0 or 1.")
    if bit1 not in (0, 1):
        raise ValueError("bit1 must be 0 or 1.")
    circuit = Circuit(2)
    circuit.h(0)
    circuit.cx(0, 1)
    if bit1:
        circuit.x(0)
    if bit0:
        circuit.z(0)
    return circuit
def decode(circuit):
    if not isinstance(circuit, Circuit):
        raise TypeError("circuit must be an OQubit Circuit.")
    circuit.cx(0, 1)
    circuit.h(0)
    state = circuit.run()
    return circuit.measure(state=state,qubits=(0, 1),)