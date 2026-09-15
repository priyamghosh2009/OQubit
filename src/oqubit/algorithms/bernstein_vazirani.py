"""
Bernstein–Vazirani algorithm.

This module implements the Bernstein–Vazirani algorithm for recovering
a hidden binary string ``s`` from a Boolean function of the form

    f(x) = s · x (mod 2)

where ``s`` and ``x`` are binary strings of equal length.

The algorithm determines the complete hidden string using a single
quantum-oracle evaluation.

Notes
-----
The implementation constructs the oracle from elementary X and
controlled-X gates. The oracle therefore represents the transformation

    U_f |x>|y> = |x>|y XOR f(x)>.

The first ``n`` qubits form the input register and the final qubit
is the oracle ancilla.

For a secret string

    s = s_0 s_1 ... s_(n-1),

the oracle applies a controlled-X gate from input qubit ``i`` to the
ancilla whenever ``s_i == 1``.
"""
from __future__ import annotations
from typing import Final
from ..circuit import Circuit
__all__ = ["bernstein_vazirani"]
def _validate_secret(secret: str) -> None:
    if not isinstance(secret, str):
        raise TypeError("secret must be a string.")
    if not secret:
        raise ValueError("secret must not be empty.")
    if any(bit not in "01" for bit in secret):
        raise ValueError("secret must contain only binary digits '0' and '1'.")
def _apply_oracle(circuit: Circuit,secret: str,) -> None:
    ancilla = len(secret)
    for qubit, bit in enumerate(secret):
        if bit == "1":
            circuit.cx(qubit, ancilla)
def bernstein_vazirani(secret: str) -> str:
    _validate_secret(secret)
    num_qubits = len(secret)
    ancilla = num_qubits
    circuit = Circuit(num_qubits + 1)
    circuit.x(ancilla)
    for qubit in range(num_qubits + 1):
        circuit.h(qubit)
    _apply_oracle(circuit,secret,)
    for qubit in range(num_qubits):
        circuit.h(qubit)
    state = circuit.run()
    result = circuit.measure(state=state,qubits=tuple(range(num_qubits)),)
    return "".join(str(bit) for bit in result)