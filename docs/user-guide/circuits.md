# Circuits

A quantum circuit is a sequence of quantum operations applied to a collection of qubits.

In OQubit, the `Circuit` class provides the main abstraction for representing quantum circuits, while `Instruction` represents an operation within a circuit.

## Importing Circuit

```python
from oqubit.circuit.circuit import Circuit
```

The instruction abstraction is available through:

```python
from oqubit.circuit.instruction import Instruction
```

## Creating a Circuit

Create a circuit by specifying the number of qubits:

```python
circuit = Circuit(2)
```

The argument must be an integer representing the number of qubits in the circuit.

For example:

```python
circuit = Circuit(3)
```

creates a circuit containing three qubits.

## Circuit Structure

A circuit can be thought of as a sequence of instructions:

```text
Circuit
│
├── Instruction
│     └── Gate
│
├── Instruction
│     └── Gate
│
└── Instruction
      └── Gate
```

Each instruction describes an operation and the qubits on which that operation acts.

## Instructions

OQubit provides the `Instruction` class for representing circuit operations.

```python
from oqubit.circuit.instruction import Instruction
```

An instruction connects a quantum operation with the qubits involved in that operation.

Conceptually:

```text
Instruction
├── Operation
├── Controls
└── Targets
```

The exact instruction fields and constructor behavior are defined by the installed OQubit version.

## Qubit Indices

Circuit qubits are identified using integer indices.

For a three-qubit circuit:

```python
circuit = Circuit(3)
```

the qubits can be referenced as:

```text
0
1
2
```

For example, an operation targeting the first qubit uses index `0`.

## Gates in Circuits

Quantum gates provide the operations that can be represented by circuit instructions.

OQubit separates these responsibilities:

```text
Circuit
   │
   ▼
Instruction
   │
   ▼
Gate
   │
   ▼
Quantum State
```

This allows the circuit representation to remain separate from the underlying statevector implementation.

## Controlled Operations

Controlled operations use control and target qubit indices.

For example, a controlled operation involving two qubits conceptually contains:

```text
Control ─────●────
             │
Target  ─────X────
```

The corresponding statevector operation uses:

```python
state.apply(
    gate,
    controls=[0],
    targets=[1]
)
```

Circuit instructions can represent the same relationship between control and target qubits.

## Multi-Qubit Operations

Operations involving multiple qubits specify multiple targets when supported by the operation.

For example:

```python
targets = [0, 1]
```

represents an operation acting on qubits `0` and `1`.

Controlled multi-qubit operations can additionally specify:

```python
controls = [0]
targets = [1, 2]
```

The number of controls and targets must be compatible with the operation being represented.

## Circuit and StateVector

`Circuit` and `StateVector` serve different purposes.

### Circuit

A `Circuit` describes **what operations should be performed**.

### StateVector

A `StateVector` represents **the current quantum state**.

Conceptually:

```text
Circuit
   │
   │ instructions
   ▼
Quantum Operations
   │
   ▼
StateVector
   │
   ▼
Measurement
```

This separation makes it possible to describe a quantum program independently from its simulated state.

## Example Circuit

A circuit can be created as follows:

```python
from oqubit.circuit.circuit import Circuit

circuit = Circuit(2)

print(circuit)
```

The circuit initially contains two qubits.

Operations can then be represented using OQubit's circuit instruction system and the gates provided by the `oqubit.gates` package.

## Circuit Validation

`Circuit` validates its input when it is created.

For example, the number of qubits must be an integer:

```python
Circuit(2)
```

is valid, while passing a non-integer value is rejected.

This prevents invalid circuit configurations from being created.

## Circuits in Quantum Algorithms

Quantum algorithms can be expressed as circuits composed of gates and instructions.

For example, algorithms such as:

* Deutsch
* Deutsch-Jozsa
* Bernstein-Vazirani
* Superdense Coding

use quantum circuits as part of their implementation.

See the [Algorithms](algorithms.md) guide for more information.

## Design

OQubit's circuit module is intentionally separated into two main components:

```text
oqubit/circuit/
├── circuit.py
└── instruction.py
```

`circuit.py` contains the `Circuit` abstraction.

`instruction.py` contains the `Instruction` abstraction used to describe operations within a circuit.

This modular structure keeps circuit construction separate from the lower-level quantum-state implementation.

## Summary

The OQubit circuit system provides:

* `Circuit` for representing quantum circuits.
* `Instruction` for representing operations within circuits.
* Integer qubit indices for identifying qubits.
* Support for operations involving targets and controls.
* Separation between circuit representation and statevector simulation.

For the underlying quantum-state representation, see [StateVectors](statevectors.md).