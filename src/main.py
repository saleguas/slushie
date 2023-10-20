import os
import sys
from contextlib import contextmanager

def sip(*parts):
    return os.path.abspath(os.path.join(os.path.dirname(__file__), *parts))

@contextmanager
def gulp(directory='.'):
    old_path = sys.path.copy()
    for root, dirs, files in os.walk(directory):
        sys.path.append(root)
    yield
    sys.path = old_path

def freeze(path: str):
    sys.path.append(sip(path))

@contextmanager
def pour(directory='.'):
    current_dir = os.path.abspath(directory)
    parent_dir = os.path.abspath(os.path.join(directory, '..'))
    yield current_dir, parent_dir

def melt():
    import inspect
    caller_frame = inspect.stack()[1]
    caller_path = os.path.dirname(os.path.abspath(caller_frame.filename))
    return caller_path

# Usage Examples

# 1. Using sip
print(sip('..', 'hello', 'hi'))

# 2. Using gulp
with gulp():
    # All subdirectories of current directory are temporarily in sys.path
    pass

# 3. Using freeze
freeze('../my_module')

# 4. Using pour
with pour() as (current_dir, parent_dir):
    print(f"Current Directory: {current_dir}")
    print(f"Parent Directory: {parent_dir}")

# 5. Using melt
caller_path = melt()
print(f"Caller Path: {caller_path}")
