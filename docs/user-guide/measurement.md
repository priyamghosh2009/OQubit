# Measurement

Measurement converts a quantum state into classical information.

OQubit provides measurement utilities for measuring a state and for sampling measurement outcomes over multiple shots.

## Import

```python
from oqubit.measurement import measure, sample
```

---

## Measuring a State

The `measure()` function performs a measurement on a quantum state.

```python
from oqubit.core.qubit import Qubit
from oqubit.core.statevector import StateVector
from oqubit.measurement import measure

state = StateVector([
    Qubit.plus()
])

result = measure(state)

print(result)
```

The result represents a classical measurement outcome.

For a single qubit, the possible computational-basis outcomes are:

```text
0
1
```

The probability of each outcome is determined by the state's amplitudes.

---

## Sampling Measurements

The `sample()` function performs repeated measurements of a state.

```python
from oqubit.core.qubit import Qubit
from oqubit.core.statevector import StateVector
from oqubit.measurement import sample

state = StateVector([
    Qubit.plus()
])

results = sample(state, shots=1000)

print(results)
```

The `shots` parameter specifies how many measurement trials are performed.

For a state such as

$$
|+\rangle = \frac{1}{\sqrt{2}}(|0\rangle + |1\rangle),
$$

repeated sampling produces both `0` and `1` outcomes with approximately equal frequency.

Because measurement is probabilistic, the exact results can vary between runs.

---

## Measuring Multi-Qubit States

Measurement also applies to multi-qubit statevectors.

```python
from oqubit.core.qubit import Qubit
from oqubit.core.statevector import StateVector
from oqubit.measurement import sample

state = StateVector([
    Qubit.zero(),
    Qubit.plus()
])

results = sample(state, shots=1000)

print(results)
```

For multiple qubits, measurement outcomes correspond to computational-basis states such as:

```text
00
01
10
11
```

Only outcomes with non-zero probability can occur.

---

## Measurement Probabilities

Measurement probabilities come from the amplitudes of the statevector.

For a single-qubit state

$$
|\psi\rangle = \alpha|0\rangle + \beta|1\rangle,
$$

the probabilities are:

$$
P(0)=|\alpha|^2
$$

and

$$
P(1)=|\beta|^2.
$$

These probabilities are also available directly from an individual `Qubit`:

```python
from oqubit.core.qubit import Qubit

q = Qubit.plus()

print(q.prob_0)
print(q.prob_1)
```

---

## Measurement and Statevectors

A `StateVector` represents the quantum state before measurement.

```python
from oqubit.core.qubit import Qubit
from oqubit.core.statevector import StateVector
from oqubit.measurement import measure

state = StateVector([
    Qubit.plus()
])

print(state.notation)

result = measure(state)

print(result)
```

This separates the two concepts:

* **Statevector** — represents the quantum state and its amplitudes.
* **Measurement** — obtains a classical outcome from that state.

---

## Measurement and Circuits

Measurement can be used with states produced through quantum circuits and algorithms.

For example, an algorithm can construct a quantum state and then use OQubit's measurement utilities to obtain an outcome or collect repeated samples.

```python
from oqubit.measurement import measure, sample

result = measure(state)
results = sample(state, shots=1000)
```

The exact construction of `state` depends on the circuit or algorithm being used.

---

## `measure()` vs `sample()`

| Function                   | Purpose                                            |
| -------------------------- | -------------------------------------------------- |
| `measure(state)`           | Perform a measurement and obtain an outcome        |
| `sample(state, shots=...)` | Perform repeated measurements and collect outcomes |

Use `measure()` when you need an individual measurement.

Use `sample()` when you want to observe the distribution of outcomes across many trials.

---

## Summary

OQubit's measurement module provides:

* Single measurement with `measure()`
* Repeated measurement with `sample()`
* Support for single- and multi-qubit states
* Measurement based on quantum-state probabilities
* Integration with OQubit `StateVector` objects

Measurement is the step that connects OQubit's quantum-state simulation with classical measurement results.