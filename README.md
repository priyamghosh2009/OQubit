# OQubit

## **OQubit** is an open-source quantum computing simulator written in Python.

It provides a clean, extensible framework for representing qubits, state vectors, quantum gates, circuits, measurements, and quantum algorithms. OQubit is designed for **quantum computing education, experimentation, algorithm development, and research-oriented software development**.

> **OQubit is currently under active development. APIs may change between releases.**

---

## Features

* Qubit state representation
* State-vector simulation
* Single-qubit quantum gates
* Controlled and multi-qubit gates
* Quantum circuits
* Measurement and sampling
* Quantum algorithms
* Jupyter Notebook examples
* Unit tests and benchmarks

### Algorithms

OQubit currently provides implementations of several fundamental quantum algorithms, including:

* Deutsch algorithm
* Deutsch-Jozsa algorithm
* Bernstein-Vazirani algorithm
* Superdense Coding

More algorithms are being added as the project develops.

---

## Installation

Install the latest released version from PyPI:

```bash
pip install oqubit
```

For development, clone the repository:

```bash
git clone https://github.com/priyamghosh2009/OQubit.git
cd OQubit
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it on Windows:

```powershell
.venv\Scripts\Activate.ps1
```

Or on Linux/macOS:

```bash
source .venv/bin/activate
```

Install the project:

```bash
pip install -e .
```

---

## Quick Start

### Create a qubit

```python
from oqubit import Qubit

q = Qubit(0,1,normalize=True)

print(q)
```

The default qubit represents the computational basis state:

$$
|0\rangle =
\begin{bmatrix}
1 \\
0
\end{bmatrix}
$$

A qubit can also be initialized using complex amplitudes:

```python
from oqubit import Qubit

q = Qubit(
    alpha=1 / 2**0.5,
    beta=1 / 2**0.5
)

print(q.state)
```

This represents the state:

$$
|\psi\rangle =
\frac{1}{\sqrt{2}}|0\rangle +
\frac{1}{\sqrt{2}}|1\rangle
$$

---

## State Vectors

Multiple qubits can be combined into a state vector.

```python
from oqubit import Qubit, StateVector

q0 = Qubit.zero()
q1 = Qubit.zero()

state = StateVector([q0, q1])

print(state)
```

The resulting system represents:

$$
|00\rangle
$$

OQubit uses tensor products to construct multi-qubit state vectors.

---

## Quantum Gates

OQubit provides standard quantum gates such as:

* X
* Y
* Z
* H
* S
* T
* Controlled-X
* Controlled-Z
* SWAP
* and other gates supported by the library

Example:

```python
from oqubit import Qubit, StateVector
from oqubit import H, X

q = Qubit.zero()

state = StateVector([q])

state.apply(H,targets=0)

print(state)
```

---

## Quantum Circuits

Quantum circuits provide a higher-level interface for composing operations.

```python
import oqubit

circuit = oqubit.Circuit(2)

circuit.h(0)
circuit.cx(0, 1)

print(circuit)
```

The circuit represents a Bell-state preparation circuit:

$$
|00\rangle
\xrightarrow{H_0}
\frac{|00\rangle + |10\rangle}{\sqrt{2}}
\xrightarrow{CX}
\frac{|00\rangle + |11\rangle}{\sqrt{2}}
$$

---

## Measurement

Quantum states can be measured using OQubit's measurement API.

```python
from oqubit import measure,Qubit,StateVector
q = Qubit.zero()
state = StateVector([q])
result = measure(state)
print(result)
```

Repeated measurements can be simulated through sampling:

```python
from oqubit import sample
from oqubit import ,Qubit,StateVector
q = Qubit.zero()
state = StateVector([q])
results = sample(state, shots=1000)

print(results)
```

---

## Algorithms

OQubit provides an algorithms package:

```python
from oqubit.algorithms import deutsch
```

For example:

```python
def sq(x):
    return x**2
result = deutsch(sq)
print(result)
```

Algorithm implementations are built using OQubit's circuit and state-vector APIs rather than being independent simulation systems.

This keeps the algorithms closely connected to the core simulator architecture.

---

## Project Structure

```text
OQubit/
|
├── src/
│   └── oqubit/
│       ├── algorithms/
│       ├── circuit/
│       ├── core/
│       ├── gates/
│       ├── measurement/
│       └── __init__.py
│
├── tests/
│
├── benchmarks/
│
├── examples/
│
├── docs/
│
├── scripts/
│
├── CITATION.cff
├── CODE_OF_CONDUCT.md
├── CONTRIBUTING.md
├── SECURITY.md
├── LICENSE
├── README.md
└── setup.py
```

---

## Development

Install the development dependencies:

```bash
pip install -e .
pip install pytest
```

Run the test suite:

```bash
pytest -v
```

Run a specific test:

```bash
pytest -v tests/test_qubit.py
```

---

## Examples

The `examples/` directory contains executable examples and Jupyter notebooks demonstrating OQubit.

Examples include:

```text
examples/
├── 01_qubit.ipynb
├── 02_statevector.ipynb
├── 03_gates.ipynb
├── 04_circuit.ipynb
├── ...
├── 08_deutsch.ipynb
├── 09_deutsch_jozsa.ipynb
├── 10_bernstein_vazirani.ipynb
└── 11_superdense_coding.ipynb
```

The notebooks are intended to make the underlying quantum operations transparent rather than hiding the simulation behind a high-level interface.

---

## Architecture

OQubit is organized into several layers.

### Core

The core layer contains fundamental quantum representations:

```text
core/
├── qubit.py
├── statevector.py
└── operators.py
```

### Gates

The gates layer contains quantum gate definitions:

```text
gates/
├── single.py
├── controlled.py
└── multi.py
```

### Circuits

The circuit layer represents sequences of quantum instructions:

```text
circuit/
├── circuit.py
└── instruction.py
```

### Measurement

Measurement and statistical sampling are separated from state representation:

```text
measurement/
├── measurement.py
└── sampling.py
```

### Algorithms

Higher-level quantum algorithms are implemented using the simulator:

```text
algorithms/
|-- deutsch.py
|-- deutsch_jozsa.py
├── bernstein_vazirani.py
└── superdense_coding.py
```

This separation is intended to keep the simulator modular and make future backend development easier.

---
## Testing and Benchmarks

OQubit uses automated tests to validate its core components.

The project also contains benchmarks for measuring the performance of operations such as:

* Qubit creation
* State-vector construction
* Quantum gates
* Circuit execution
* Quantum algorithms

Performance results should be interpreted in the context of simulator configuration, Python version, hardware, and circuit size.

---

## Contributing

Contributions are welcome.

Before contributing, please read:

* `CONTRIBUTING.md`
* `CODE_OF_CONDUCT.md`
* `SECURITY.md`

For bugs, feature requests, documentation improvements, or other development discussions, use the appropriate GitHub repository channels.

---

## Security

Please do not publicly disclose security-sensitive issues before they have been responsibly reported.

See `SECURITY.md` for the project's security reporting process.

---

## Citation

If you use OQubit in research, education, software, or other work, please cite the project.

Citation information is provided in:

```text
CITATION.cff
```

---

## License

OQubit is distributed under the license specified in:

```text
LICENSE
```

---

## Author

**Priyam Ghosh**

GitHub: `priyamghosh2009`

ORCID: `0009-0006-8619-349X`

---

## Status

OQubit is an **open-source quantum computing simulator under active development**.

The project focuses on building a transparent and extensible simulation stack in Python, with future work exploring higher-performance native backends.

---

**OQubit — Quantum computing, simulated.**