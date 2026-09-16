"""
Deutsch–Jozsa algorithm.

This module implements the Deutsch–Jozsa algorithm for Boolean
functions of the form

    f : {0, 1}^n -> {0, 1}

under the promise that ``f`` is either constant or balanced.

The algorithm determines whether the function is constant or
balanced using a single quantum-oracle evaluation.

Notes
-----
The implementation constructs the oracle from elementary X and
controlled-X gates. The oracle therefore represents the transformation

    U_f |x>|y> = |x>|y XOR f(x)>.

The first ``n`` qubits form the input register and the final qubit
is the oracle ancilla.
"""
from __future__ import annotations
from collections.abc import Callable, Iterable
from itertools import product
from typing import Literal
from ..circuit import Circuit
__all__ = ["deutsch_jozsa"]
DeutschJozsaResult = Literal["constant", "balanced"]
def _validate_num_qubits(num_qubits: int) -> None:
    if not isinstance(num_qubits, int):
        raise TypeError("num_qubits must be an integer.")
    if isinstance(num_qubits, bool):
        raise TypeError("num_qubits must be an integer.")
    if num_qubits < 1:
        raise ValueError("num_qubits must be at least 1.")
def _validate_function(function: Callable[[tuple[int, ...]], int],num_qubits: int,) -> dict[tuple[int, ...], int]:
    if not callable(function):
        raise TypeError("function must be callable.")
    truth_table: dict[tuple[int, ...], int] = {}
    for bits in product((0, 1), repeat=num_qubits):
        value = function(bits)
        if not isinstance(value, int) or isinstance(value, bool):
            raise TypeError("function must return an integer value of 0 or 1.")
        if value not in (0, 1):
            raise ValueError("function must return either 0 or 1.")
        truth_table[bits] = value
    return truth_table
def _classify_truth_table(truth_table: dict[tuple[int, ...], int],) -> DeutschJozsaResult:
    values = tuple(truth_table.values())
    total = len(values)
    ones = sum(values)
    if ones == 0 or ones == total:
        return "constant"
    if ones * 2 == total:
        return "balanced"
    raise ValueError("function must be either constant or balanced.")
def _apply_oracle(circuit: Circuit,truth_table: dict[tuple[int, ...], int],num_qubits: int,) -> None:
    ancilla = num_qubits
    for bits, value in truth_table.items():
        if value == 0:
            continue
        if num_qubits == 1:
            if bits[0] == 1:
                circuit.cx(0, ancilla)
            else:
                circuit.x(0)
                circuit.cx(0, ancilla)
                circuit.x(0)
            continue
        if num_qubits == 2:
            _apply_two_controlled_x(
                circuit,
                bits,
                ancilla,
            )
            continue
        raise NotImplementedError(
            "Deutsch–Jozsa oracles with more than 2 input qubits "
            "require multi-controlled gates, which are not yet "
            "exposed by the current OQubit Circuit API."
        )
def _apply_two_controlled_x(circuit: Circuit,bits: tuple[int, ...],target: int,) -> None:
    control0 = 0
    control1 = 1
    zero_controls = [
        index
        for index, bit in enumerate(bits)
        if bit == 0
        ]
    for qubit in zero_controls:
        circuit.x(qubit)
    circuit.ccx(control0,control1,target,)
    for qubit in reversed(zero_controls):
        circuit.x(qubit)
def deutsch_jozsa(function: Callable[[tuple[int, ...]], int],num_qubits: int,) -> DeutschJozsaResult:
    _validate_num_qubits(num_qubits)
    truth_table = _validate_function(function,num_qubits,)
    _classify_truth_table(truth_table)
    circuit = Circuit(num_qubits + 1)
    ancilla = num_qubits
    circuit.x(ancilla)
    for qubit in range(num_qubits + 1):
        circuit.h(qubit)
    _apply_oracle(
        circuit,
        truth_table,
        num_qubits,
    )
    for qubit in range(num_qubits):
        circuit.h(qubit)
    state = circuit.run()
    result = circuit.measure(
        state=state,
        qubits=tuple(range(num_qubits)),
    )

    if result==0:
        return "constant"
    return "balanced"