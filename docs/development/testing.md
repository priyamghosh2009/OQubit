# Testing

OQubit uses automated tests to verify that its components and algorithms behave as expected.

The test suite is located in the repository's `tests/` directory:

```text
OQubit/
├── src/
│   └── oqubit/
├── tests/
├── benchmarks/
└── examples/
```

## Testing Tools

OQubit uses:

* **pytest** — test framework
* **pytest-benchmark** — performance benchmarking

Tests focus on correctness, while benchmarks focus on performance.

---

## Running the Test Suite

From the OQubit repository root, run:

```powershell
pytest
```

This discovers and runs the tests in the project.

To run only the tests directory:

```powershell
pytest tests/
```

---

## Running a Specific Test File

Individual test files can be executed directly.

For example:

```powershell
pytest tests/test_deutsch.py
```

or:

```powershell
pytest tests/test_bernstein_vazirani.py
```

This is useful when working on a specific component or algorithm.

---

## Test Organization

Tests are organized according to the functionality they verify.

A typical structure is:

```text
tests/
├── test_deutsch.py
├── test_deutsch_jozsa.py
├── test_bernstein_vazirani.py
└── test_superdense_coding.py
```

As OQubit grows, tests can also be added for core components such as:

```text
Qubit
StateVector
Gates
Circuit
Measurement
```

The exact test structure can evolve with the source tree.

---

## What Tests Should Verify

Tests should primarily verify **correctness**.

Examples include:

* Correct qubit initialization
* Correct normalization
* Correct probability calculations
* Correct statevector construction
* Correct gate application
* Correct control and target handling
* Correct measurement results
* Correct algorithm results
* Appropriate errors for invalid input

For example, a test for a standard qubit state might verify its probabilities:

```python
from oqubit.core.qubit import Qubit

q = Qubit.zero()

assert q.prob_0 == 1
assert q.prob_1 == 0
```

---

## Testing Algorithms

Algorithm tests should verify that the implementation produces the expected result for known inputs.

For example, the Superdense Coding API uses two separate classical bits:

```python
circuit = encode(1, 0)
message = decode(circuit)
```

A test can then verify that the decoded message corresponds to the encoded input.

This is preferable to testing only whether the functions execute without raising an exception.

---

## Testing Invalid Input

OQubit should also test how its API handles invalid input.

For example, `Qubit` rejects an invalid zero-amplitude normalization case when normalization is requested.

Tests for errors can use `pytest.raises`:

```python
import pytest
from oqubit.core.qubit import Qubit

def test_invalid_qubit():
    with pytest.raises(ValueError):
        Qubit(0, 0)
```

The expected exception should match the behavior documented by the relevant API.

---

## Test Independence

Tests should be independent from one another.

A test should ideally:

1. Create the objects it needs.
2. Perform the operation being tested.
3. Verify the result.
4. Leave no required state for another test.

This makes failures easier to reproduce and diagnose.

---

## Running Tests During Development

A simple development workflow is:

```text
Make a change
     │
     ▼
Run the relevant tests
     │
     ▼
Fix any failures
     │
     ▼
Run the complete test suite
     │
     ▼
Run benchmarks when performance is affected
```

For a larger change, running the complete suite before committing helps catch regressions outside the modified component.

---

## Tests and Benchmarks

Tests and benchmarks have different purposes.

|                         | Tests       | Benchmarks       |
| ----------------------- | ----------- | ---------------- |
| Main purpose            | Correctness | Performance      |
| Location                | `tests/`    | `benchmarks/`    |
| Typical tool            | pytest      | pytest-benchmark |
| Checks results          | Yes         | Not primarily    |
| Measures execution time | No          | Yes              |

A benchmark should not be used as a replacement for a correctness test.

---

## Debugging Test Failures

When a test fails, first identify whether the problem is:

* An implementation error
* An incorrect test expectation
* An outdated test
* An invalid API call
* An environment or dependency issue

Run the failing test separately to get a smaller and clearer failure report:

```powershell
pytest tests/test_example.py
```

For more detailed output:

```powershell
pytest -v
```

For a specific test:

```powershell
pytest -v tests/test_example.py
```

---

## Adding Tests

When adding a new feature to OQubit, add tests covering its expected behavior.

A useful sequence is:

1. Define the expected behavior.
2. Write tests for that behavior.
3. Implement or modify the feature.
4. Run the tests.
5. Add regression tests for bugs that are discovered later.

Tests should reflect the public behavior of OQubit rather than relying unnecessarily on private implementation details.

---

## Before a Release

Before preparing a release, run the complete test suite:

```powershell
pytest
```

A release should also be checked for:

* Passing tests
* Correct package structure
* Working examples
* Correct documentation
* Correct version information
* Successful package building

Performance benchmarks can be run separately when relevant.

---

## Summary

The OQubit test suite provides a way to verify that changes do not break existing functionality.

The basic commands are:

```powershell
# Run all tests
pytest

# Run tests with detailed output
pytest -v

# Run one test file
pytest tests/test_example.py
```

As OQubit develops, the test suite should grow alongside the library and cover both core functionality and higher-level quantum algorithms.