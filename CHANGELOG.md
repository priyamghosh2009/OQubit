# Changelog

All notable changes to OQubit are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/), and OQubit follows [Semantic Versioning](https://semver.org/).

## [0.1.0] - 2026-09-17

Initial release of OQubit.

### Added

* `Qubit` for representing single-qubit quantum states.
* `StateVector` for multi-qubit quantum states.
* Quantum operator and gate abstractions.
* Single-qubit, controlled, and multi-qubit gates.
* Quantum circuit construction with the `Circuit` API.
* Circuit instructions through the `Instruction` API.
* Quantum measurement and sampling utilities.
* Initial quantum algorithms package.
* Deutsch algorithm.
* Deutsch–Jozsa algorithm.
* Bernstein–Vazirani algorithm.
* Superdense Coding.
* Example notebooks demonstrating OQubit functionality.
* Unit tests for core components, gates, measurements, circuits, and algorithms.
* Initial benchmark suite.
* Project documentation.
* Contributing guidelines.
* Code of Conduct.
* Security Policy.
* `CITATION.cff`.
* Open-source project license.

### Project Structure

* Established the `src/oqubit` Python package layout.
* Organized the project into:

  * `core`
  * `gates`
  * `circuit`
  * `measurement`
  * `algorithms`
* Added dedicated `tests`, `benchmarks`, and `examples` directories.

[0.1.0]: https://github.com/priyamghosh2009/OQubit/releases/tag/v0.1.0