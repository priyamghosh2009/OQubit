# OQubit Architecture

This document describes the internal structure of OQubit and how its main components work together.

OQubit is organized into separate modules for quantum states, operators, gates, circuits, measurement, and algorithms.

## Project Structure

The main source tree is:

```text
OQubit/
│
├── src/
│   └── oqubit/
│       ├── algorithms/
│       │   ├── deutsch.py
│       │   ├── deutsch_jozsa.py
│       │   ├── bernstein_vazirani.py
│       │   └── superdense_coding.py
│       │
│       ├── circuit/
│       │   ├── circuit.py
│       │   └── instruction.py
│       │
│       ├── core/
│       │   ├── qubit.py
│       │   ├── statevector.py
│       │   └── operators.py
│       │
│       ├── gates/
│       │   ├── single.py
│       │   ├── controlled.py
│       │   └── multi.py
│       │
│       ├── measurement/
│       │   ├── measurement.py
│       │   └── sampling.py
│       │
│       └── __init__.py
│
├── tests/
├── benchmarks/
├── examples/
└── docs/
```

---

## Architecture Overview

The main components can be viewed as layers:

```text
┌─────────────────────────────┐
│         Algorithms          │
├─────────────────────────────┤
│          Circuits           │
├─────────────────────────────┤
│      Gates / Operators      │
├─────────────────────────────┤
│      StateVector / Qubit    │
├─────────────────────────────┤
│         Measurement         │
└─────────────────────────────┘
```

These modules are separated so that individual components can be used independently.

---

## Core

The `core` package contains the fundamental representations used by the simulator.

```text
oqubit/core/
├── qubit.py
├── statevector.py
└── operators.py
```

### Qubit

`qubit.py` provides the `Qubit` class.

A qubit is represented using two complex amplitudes:

$$
|\psi\rangle = \alpha|0\rangle + \beta|1\rangle
$$

The class also provides commonly used states such as:

```python
Qubit.zero()
Qubit.one()
Qubit.plus()
Qubit.minus()
Qubit.i()
Qubit.minus_i()
```

Normalization is handled by the `Qubit` implementation when enabled.

### StateVector

`statevector.py` provides the `StateVector` class.

A statevector represents a system containing one or more qubits.

For `n` qubits, the statevector contains:

$$
2^n
$$

complex amplitudes.

`StateVector` also provides operations for applying gates to selected qubit targets and, where required, controlled operations.

### Operators

`operators.py` contains the underlying `Gate` abstraction used by OQubit gates and state operations.

This separates the representation of an operator from the higher-level gate modules.

---

## Gates

The `gates` package contains gate implementations:

```text
oqubit/gates/
├── single.py
├── controlled.py
└── multi.py
```

The modules separate gates according to their scope.

### Single-Qubit Gates

`single.py` contains gates that operate on individual qubits.

### Controlled Gates

`controlled.py` contains gates involving control qubits and target qubits.

### Multi-Qubit Gates

`multi.py` contains gates operating on multiple qubits.

Gates are applied to a `StateVector` using target and, when necessary, control indices.

```python
state.apply(
    gate,
    controls=[0],
    targets=[1]
)
```

This keeps gate definitions separate from the state representation.

---

## Circuits

The `circuit` package provides the structure for representing quantum circuits.

```text
oqubit/circuit/
├── circuit.py
└── instruction.py
```

### Circuit

`Circuit` represents a quantum circuit and is initialized with the number of qubits:

```python
from oqubit.circuit.circuit import Circuit

circuit = Circuit(2)
```

### Instruction

`Instruction` represents an operation within a circuit.

The separation between `Circuit` and `Instruction` allows a circuit to represent a sequence of quantum operations without embedding individual operation definitions directly into the circuit class.

---

## Measurement

Measurement is separated from the state and gate implementations:

```text
oqubit/measurement/
├── measurement.py
└── sampling.py
```

The public measurement interface provides:

```python
from oqubit.measurement import measure, sample
```

`measure()` obtains a measurement outcome from a state.

`sample()` performs repeated measurements and is useful for examining the distribution of possible outcomes.

Keeping measurement separate from `StateVector` allows quantum-state representation and classical observation to remain distinct concepts.

---

## Algorithms

The `algorithms` package contains higher-level quantum algorithms and protocols.

```text
oqubit/algorithms/
├── deutsch.py
├── deutsch_jozsa.py
├── bernstein_vazirani.py
└── superdense_coding.py
```

These implementations build on lower-level OQubit components rather than defining a separate simulation system.

Conceptually:

```text
Algorithm
    │
    ▼
Circuit / State Preparation
    │
    ▼
Gates and Operators
    │
    ▼
StateVector
    │
    ▼
Measurement
    │
    ▼
Classical Result
```

For example, Superdense Coding exposes an `encode()` operation that creates the required circuit and a `decode()` operation that interprets the resulting circuit.

---

## Separation of Responsibilities

OQubit follows a modular design where each component has a focused responsibility.

| Component      | Responsibility                           |
| -------------- | ---------------------------------------- |
| `Qubit`        | Represents a single qubit                |
| `StateVector`  | Represents multi-qubit quantum states    |
| `Gate`         | Defines the operator abstraction         |
| `gates/`       | Provides gate implementations            |
| `Circuit`      | Represents quantum circuits              |
| `Instruction`  | Represents circuit operations            |
| `measurement/` | Produces classical measurement results   |
| `algorithms/`  | Provides higher-level quantum algorithms |

This separation makes it possible to modify one part of the simulator without requiring every other component to be redesigned.

---

## Data Flow

A typical state-based computation follows this general flow:

```text
Qubit
  │
  ▼
StateVector
  │
  ├── Gate
  │     │
  │     ▼
  │  StateVector
  │
  ▼
Measurement
  │
  ▼
Classical Result
```

A circuit-based computation adds the circuit representation:

```text
Qubits
   │
   ▼
StateVector / Circuit
   │
   ▼
Instructions
   │
   ▼
Gates
   │
   ▼
Quantum State
   │
   ▼
Measurement
   │
   ▼
Result
```

---

## Design Principles

The current architecture follows several simple principles:

### Modularity

Quantum states, gates, circuits, measurement, and algorithms are implemented as separate modules.

### Reusability

Core classes such as `Qubit`, `StateVector`, and `Gate` can be used independently of the higher-level algorithm implementations.

### Explicit Qubit Indexing

Operations use explicit `controls` and `targets` when operating on multi-qubit states.

For example:

```python
state.apply(
    gate,
    controls=[0],
    targets=[1]
)
```

This makes the relationship between an operation and the qubits it affects explicit.

### Layered Design

Higher-level algorithms build on lower-level simulation components rather than duplicating their functionality.

---

## Development Direction

The architecture is designed to allow OQubit to grow without changing its fundamental concepts.

Potential future development can extend individual layers—for example, additional gates, algorithms, measurement functionality, or alternative execution backends—while keeping the core quantum-state representation separate from those higher-level features.

The architecture therefore provides a foundation for extending OQubit while keeping the simulator's components organized and independently testable.