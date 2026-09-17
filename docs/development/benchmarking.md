# Benchmarking

OQubit uses benchmarks to measure the performance of selected parts of the library and to help identify performance changes between versions.

Benchmark files are stored separately from the test suite:

```text
OQubit/
├── benchmarks/
│   ├── benchmark_deutsch.py
│   ├── benchmark_bernstein_vazirani.py
│   └── benchmark_superdense_coding.py
│
└── tests/
```

## Purpose

Benchmarks are useful for measuring:

* Execution time
* Performance changes between implementations
* Algorithm execution overhead
* Performance regressions
* The effect of future optimizations

Benchmarks are different from regular tests.

**Tests** determine whether functionality is correct.

**Benchmarks** measure how efficiently that functionality executes.

---

## Benchmark Structure

OQubit benchmarks use `pytest-benchmark`.

A benchmark can measure a callable by passing it to the benchmark fixture:

```python
def test_algorithm(benchmark):
    result = benchmark(algorithm)
```

The benchmark framework executes the operation repeatedly and records timing information.

The exact benchmark setup should follow the API of the algorithm being measured.

---

## Running Benchmarks

Install the development dependencies required by the project, including `pytest` and `pytest-benchmark`.

From the repository root, benchmarks can be run with:

```powershell
pytest benchmarks/
```

To run one benchmark file:

```powershell
pytest benchmarks/benchmark_deutsch.py
```

Another example:

```powershell
pytest benchmarks/benchmark_bernstein_vazirani.py
```

And:

```powershell
pytest benchmarks/benchmark_superdense_coding.py
```

---

## Benchmark Results

A benchmark run reports execution-time information for the measured operations.

Example output may look similar to:

```text
-------------------------------- benchmark: 1 tests --------------------------------
Name                 Min      Max     Mean
test_algorithm       ...      ...     ...
```

The exact values depend on the computer, Python version, operating system, system load, and OQubit version.

Benchmark numbers should therefore be compared under similar conditions.

---

## Benchmarking Algorithms

OQubit currently includes benchmarks for several algorithm implementations.

### Deutsch

```text
benchmarks/benchmark_deutsch.py
```

Measures the execution of the Deutsch algorithm.

### Bernstein–Vazirani

```text
benchmarks/benchmark_bernstein_vazirani.py
```

Measures the execution of the Bernstein–Vazirani algorithm.

### Superdense Coding

```text
benchmarks/benchmark_superdense_coding.py
```

Measures operations associated with the Superdense Coding implementation.

For Superdense Coding, the benchmark must use the actual API:

```python
circuit = encode(1, 0)
```

rather than passing the two bits as a single string.

The resulting circuit can then be supplied to:

```python
decode(circuit)
```

---

## Benchmarks vs Tests

Benchmarks should not replace functional tests.

For example:

```text
tests/
└── Verify that the algorithm produces the expected result.

benchmarks/
└── Measure how long the algorithm takes to execute.
```

A benchmark may successfully measure a function even when the function's result is incorrect, so correctness should be covered separately by the test suite.

---

## Keeping Benchmarks Reliable

When adding or modifying a benchmark:

1. Use a valid OQubit API.
2. Keep the measured operation focused.
3. Avoid unnecessary work inside the timed section.
4. Keep benchmark inputs consistent when comparing versions.
5. Run benchmarks on the same environment when comparing results.
6. Use regular tests to verify correctness separately.

For example, if setup is not part of what you want to measure, prepare the input before calling the benchmark:

```python
circuit = encode(1, 0)

def test_decode(benchmark):
    result = benchmark(decode, circuit)
```

This helps ensure that the measurement focuses on the operation being evaluated.

---

## Benchmarking During Development

Benchmarks are particularly useful when making performance-related changes to OQubit.

A typical workflow is:

```text
Make change
    │
    ▼
Run tests
    │
    ▼
Run benchmarks
    │
    ▼
Compare results
    │
    ▼
Review performance change
```

Correctness should always be established before using benchmark results to evaluate an optimization.

---

## Environment Matters

Benchmark results are affected by the execution environment.

Important factors include:

* Python version
* OQubit version
* Operating system
* CPU
* Available memory
* Background processes
* Number of benchmark iterations
* Input size

For meaningful comparisons, record the environment when reporting significant benchmark results.

---

## Adding a New Benchmark

New benchmark files should be placed in:

```text
benchmarks/
```

Use a descriptive filename such as:

```text
benchmark_<feature>.py
```

For example:

```text
benchmark_statevector.py
```

A benchmark should focus on a specific operation or feature rather than combining unrelated measurements into one test.

---

## Performance Development

Benchmarking is intended to support OQubit development as the simulator grows.

Future performance work may include measuring:

* Larger statevectors
* Multi-qubit operations
* Gate application
* Measurement and sampling
* Quantum algorithms
* Alternative execution backends

Benchmark results should be treated as measurements of a particular implementation and environment, not as universal performance guarantees.