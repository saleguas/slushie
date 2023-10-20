import os
import sys
from contextlib import contextmanager
from typing import Tuple, Iterator, Any, TextIO, Optional

def sip(*parts: str) -> str:
    """
    Get the absolute path relative to the current script's directory.
    
    :param parts: Parts of the path to join.
    :return: Absolute path.
    """
    return os.path.abspath(os.path.join(os.path.dirname(__file__), *parts))

@contextmanager
def gulp(directory: str = '.') -> Iterator[None]:
    """
    Context manager to temporarily add all subdirectories of a directory to sys.path.
    
    :param directory: Directory to add subdirectories from.
    """
    old_path = sys.path.copy()
    for root, dirs, files in os.walk(directory):
        sys.path.append(root)
    yield
    sys.path = old_path

def freeze(path: str) -> None:
    """
    Append a specific path to sys.path.
    
    :param path: Path to append to sys.path.
    """
    sys.path.append(sip(path))

@contextmanager
def pour(directory: str = '.') -> Iterator[Tuple[str, str]]:
    """
    Context manager to get the current and parent directory paths.
    
    :param directory: Directory to get paths for.
    :return: Current and parent directory paths.
    """
    current_dir = os.path.abspath(directory)
    parent_dir = os.path.abspath(os.path.join(directory, '..'))
    yield current_dir, parent_dir

def melt() -> str:
    """
    Get the directory of the calling script.
    
    :return: Directory of the calling script.
    """
    import inspect
    caller_frame = inspect.stack()[1]
    caller_path = os.path.dirname(os.path.abspath(caller_frame.filename))
    return caller_path

def slurp() -> str:
    """
    Get the directory where the terminal command is executed.
    
    :return: Directory where the terminal command is executed.
    """
    return os.getcwd()


def scoop(file: str, mode: str = 'r', buffering: Optional[int] = -1, 
          encoding: Optional[str] = None, errors: Optional[str] = None, 
          newline: Optional[str] = None, closefd: bool = True, 
          opener: Optional[Any] = None) -> TextIO:
    """
    Shortcut to open a file with a path relative to the current script's directory.
    
    :param file: File path relative to the current script's directory.
    :param mode: Mode in which the file is opened.
    :param buffering: Buffering policy.
    :param encoding: Encoding format.
    :param errors: Specifies how encoding and decoding errors are to be handled.
    :param newline: Controls how universal newlines mode works.
    :param closefd: If closefd is False and a file descriptor rather than a filename is given, 
                    the underlying file descriptor will be kept open when the file is closed.
    :param opener: A custom opener.
    :return: File object.
    """
    file_path = sip(file)
    return open(file_path, mode, buffering, encoding, errors, newline, closefd, opener)

