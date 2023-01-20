from setuptools import find_packages, setup
from pathlib import Path


def _open_readme(file_path: str) -> str:
    with open(Path(".", file_path), encoding="utf-8") as f:
        return f.read()


setup(
    name="playground-notebooks",
    description="Collection of notebooks for trying out tools and python  packages",
    long_description=_open_readme("README.md"),
    install_requires=["qdrant_client", "sentence_transformers", "jupyter-notebook"],
    python_requires=">=3.7",
)
