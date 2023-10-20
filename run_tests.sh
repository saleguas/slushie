#!/bin/bash

# Activate virtual environment if exists
if [ -d "venv" ]; then
    source venv/bin/activate
fi

# Install the package in editable mode
pip install -e .

# Run pytest to execute tests
pytest

# Deactivate virtual environment if exists
if [ -d "venv" ]; then
    deactivate
fi
