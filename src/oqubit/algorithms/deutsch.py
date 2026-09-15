from __future__ import annotations
from collections.abc import Callable
from typing import Literal
from ..circuit import Circuit
__all__ = ["deutsch"]
DeutschResult = Literal["constant", "balanced"]
def _validate_function(function: Callable[[int], int],) -> tuple[int, int]:
    if not callable(function):
        raise TypeError("function must be callable.")
    f0 = function(0)
    f1 = function(1)
    if f0 not in (0, 1) or f1 not in (0, 1):
        raise ValueError("function must return either 0 or 1.")
    return f0, f1
def _apply_oracle(circuit: Circuit,f0: int,f1: int,) -> None:
    if f0 == 0 and f1 == 0:
        return
    if f0 == 1 and f1 == 1:
        circuit.x(1)
        return
    if f0 == 0 and f1 == 1:
        circuit.cx(0, 1)
        return
    circuit.x(1)
    circuit.cx(0, 1)
    circuit.x(1)
def deutsch(function: Callable[[int], int],) -> DeutschResult:
    f0, f1 = _validate_function(function)
    circuit = Circuit(2)
    circuit.x(1)
    circuit.h(0)
    circuit.h(1)
    _apply_oracle(circuit, f0, f1)
    circuit.h(0)
    state = circuit.run()
    result = circuit.measure(state=state,qubits=0,)
    return "constant" if result == 0 else "balanced"