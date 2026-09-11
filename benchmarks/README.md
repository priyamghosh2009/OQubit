# OQubit Benchmarks

This directory contains the performance benchmark suite for **OQubit**, a Python quantum computing and quantum simulation library.

The benchmark suite measures the execution performance of selected OQubit operations and provides reproducible performance measurements for tracking optimization and regression over time.

---

## Overview

The OQubit benchmark suite is designed to:

* Measure the performance of core OQubit operations.
* Establish performance baselines.
* Detect performance regressions.
* Evaluate performance improvements.
* Provide reproducible benchmark results.
* Track performance as OQubit evolves.

The benchmark suite uses [`pytest-benchmark`](https://pytest-benchmark.readthedocs.io/) for repeated and statistically useful measurements.

---

## Directory Structure

```text
benchmarks/
├── README.md
├── benchmark_qubit.py
├── benchmark_statevector.py
├── benchmark_gates.py
├── benchmark_circuit.py
└── results/
    └── results.json
```

The exact structure may change as additional benchmarks are added.

### Benchmark Files

| File                  | Description                                       |
| --------------------- | ------------------------------------------------- |
| `README.md`           | Documentation, methodology, and benchmark results |
| `benchmark_qubit.py`       | Benchmarks for `Qubit` operations                 |
| `benchmark_statevector.py` | Benchmarks for `StateVector` operations           |
| `benchmark_gates.py`  | Benchmarks for quantum gates                      |
| `benchmark_circuit.py`| Benchmarks for Quantum Circuits                   |
| `results/`            | Optional stored benchmark results                 |

---

# Requirements

The benchmark suite requires:

* Python 3.11 or a compatible Python version
* OQubit
* `pytest`
* `pytest-benchmark`

Install the benchmarking dependencies with:

```bash
pip install pytest pytest-benchmark
```

If OQubit is being developed locally, install it in editable mode:

```bash
pip install -e .
```

---

# Running the Benchmarks

Run the complete benchmark suite:

```bash
pytest benchmarks/ --benchmark-only
```

Sort the results by mean execution time:

```bash
pytest benchmarks/ --benchmark-only --benchmark-sort=mean
```

Run the Qubit benchmarks:

```bash
pytest benchmarks/test_qubit.py --benchmark-only
```

Run the StateVector benchmarks:

```bash
pytest benchmarks/test_statevector.py --benchmark-only
```

Run the gate benchmarks:

```bash
pytest benchmarks/test_gates.py --benchmark-only
```

---

# Saving Benchmark Results

Benchmark results can be exported to JSON:

```bash
pytest benchmarks/ \
    --benchmark-only \
    --benchmark-json=benchmarks/results/results.json
```

The JSON file can be retained for later analysis or comparison between different versions of OQubit.

---

# Benchmark Categories

## Qubit Benchmarks

The Qubit benchmarks measure the performance of fundamental single-qubit operations.

Current benchmark targets may include:

* Qubit construction
* `Qubit.zero()`
* `Qubit.plus()`
* `Qubit.minus()`
* Qubit state initialization

Example:

```python
benchmark(Qubit.zero)
```

---

## StateVector Benchmarks

The StateVector benchmarks measure operations involving multi-qubit quantum states.

Current benchmark targets may include:

* StateVector construction
* Tensor-product state construction
* State access
* State notation generation

Example:

```python
benchmark(StateVector, qubits)
```

---

## Gate Benchmarks

The gate benchmarks measure the performance of applying quantum gates.

Current benchmark targets may include:

* Pauli-X
* Pauli-Y
* Pauli-Z
* Hadamard
* Other implemented single-qubit gates

Example:

```python
benchmark(operation)
```

where `operation` performs the gate application being measured.

---
## Circuit Benchmarks

The circuit benchmarks measure the performance of executing quantum circuits.

Current benchmark targets may include:

* Circuit construction

* Gate insertion

* Circuit execution

* Circuits containing multiple quantum gates

* Other implemented circuit operations

Example:

```python
benchmark(operation)
```

# Benchmark Methodology

OQubit uses `pytest-benchmark` instead of measuring a single function call with `time.time()`.

A single measurement can be affected by:

* Operating-system scheduling
* Background processes
* CPU frequency changes
* Memory allocation
* Cache effects
* Other system activity

`pytest-benchmark` performs repeated measurements and provides statistical information about the execution time.

Typical metrics include:

| Metric     | Description                     |
| ---------- | ------------------------------- |
| Min        | Minimum measured execution time |
| Max        | Maximum measured execution time |
| Mean       | Average execution time          |
| StdDev     | Standard deviation              |
| Rounds     | Number of benchmark rounds      |
| Iterations | Number of iterations per round  |

For execution-time benchmarks, **lower execution time is generally better**.

---

# Benchmark Environment

Benchmark results depend on the system on which they are executed.

Each published benchmark result should record the relevant environment.

Recommended information includes:

```text
Operating System:
Python:
OQubit version:
pytest version:
pytest-benchmark version:

CPU:
RAM:

NumPy version:
```

For example:

```text
Operating System: Windows 11
Python: 3.11
CPU: AMD Ryzen 3 5300U
RAM: 8 GB
```

Recording the environment makes future benchmark comparisons more meaningful.

---

# Results

The results in this section should contain measurements from an actual benchmark run.

**Do not manually estimate or invent benchmark values.**

## Qubit

| Benchmark       | Min | Max | Mean | StdDev |
| --------------- | --: | --: | ---: | -----: |
| Qubit creation  |   — |   — |    — |      — |
| `Qubit.zero()`  |   — |   — |    — |      — |
| `Qubit.plus()`  |   — |   — |    — |      — |
| `Qubit.minus()` |   — |   — |    — |      — |

---

## StateVector

| Benchmark               | Min | Max | Mean | StdDev |
| ----------------------- | --: | --: | ---: | -----: |
| StateVector creation    |   — |   — |    — |      — |
| StateVector notation    |   — |   — |    — |      — |
| State-vector operations |   — |   — |    — |      — |

---

## Gates

| Benchmark | Min | Max | Mean | StdDev |
| --------- | --: | --: | ---: | -----: |
| Pauli-X   |   — |   — |    — |      — |
| Pauli-Y   |   — |   — |    — |      — |
| Pauli-Z   |   — |   — |    — |      — |
| Hadamard  |   — |   — |    — |      — |

> The tables above are placeholders until an actual benchmark run is performed.

---

## Circuit

| Benchmark | Min | Max | Mean | StdDev |
| --------- | --: | --: | ---: | -----: |
| Circuit creation | — | — | — | — |
| Gate insertion | — | — | — | — |
| Circuit execution | — | — | — | — |

> The tables above are placeholders until an actual benchmark run is performed.

---

# Example Output

A benchmark run may produce output similar to:

```text
-------------------------------- benchmark 'qubit' --------------------------------

Name                     Min      Max     Mean    StdDev
---------------------------------------------------------
test_qubit_creation      ...      ...     ...       ...
test_qubit_zero          ...      ...     ...       ...
test_qubit_plus          ...      ...     ...       ...
test_qubit_minus         ...      ...     ...       ...

-------------------------------- benchmark 'gates' --------------------------------

Name                     Min      Max     Mean    StdDev
---------------------------------------------------------
test_x_gate              ...      ...     ...       ...
test_y_gate              ...      ...     ...       ...
test_z_gate              ...      ...     ...       ...
test_h_gate              ...      ...     ...       ...
```

The exact values will depend on the benchmark environment and OQubit implementation.

---

# Reproducibility

To reproduce the benchmark results, use the same:

* OQubit version or Git revision
* Python version
* Dependency versions
* Hardware
* Operating system
* Benchmark inputs

It is also recommended to minimize other CPU-intensive activity while benchmarking.

Run:

```bash
pytest benchmarks/ --benchmark-only --benchmark-sort=mean
```

To save the results:

```bash
pytest benchmarks/ \
    --benchmark-only \
    --benchmark-json=benchmarks/results/results.json
```

---

# Comparing Implementations

Benchmarking is useful when evaluating performance changes between implementations.

For example, a baseline can be saved with:

```bash
pytest benchmarks/ \
    --benchmark-only \
    --benchmark-save=baseline
```

After making a performance-related change:

```bash
pytest benchmarks/ \
    --benchmark-only \
    --benchmark-compare=baseline
```

This allows the new implementation to be compared with the previous baseline.

---

# Benchmark Fairness

When comparing two implementations, the following should remain consistent:

* Input data
* Number of qubits
* Initial state
* Gate sequence
* Numerical precision
* Number of operations
* Hardware
* Python version
* Dependency versions

Only the implementation being evaluated should change.

This helps ensure that measured performance differences are caused by the implementation rather than by changes in the benchmark conditions.

---

# Avoiding Incorrect Benchmarks

Benchmark setup should be separated from the operation being measured whenever possible.

For example, prefer:

```python
benchmark(Qubit.zero)
```

rather than:

```python
benchmark(Qubit.zero())
```

The first form allows the benchmark framework to measure the function call itself.

For an operation requiring arguments:

```python
benchmark(Qubit, 1, 0)
```

or:

```python
benchmark(lambda: Qubit(1, 0))
```

can be used depending on the operation being tested.

The benchmark should measure the operation of interest rather than unrelated setup work.

---

# Quantum State Scaling

Future benchmark versions can evaluate how OQubit performance changes as the number of qubits increases.

For a state-vector simulator, an `n`-qubit system contains:

```text
2ⁿ
```

complex amplitudes.

For example:

| Qubits | Amplitudes |
| -----: | ---------: |
|      1 |          2 |
|      2 |          4 |
|      4 |         16 |
|      8 |        256 |
|     10 |      1,024 |
|     16 |     65,536 |
|     20 |  1,048,576 |

Scaling benchmarks can help characterize the computational and memory requirements of OQubit's simulator.

---

# Future Benchmarks

As OQubit develops, additional benchmark categories may be added, including:

* Multi-qubit gates
* Controlled gates
* Measurement
* Probability calculations
* State normalization
* Operator multiplication
* Matrix multiplication
* Circuit execution
* Circuit-depth scaling
* Number-of-qubits scaling
* Numerical precision comparisons
* Memory usage

Only benchmarks that are actually implemented should be included in the current benchmark results.

---

# Performance Regression Testing

Benchmark results can be used to identify performance regressions.

For example, if a new implementation performs significantly slower than an established baseline, the change can be investigated before being considered complete.

Potential causes of regressions may include:

* Additional memory allocations
* Unnecessary matrix construction
* Repeated tensor products
* Excessive copying
* Inefficient Python-level loops
* Additional normalization operations
* Changes to numerical representations

Performance measurements should always be considered alongside OQubit's correctness tests.

---

# Historical Results

For long-term performance tracking, benchmark results may be stored separately using dated files:

```text
benchmarks/
└── results/
    ├── 2026-09-11.json
    ├── 2026-10-01.json
    └── ...
```

Historical results make it possible to observe how OQubit's performance changes over time.

---

# Updating the Results

Benchmark results should be updated when:

* A significant performance optimization is introduced.
* A major OQubit version is released.
* The benchmark suite changes substantially.
* A new benchmark category is introduced.
* The benchmark environment changes significantly.

When updating results, record the environment used for the benchmark run.

---

# Limitations

Benchmark results are affected by the execution environment.

Factors that may influence results include:

* CPU architecture
* CPU frequency
* RAM performance
* Operating-system scheduling
* Background processes
* Python implementation and version
* NumPy version
* OQubit version
* System temperature and power-management behavior

Therefore, benchmark results should be treated as **reference measurements**, rather than universal performance guarantees.

---

# Contributing

When adding a new benchmark:

1. Keep the benchmark focused on a specific operation.
2. Avoid unnecessary work inside the measured function.
3. Use consistent and deterministic inputs where possible.
4. Document unusual benchmark assumptions.
5. Run the benchmark multiple times.
6. Record the relevant environment.
7. Avoid drawing conclusions from a single measurement.

New benchmarks should also have corresponding correctness tests where appropriate.

---

# License

The OQubit benchmark suite is distributed as part of the OQubit project and is subject to the license specified by the project.

---

**OQubit — Quantum Computing and Simulation in Python**
