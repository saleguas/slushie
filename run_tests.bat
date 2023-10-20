@echo off

REM Activate virtual environment if exists
if exist "venv" (
    .\venv\Scripts\activate
)

REM Install the package in editable mode
pip install -e .

REM Run pytest to execute tests
pytest

REM Deactivate virtual environment if exists
if exist "venv" (
    deactivate
)
