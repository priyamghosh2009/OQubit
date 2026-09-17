# Qubits

The `Qubit` class is the fundamental quantum-state representation in OQubit.

A single qubit is represented as:

$$
|\psi\rangle = \alpha|0\rangle + \beta|1\rangle
$$

where `α` and `β` are complex amplitudes.

For a normalized qubit:

$$
|\alpha|^2 + |\beta|^2 = 1
$$

## Importing `Qubit`

```python
from oqubit.core.qubit import Qubit
```

## Creating a Qubit

A qubit can be created by providing its two amplitudes:

```python
q = Qubit(
    alpha=1,
    beta=0
)
```

This represents:

$$
|0\rangle
$$

You can also provide complex amplitudes:

```python
q = Qubit(
    alpha=0.6,
    beta=0.8
)
```

By default, OQubit normalizes the supplied amplitudes.

## Normalization

The constructor accepts the `normalize` parameter.

```python
q = Qubit(
    alpha=1,
    beta=1
)
```

With normalization enabled, the state becomes:

$$
|\psi\rangle =
\frac{1}{\sqrt{2}}|0\rangle +
\frac{1}{\sqrt{2}}|1\rangle
$$

To keep the supplied amplitudes unchanged:

```python
q = Qubit(
    alpha=1,
    beta=1,
    normalize=False
)
```

Use `normalize=False` when you intentionally need to work with an unnormalized state.

A zero-amplitude state cannot be normalized and raises `ValueError` when normalization is requested.

## Standard States

OQubit provides class methods for commonly used single-qubit states.

### Zero State

```python
q = Qubit.zero()
```

Represents:

$$
|0\rangle
$$

### One State

```python
q = Qubit.one()
```

Represents:

$$
|1\rangle
$$

### Plus State

```python
q = Qubit.plus()
```

Represents:

$$
|+\rangle =
\frac{|0\rangle + |1\rangle}{\sqrt{2}}
$$

### Minus State

```python
q = Qubit.minus()
```

Represents:

$$
|-\rangle =
\frac{|0\rangle - |1\rangle}{\sqrt{2}}
$$

### Positive Imaginary State

```python
q = Qubit.i()
```

### Negative Imaginary State

```python
q = Qubit.minus_i()
```

These methods provide convenient access to commonly used states without manually specifying their amplitudes.

## Measurement Probabilities

The `Qubit` class provides two probability properties:

```python
q.prob_0
q.prob_1
```

For example:

```python
q = Qubit.plus()

print(q.prob_0)
print(q.prob_1)
```

For the `|+⟩` state, both values are:

```text
0.5
0.5
```

The probabilities correspond to measuring the qubit in the computational basis:

$$
P(0) = |\alpha|^2
$$

$$
P(1) = |\beta|^2
$$

## Complex Amplitudes

Qubit amplitudes can be complex numbers:

```python
q = Qubit(
    alpha=1 + 0j,
    beta=0 + 1j
)
```

Complex amplitudes are essential for representing quantum phase.

## Inspecting a Qubit

A `Qubit` can be printed directly:

```python
q = Qubit.plus()

print(q)
```

The object provides a representation of its quantum state that can be used while experimenting with OQubit.

## Example

A simple example using several standard states:

```python
from oqubit.core.qubit import Qubit

states = [
    Qubit.zero(),
    Qubit.one(),
    Qubit.plus(),
    Qubit.minus(),
    Qubit.i(),
    Qubit.minus_i(),
]

for state in states:
    print(state)
```

## Qubits and StateVectors

A `Qubit` represents one quantum bit, while a `StateVector` represents the combined state of multiple qubits.

For example:

```python
from oqubit.core.qubit import Qubit
from oqubit.core.statevector import StateVector

state = StateVector([
    Qubit.zero(),
    Qubit.one(),
])

print(state)
```

This produces the two-qubit state:

$$
|01\rangle
$$

See [StateVectors](statevectors.md) for more information.

## Summary

The `Qubit` class provides:

* Direct construction from `alpha` and `beta` amplitudes
* Automatic normalization
* Optional `normalize=False`
* Computational-basis probabilities
* Standard states such as `zero()`, `one()`, `plus()`, and `minus()`
* Complex amplitude support

The `Qubit` class forms the foundation for OQubit's statevector and circuit functionality.