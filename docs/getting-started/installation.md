# Installation

This guide explains how to install **OQubit** and verify that the installation is working correctly.

## Requirements

OQubit requires:

* Python 3.9 or newer
* `pip`

You can check your Python version with:

```bash
python --version
```

On some systems, you may need:

```bash
python3 --version
```

## Install from PyPI

The recommended way to install OQubit is through PyPI:

```bash
pip install oqubit
```

To install a specific version:

```bash
pip install oqubit==0.1.0
```

## Verify the Installation

After installation, open Python and import OQubit:

```python
import oqubit

print(oqubit)
```

You can also check the installed package version:

```python
import importlib.metadata

print(importlib.metadata.version("oqubit"))
```

## Install from Source

If you want to work with the OQubit source code, clone the repository:

```bash
git clone https://github.com/priyamghosh2009/OQubit.git
cd OQubit
```

Then install OQubit in editable mode:

```bash
pip install -e .
```

Editable installation is useful for development because changes made to the source code are available without reinstalling the package.

## Recommended Virtual Environment

Using a virtual environment helps keep OQubit and its dependencies separate from other Python projects.

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it on Windows:

```powershell
.venv\Scripts\Activate.ps1
```

Activate it on Linux or macOS:

```bash
source .venv/bin/activate
```

Then install OQubit:

```bash
pip install -e .
```

## Installing Development Dependencies

When developing OQubit, install the project's development dependencies if they are provided by the repository:

```bash
pip install -e ".[dev]"
```

This can provide tools used for testing, benchmarking, and development.

## Troubleshooting

### `pip` is not recognized

Try invoking pip through Python:

```bash
python -m pip install oqubit
```

### Multiple Python installations

If the wrong Python installation is being used, check:

```bash
python --version
python -m pip --version
```

This helps verify that `pip` belongs to the Python interpreter you intend to use.

### Installation from source fails

Make sure you are running the command from the OQubit repository root, where the project's packaging configuration is located.

## Next Step

Once OQubit is installed, continue with the [Quickstart](quickstart.md) guide to create your first quantum state and circuit.