# Quantum Algorithms

OQubit includes implementations of several introductory quantum algorithms and protocols.

The algorithm modules are located in:

```text
src/
└── oqubit/
    └── algorithms/
        ├── deutsch.py
        ├── deutsch_jozsa.py
        ├── bernstein_vazirani.py
        └── superdense_coding.py
```

These algorithms use OQubit's core quantum-state and circuit functionality.

## Available Algorithms

| Algorithm          | Module               | Purpose                                                          |
| ------------------ | -------------------- | ---------------------------------------------------------------- |
| Deutsch Algorithm  | `deutsch`            | Determines whether a one-bit function is constant or balanced    |
| Deutsch–Jozsa      | `deutsch_jozsa`      | Determines whether a function is constant or balanced            |
| Bernstein–Vazirani | `bernstein_vazirani` | Finds a hidden binary string using one oracle query              |
| Superdense Coding  | `superdense_coding`  | Communicates two classical bits using one qubit of communication |

---

## Deutsch Algorithm

Deutsch's algorithm is a simple example of quantum advantage.

It determines whether a Boolean function is **constant** or **balanced** using a quantum circuit.

The implementation is available from:

```python
from oqubit.algorithms.deutsch import deutsch
```

The algorithm demonstrates concepts such as:

* Superposition
* Quantum interference
* Oracle operations
* Measurement

A typical workflow is:

```python
from oqubit.algorithms.deutsch import deutsch

result = deutsch(...)
print(result)
```

The exact arguments depend on the oracle/function representation used by the implementation.

---

## Deutsch–Jozsa Algorithm

The Deutsch–Jozsa algorithm generalizes Deutsch's problem to functions with multiple input bits.

For a promised Boolean function, it determines whether the function is:

* **Constant** — produces the same output for every input.
* **Balanced** — produces `0` for half of the inputs and `1` for the other half.

Import the implementation with:

```python
from oqubit.algorithms.deutsch_jozsa import deutsch_jozsa
```

Example workflow:

```python
from oqubit.algorithms.deutsch_jozsa import deutsch_jozsa

result = deutsch_jozsa(...)
print(result)
```

The algorithm demonstrates how superposition allows information about multiple inputs to be processed within a single quantum computation.

---

## Bernstein–Vazirani Algorithm

The Bernstein–Vazirani algorithm finds a hidden binary string encoded in a function.

For a hidden string

```text
s = 1011
```

the algorithm can determine the string using a single oracle query in the quantum setting.

Import it with:

```python
from oqubit.algorithms.bernstein_vazirani import bernstein_vazirani
```

Example:

```python
from oqubit.algorithms.bernstein_vazirani import bernstein_vazirani

result = bernstein_vazirani(...)
print(result)
```

The algorithm demonstrates:

* Quantum superposition
* Oracle queries
* Phase encoding
* Interference
* Measurement

---

## Superdense Coding

Superdense coding is a quantum communication protocol that allows two classical bits of information to be encoded using a shared entangled pair and one transmitted qubit.

OQubit provides the protocol through the `superdense_coding` module.

```python
from oqubit.algorithms.superdense_coding import encode, decode
```

### Encoding

The `encode()` function accepts two classical bits:

```python
circuit = encode(1, 0)
```

The two arguments represent the classical bit pair being encoded.

For example:

```python
encode(0, 0)
encode(0, 1)
encode(1, 0)
encode(1, 1)
```

Each pair corresponds to one of the four possible two-bit messages.

### Decoding

The resulting circuit can then be passed to `decode()`:

```python
message = decode(circuit)

print(message)
```

The decoder recovers the encoded two-bit message.

---

## Using Algorithms

Algorithm implementations can be imported directly from their respective modules.

For example:

```python
from oqubit.algorithms.deutsch import deutsch
from oqubit.algorithms.deutsch_jozsa import deutsch_jozsa
from oqubit.algorithms.bernstein_vazirani import bernstein_vazirani
from oqubit.algorithms.superdense_coding import encode, decode
```

OQubit algorithms are built on the same underlying components used elsewhere in the library:

```text
Algorithms
    │
    ├── Circuits
    │
    ├── StateVectors
    │
    ├── Gates
    │
    └── Measurement
```

This makes the algorithms useful both as ready-to-use implementations and as examples of how OQubit can be used to construct quantum computations.

---

## Algorithms and Measurement

Most quantum algorithms eventually produce a classical result through measurement.

For state-based workflows, OQubit provides:

```python
from oqubit.measurement import measure, sample
```

For example:

```python
result = measure(state)
```

or:

```python
results = sample(state, shots=1000)
```

The algorithm determines how the quantum state is prepared and manipulated; measurement extracts the resulting classical information.

---

## Learning From the Implementations

The algorithm source code can also be used to understand how OQubit components work together.

A typical implementation combines:

1. Qubit and state preparation
2. Quantum gates
3. Circuit operations
4. Controlled operations where required
5. Measurement
6. Classical interpretation of the result

This provides a practical way to move from individual OQubit components to complete quantum algorithms.

---

## Version Scope

The algorithms documented here correspond to the algorithms included in the current OQubit release.

Additional algorithms can be added as the library evolves.