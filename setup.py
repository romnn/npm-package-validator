#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

import os
from setuptools import find_packages, setup

current = os.path.dirname(os.path.realpath(__file__))

short_description = "No description has been added so far."

version = "1.0.3"

with open(os.path.join(current, "README.rst")) as readme_file:
    long_description = readme_file.read()

requirements = ["Click>=6.0"]
test_requirements = [
    "tox",
    "pytest",
    "pytest-cov",
    "pytest-xdist",
    "pytest-sugar",
    "mypy",
    "pyfakefs",
]
coverage_requirements = ["coverage", "codecov"]
docs_requirements = ["sphinx>=2.0", "romnn_sphinx_press_theme", "sphinxemoji"]
formatting_requirements = ["flake8", "black==19.10b0", "isort"]
tool_requirements = [
    "m2r",
    "twine",
    "invoke",
    "ruamel.yaml",
    "pre-commit",
    "cookiecutter",
    "bump2version",
]
dev_requirements = (
    requirements
    + test_requirements
    + coverage_requirements
    + docs_requirements
    + formatting_requirements
    + tool_requirements
)

setup(
    author="romnn",
    author_email="contact@romnn.com",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Environment :: Console",
        "Operating System :: OS Independent",
        "Natural Language :: English",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    entry_points={
        "console_scripts": [
            "npm_package_validator=npm_package_validator.cli:main"
        ]
    },
    python_requires=">=3.6",
    install_requires=requirements,
    setup_requires=tool_requirements,
    tests_require=test_requirements,
    extras_require=dict(
        dev=dev_requirements, docs=docs_requirements, test=test_requirements
    ),
    license="MIT",
    description=short_description,
    long_description=long_description,
    include_package_data=True,
    package_data={"npm_package_validator": []},
    keywords="npm_package_validator",
    name="npm_package_validator",
    packages=find_packages(include=["npm_package_validator"]),
    test_suite="tests",
    url="https://github.com/romnn/npm-package-validator",
    version=version,
    zip_safe=False,
)
