# StateVectors

The `StateVector` class represents the quantum state of a multi-qubit system in OQubit.

A statevector contains the amplitudes of all computational-basis states of a quantum system.

For `n` qubits, a statevector contains:

$$
2^n
$$

complex amplitudes.

## Importing `StateVector`

```python
from oqubit.core.statevector import StateVector
```

You will commonly use it together with `Qubit`:

```python
from oqubit.core.qubit import Qubit
from oqubit.core.statevector import StateVector
```

## Creating a StateVector

A `StateVector` can be created from a list of `Qubit` objects:

```python
q0 = Qubit.zero()
q1 = Qubit.one()

state = StateVector([
    q0,
    q1
])
```

The resulting system represents:

$$
|0\rangle \otimes |1\rangle = |01\rangle
$$

OQubit combines the individual qubit states using the tensor product.

## Single-Qubit StateVector

A single qubit can also be placed into a `StateVector`:

```python
q = Qubit.zero()

state = StateVector([
    q
])
```

This represents:

$$
|0\rangle
$$

## Multi-Qubit Systems

For example, four qubits can be combined into a single statevector:

```python
state = StateVector([
    Qubit.zero(),
    Qubit.one(),
    Qubit.zero(),
    Qubit.one()
])
```

This represents:

$$
|0101\rangle
$$

The number of amplitudes in the resulting statevector is:

$$
2^4 = 16
$$

## Superposition States

Statevectors can contain qubits that are already in superposition.

```python
state = StateVector([
    Qubit.plus(),
    Qubit.zero()
])
```

The resulting state is:

$$
|+\rangle \otimes |0\rangle
$$

which expands to:

$$
\frac{1}{\sqrt{2}}|00\rangle +
\frac{1}{\sqrt{2}}|10\rangle
$$

The exact statevector is determined by the tensor product of the supplied qubit states.

## State Notation

OQubit provides a human-readable notation for statevectors.

```python
print(state.notation)
```

For a computational-basis state, the notation can be represented as:

```text
(1+0j)|01⟩
```

For a superposition, multiple basis states can be displayed with their corresponding amplitudes.

This representation is useful for inspecting and debugging quantum states.

## Applying Gates

Operations can be applied to a `StateVector` using `apply()`.

For a single-qubit operation, specify the target qubit:

```python
state.apply(
    gate,
    targets=[0]
)
```

The `targets` argument identifies which qubit or qubits the operation acts on.

### Controlled Operations

For controlled operations, specify both controls and targets:

```python
state.apply(
    gate,
    controls=[0],
    targets=[1]
)
```

Here, qubit `0` acts as the control and qubit `1` as the target.

The number of controls and targets must match the requirements of the supplied gate.

## Qubit Indexing

Qubits are identified by their indices in the `StateVector`.

For example:

```python
state = StateVector([
    Qubit.zero(),  # qubit 0
    Qubit.one(),   # qubit 1
    Qubit.zero(),  # qubit 2
])
```

The system contains three qubits:

```text
0 → |0⟩
1 → |1⟩
2 → |0⟩
```

An operation targeting the third qubit would use:

```python
targets=[2]
```

## Statevector Evolution

A statevector can be transformed by applying a sequence of operations.

Conceptually:

```text
Initial State
     │
     ▼
  Gate 1
     │
     ▼
  Gate 2
     │
     ▼
  Gate 3
     │
     ▼
Final State
```

For example:

```python
state.apply(
    gate_1,
    targets=[0]
)

state.apply(
    gate_2,
    controls=[0],
    targets=[1]
)
```

Each operation updates the simulated quantum state.

## Tensor Product

The tensor product is fundamental to OQubit's multi-qubit representation.

For two qubits:

$$
|\psi\rangle =
|\psi_0\rangle \otimes |\psi_1\rangle
$$

For example:

$$
|0\rangle \otimes |1\rangle = |01\rangle
$$

The dimension of the resulting statevector doubles with every additional qubit.

| Qubits | Amplitudes |
| -----: | ---------: |
|      1 |          2 |
|      2 |          4 |
|      3 |          8 |
|      4 |         16 |
|      n |      $2^n$ |

## Computational-Basis States

A computational-basis state contains one non-zero amplitude.

For example:

```python
state = StateVector([
    Qubit.zero(),
    Qubit.one()
])
```

represents:

$$
|01\rangle
$$

Its amplitude for `|01⟩` is `1`, while the amplitudes of the other computational-basis states are `0`.

## StateVector and Measurement

Statevectors can be passed to OQubit's measurement functions.

```python
from oqubit.measurement import measure, sample

result = measure(state)
```

For repeated measurements:

```python
results = sample(
    state,
    shots=1000
)
```

See [Measurement](measurement.md) for more information.

## StateVector and Circuits

`StateVector` provides the underlying quantum-state representation, while `Circuit` provides a structured representation of quantum operations.

This separation allows OQubit to represent:

```text
Quantum State
     ▲
     │
StateVector
     ▲
     │
Quantum Operations
     ▲
     │
Circuit / Instructions
```

See [Circuits](circuits.md) for more information.

## Example

The following example creates a two-qubit state and displays its notation:

```python
from oqubit.core.qubit import Qubit
from oqubit.core.statevector import StateVector

q0 = Qubit.zero()
q1 = Qubit.one()

state = StateVector([
    q0,
    q1
])

print(state)
print(state.notation)
```

The resulting system represents:

$$
|01\rangle
$$

## Summary

`StateVector` provides the multi-qubit state representation used by OQubit.

Key concepts include:

* A `StateVector` is constructed from `Qubit` objects.
* Qubit states are combined using tensor products.
* An `n`-qubit system has `2^n` amplitudes.
* Gates can be applied using `targets` and, when required, `controls`.
* The `notation` property provides a readable representation of the quantum state.
* Statevectors can be measured and used as the underlying state of quantum circuits.