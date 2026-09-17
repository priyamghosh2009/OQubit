# Quickstart

This guide introduces the basic workflow of OQubit using its quantum states, statevectors, gates, circuits, measurement tools, and algorithms.

## 1. Import OQubit

Start by importing the main components:

```python
from oqubit.core.qubit import Qubit
from oqubit.core.statevector import StateVector
```

## 2. Create a Qubit

A qubit is represented by two complex amplitudes:

$$
|\psi\rangle = \alpha|0\rangle + \beta|1\rangle
$$

Create a qubit directly using `Qubit`:

```python
q = Qubit(alpha=1, beta=0)

print(q)
```

By default, OQubit normalizes the amplitudes.

You can also disable automatic normalization:

```python
q = Qubit(
    alpha=1,
    beta=0,
    normalize=False
)
```

## 3. Use Standard Qubit States

OQubit provides class methods for commonly used states:

```python
zero = Qubit.zero()
one = Qubit.one()

plus = Qubit.plus()
minus = Qubit.minus()

i = Qubit.i()
minus_i = Qubit.minus_i()
```

For example:

```python
q = Qubit.plus()

print(q)
```

represents the `|+⟩` state:

$$
|+\rangle =
\frac{1}{\sqrt{2}}|0\rangle +
\frac{1}{\sqrt{2}}|1\rangle
$$

## 4. Inspect Measurement Probabilities

A qubit exposes its computational-basis probabilities:

```python
q = Qubit.plus()

print(q.prob_0)
print(q.prob_1)
```

For `|+⟩`, both probabilities are approximately `0.5`.

## 5. Create a StateVector

Multiple qubits can be combined into a `StateVector`:

```python
q0 = Qubit.zero()
q1 = Qubit.one()

state = StateVector([
    q0,
    q1
])

print(state)
```

This represents the two-qubit computational basis state:

$$
|01\rangle
$$

OQubit constructs the combined state using the tensor product of the individual qubit states.

## 6. Display State Notation

A `StateVector` can be represented using ket notation:

```python
print(state.notation)
```

For example, a two-qubit state can be displayed in a form such as:

```text
(1+0j)|01⟩
```

This notation is useful when inspecting quantum states during development and experimentation.

## 7. Apply Gates to a StateVector

Quantum gates can be applied to a statevector through `StateVector.apply()`.

For example, a gate can be applied to a target qubit:

```python
from oqubit.core.operators import Gate

# Use a gate provided by the OQubit gates package.
# Example:
# from oqubit.gates.single import H

state.apply(H, targets=[0])
```

For controlled operations, specify both the control and target qubits according to the gate's API:

```python
state.apply(
    gate,
    controls=[0],
    targets=[1]
)
```

The exact gate objects available depend on the OQubit release.

## 8. Build a Circuit

OQubit provides the `Circuit` class for representing quantum circuits:

```python
from oqubit.circuit.circuit import Circuit

circuit = Circuit(2)
```

A circuit contains quantum instructions that describe operations performed on its qubits.

Instructions are represented using the `Instruction` abstraction:

```python
from oqubit.circuit.instruction import Instruction
```

The circuit API can then be used to construct and execute supported operations.

## 9. Measure Quantum States

Measurement functionality is provided by the measurement package:

```python
from oqubit.measurement import measure, sample
```

A state can be measured using:

```python
result = measure(state)

print(result)
```

For repeated measurements, use `sample()`:

```python
results = sample(state, shots=1000)

print(results)
```

Sampling allows you to observe the distribution of computational-basis measurement outcomes.

## 10. Run a Quantum Algorithm

OQubit includes quantum algorithms in:

```text
oqubit.algorithms
```

For example, Deutsch's algorithm can be imported with:

```python
from oqubit.algorithms.deutsch import deutsch
```

Other algorithms included in OQubit include:

```text
Deutsch
Deutsch-Jozsa
Bernstein-Vazirani
Superdense Coding
```

See the [Algorithms](../user-guide/algorithms.md) guide for algorithm-specific usage.

## A Simple OQubit Example

The following example creates two qubits and combines them into a statevector:

```python
from oqubit.core.qubit import Qubit
from oqubit.core.statevector import StateVector

q0 = Qubit.zero()
q1 = Qubit.one()

state = StateVector([
    q0,
    q1
])

print("State:")
print(state)

print("Notation:")
print(state.notation)
```

Output represents the state:

```text
|01⟩
```

## Next Steps

Continue with the User Guide to learn more about individual OQubit components:

* [Qubits](../user-guide/qubits.md)
* [StateVectors](../user-guide/statevectors.md)
* [Gates](../user-guide/gates.md)
* [Circuits](../user-guide/circuits.md)
* [Measurement](../user-guide/measurement.md)
* [Algorithms](../user-guide/algorithms.md)