from setuptools import setup, find_packages
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent
with open("README.md","r") as f:
    description = f.read()
setup(
    name='oqubit',
    version='0.1',
    install_requires=["numpy>=2.0"],
     package_dir={
        "": str(BASE_DIR / "src")
    },

    packages=find_packages(
        where=str(BASE_DIR / "src")
    ),
    python_requires=">=3.9",
    long_description=description,
    long_description_content_type="text/markdown",
)