import os, sys
import pytest

# This line is incredibly ironic and also the reason why this library exists lmao
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'slushie')))

from slushie import sip, gulp, pour, melt, slurp, scoop, freeze

def test_sip():
    # Test if sip() returns the correct absolute path
    assert os.path.isabs(sip('test'))

def test_gulp():
    # Test if gulp() correctly modifies sys.path
    directory = 'test_directory'
    with gulp(directory):
        assert any(directory in path for path in sys.path)

def test_freeze():
    # Test if freeze() correctly modifies sys.path
    freeze('test_directory')
    assert any('test_directory' in path for path in sys.path)

def test_pour():
    # Test if pour() returns the correct current and parent directories
    with pour('test_directory') as (current_dir, parent_dir):
        assert current_dir.endswith('test_directory')
        assert os.path.basename(parent_dir) != 'test_directory'

def test_melt():
    # Test if melt() returns the directory of the calling function/script
    def test_function():
        return melt()
    assert test_function() == os.path.dirname(__file__)

def test_slurp():
    # Test if slurp() returns the current working directory
    assert slurp() == os.getcwd()

def test_scoop(tmp_path):
    # Test if scoop() correctly opens and writes to a file
    file_path = tmp_path / "test.txt"
    with scoop(file_path, 'w') as file:
        file.write('Hello, Slushie!')
    with open(file_path, 'r') as file:
        assert file.read() == 'Hello, Slushie!'
    with scoop(file_path, 'a') as file:
        file.write(' Hello, World!')
    with open(file_path, 'r') as file:
        assert file.read() == 'Hello, Slushie! Hello, World!'
    # test encoding
    with scoop(file_path, 'w', encoding='utf-8') as file:
        file.write('Hello, Slushie!')
    with open(file_path, 'r', encoding='utf-8') as file:
        assert file.read() == 'Hello, Slushie!'
