#! /bin/sh
python3 -m unittest
mypy complex_number/
flake8 tests/ complex_number/
