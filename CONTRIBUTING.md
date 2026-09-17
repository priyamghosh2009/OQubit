# Contributing to OQubit

Thank you for your interest in contributing to OQubit!

OQubit is an open-source quantum computing and simulation project. Contributions of all kinds are welcome.

## How to Contribute

You can contribute by:

* Reporting bugs
* Suggesting features
* Improving documentation
* Adding tests
* Improving examples
* Adding quantum algorithms or gates
* Fixing existing issues

## Getting Started

Clone the repository:

```bash
git clone https://github.com/priyamghosh2009/OQubit.git
cd OQubit
```

Create and activate a virtual environment, then install OQubit:

```bash
python -m pip install -e .
```

## Create a Branch

Please use a separate branch for your changes:

```bash
git switch -c feature/my-feature
```

Some examples:

```text
feature/qft
fix/statevector
docs/readme
test/gates
```

## Make Your Changes

Please:

* Keep your changes focused.
* Follow the existing code style.
* Add tests for new functionality when possible.
* Update documentation when needed.
* Avoid unnecessary dependencies.

## Run Tests

Before submitting your changes, run:

```bash
pytest
```

Make sure the tests pass.

## Pull Requests

When your changes are ready:

1. Push your branch to your fork.
2. Open a Pull Request against `main`.
3. Explain what you changed.
4. Mention how you tested it.

Please keep Pull Requests clear and focused.

## Commit Messages

Use short, descriptive commit messages.

Examples:

```text
feat: add QFT
fix: correct statevector operation
test: add gate tests
docs: update README
```

## Security Issues

Please **do not** report security vulnerabilities through public GitHub Issues or Pull Requests.

See [SECURITY.md](SECURITY.md) for information about privately reporting security issues.

## Code of Conduct

Please read and follow the [Code of Conduct](CODE_OF_CONDUCT.md) when participating in the project.

## Thank You

Thank you for helping improve OQubit!
