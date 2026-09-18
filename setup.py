from setuptools import setup, find_packages
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent
with open("README.md","r") as f:
    ldescription = f.read()
setup(
    name="oqubit",
    version="0.1.1",
    author="Priyam Ghosh",
    author_email="priyamghosh2009@outlook.com",
    description=(
        "An open-source Python framework for simulating quantum circuits, "
        "qubits, state vectors, quantum gates, measurements, and algorithms."
    ),
    install_requires=["numpy>=2.0",],
    package_dir={
        "": str(BASE_DIR / "src")
    },
    packages=find_packages(
        where=str(BASE_DIR / "src")
    ),
    python_requires=">=3.9",
    long_description=ldescription,
    long_description_content_type="text/markdown",
    keywords=[
        "quantum computing",
        "quantum simulator",
        "quantum simulation",
        "quantum circuits",
        "qubits",
        "quantum algorithms",
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: POSIX :: Linux",
        "Operating System :: MacOS",
        "Topic :: Scientific/Engineering",
        "Topic :: Scientific/Engineering :: Physics",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)