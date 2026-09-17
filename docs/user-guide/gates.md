# Gates

Quantum gates are mathematical operations that transform quantum states.

In OQubit, gates are represented as operators and can be applied to `StateVector` objects to evolve a quantum system.

## Importing Gate

The base `Gate` abstraction is provided by OQubit:

```python
from oqubit.core.operators import Gate
```

Gate implementations are organized under the `oqubit.gates` package.

```text
oqubit/
└── gates/
    ├── single.py
    ├── controlled.py
    └── multi.py
```

## Single-Qubit Gates

Single-qubit gates operate on one target qubit.

A single-qubit gate can be applied to a `StateVector` by specifying the target:

```python
state.apply(
    gate,
    targets=[0]
)
```

For example, if `state` contains multiple qubits, `targets=[0]` applies the operation to the first qubit.

The available single-qubit gates are defined in:

```text
oqubit.gates.single
```

## Controlled Gates

Controlled gates operate conditionally based on one or more control qubits.

A controlled operation can be applied by specifying both controls and targets:

```python
state.apply(
    gate,
    controls=[0],
    targets=[1]
)
```

In this example:

* `0` is the control qubit.
* `1` is the target qubit.

Controlled-gate implementations are located in:

```text
oqubit.gates.controlled
```

## Multi-Qubit Gates

Multi-qubit gates operate on multiple target qubits.

They are provided through:

```text
oqubit.gates.multi
```

When applying a multi-qubit operation, provide the required target qubits:

```python
state.apply(
    gate,
    targets=[0, 1]
)
```

The number of target qubits must match the dimensions required by the gate.

## Applying a Gate

The primary interface for applying a gate to a quantum state is `StateVector.apply()`.

The general form is:

```python
state.apply(
    gate,
    controls=[...],
    targets=[...]
)
```

For operations without control qubits, only `targets` are required:

```python
state.apply(
    gate,
    targets=[0]
)
```

For controlled operations:

```python
state.apply(
    gate,
    controls=[0],
    targets=[1]
)
```

The `controls` argument is used when the operation requires control qubits.

## Gate Operators

Internally, a quantum gate can be represented by a matrix operator.

For a single-qubit gate:

$$
U =
\begin{bmatrix}
u_{00} & u_{01} \\
u_{10} & u_{11}
\end{bmatrix}
$$

Applying the gate to a qubit state is expressed as:

$$
|\psi'\rangle = U|\psi\rangle
$$

For multi-qubit systems, OQubit expands the operation to act on the appropriate dimensions of the complete statevector.

## Gate Targets

Target indices identify the qubits affected by an operation.

For example:

```python
state.apply(
    gate,
    targets=[1]
)
```

applies the gate to qubit `1`.

For two targets:

```python
state.apply(
    gate,
    targets=[0, 1]
)
```

the operation acts on both qubits.

The target count must be compatible with the gate being applied.

## Gate Controls

Control indices identify qubits that conditionally control an operation.

For example:

```python
state.apply(
    gate,
    controls=[0],
    targets=[1]
)
```

represents an operation controlled by qubit `0` and applied to qubit `1`.

Multiple controls can be represented when supported by the gate:

```python
state.apply(
    gate,
    controls=[0, 1],
    targets=[2]
)
```

## Gate Organization

OQubit separates gates according to their scope:

```text
oqubit.gates
│
├── single.py
│   └── Single-qubit gates
│
├── controlled.py
│   └── Controlled gates
│
└── multi.py
    └── Multi-qubit gates
```

This keeps the gate implementations separate from the core statevector and circuit logic.

## Gates and Circuits

Gates can also be used as operations within quantum circuits.

A circuit describes a sequence of operations, while the statevector represents the quantum state produced by those operations.

Conceptually:

```text
Circuit
   │
   ▼
Instructions
   │
   ▼
Gates
   │
   ▼
StateVector
```

See [Circuits](circuits.md) for more information.

## Example

A statevector can be created and then transformed by applying a gate:

```python
from oqubit.core.qubit import Qubit
from oqubit.core.statevector import StateVector

state = StateVector([
    Qubit.zero(),
    Qubit.zero()
])

state.apply(
    gate,
    targets=[0]
)

print(state)
print(state.notation)
```

Replace `gate` with a gate provided by the OQubit gates package.

## Gate Validation

OQubit validates the relationship between an operation and the supplied qubit indices.

For example, an operation requiring a particular number of targets should not be applied with an incompatible number of target qubits.

This helps detect invalid circuit or statevector operations early.

## Summary

OQubit's gate system is organized around three main categories:

* **Single-qubit gates** — operations acting on one target.
* **Controlled gates** — operations using control and target qubits.
* **Multi-qubit gates** — operations acting on multiple qubits.

The main state-evolution interface is:

```python
state.apply(
    gate,
    controls=[...],
    targets=[...]
)
```

This design separates quantum gates from the `StateVector` representation while allowing gates to be composed into larger quantum circuits.
