# Slushie 🍧

🍭 Ever wanted to just get a file from a sibling or parent directory without pulling your hair out? Slushie is the perfect "it just works" solution to relative paths in Python.

<!-- include media/slushie.gif -->

![Slushie Demo](media/slushie.gif)

## Table of Contents

- [❔ Why Slushie?](#-why-slushie)
- [🚀 Installation](#-installation)
- [🌈 Usage](#-usage)
- [🔬 Running Tests](#-running-tests)
- [🤝 Contributing](#-contributing)
- [📜 License](#-license)

## ❔ Why Slushie?

Relative paths and imports in Python are an absolute nightmare due to how `PYTHONPATH` works and finds modules.

For example, 
```
project_root/
│   main.py
│
├───package1/
│   │   module1.py
│   │   file.csv
│   │
│   └───subpackage1/
│       │   module2.py
```

If I wanted to import `module1.py` from `main.py`, you'd think it would be something like the following:

```
from package1 import module1
from package1.subpackage1 import module2
```

<!-- bold -->

**This (most likely) will not work. Why?**

Python relies on the dreaded `PYTHONPATH` environment variable to determine where to look for modules to import. 

`PYTHONPATH` is a list of directories that Python checks whenever you attempt an import. If `package1` and `subpackage1` are not included in the `PYTHONPATH`, Python doesn’t know where to look for `module1.py`, and `module2.py`, resulting in an `ImportError`.

Additionally, attempting to open `file.csv`, using the traditional open command like this:

```
open("package1/file.csv")
```

will most likely not even find the file, and even if it does, there's a high chance it will break if it is ever moved to another machine or ran from a different directory.

This is because the search for `file.csv` is relative to the current working directory where the Python script is executed, not necessarily where main.py is located.

**TL;DR: If you use python's default import and open commands, you either have to do some Python witchcraft or risk randomly breaking your code.**

## 🚀 Installation

Install it directly from PyPI:

```
pip install slushie
```

## 🌈 Usage


### sip(*parts: str) -> str

**Purpose**: Create absolute paths relative to the current FILE. Ideal for accessing files in parent or sibling directories without a fuss.

#### Parameters:
- `*parts: str` - Parts of the path to join.

#### Usage:
Access `hello.txt` located in a sibling directory from `script.py`.

```
/project
    /folder1
        script.py
    /folder2
        hello.txt
```

```python
path = sip('..', 'folder2', 'hello.txt')
print(path)

# Output:
# /path/to/project/folder2/hello.txt
# In this case, sip('.') refers to /path/to/project/folder1/
```

The above code is fundamentally equivalent to the following:

```python
import os
import sys

path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'folder2', 'hello.txt')
print(path)

# Output:
# /path/to/project/folder2/hello.txt
```

This is extremely useful, as if you ever need to open a file, such as a csv for data analysis or a text file for logging, you should almost always be using relative paths as to avoid breaking your code when you move it to a different machine or share it with someone else. Slushie makes this easy.

```python
### gulp(directory: str = '.') -> Iterator[None]

**Purpose**: Temporarily include directories in the Python path, easing the import of modules/packages.

#### Parameters:
- `directory: str` - Directory to add directories from.

#### Usage:
Import a module from a sibling directory.

```python
with gulp('../sibling_directory'):
    import a_module_from_sibling_directory
```

### freeze(path: str) -> None

**Purpose**: Make a specific directory permanently available for imports.

#### Parameters:
- `path: str` - Path to append to `sys.path`.

#### Usage:
```python
freeze('../another_directory')
import a_module_from_another_directory
```

### pour(directory: str = '.') -> Iterator[Tuple[str, str]]

**Purpose**: Easily access the current and parent directory paths of the current file the code is being written in.

#### Parameters:
- `directory: str` - Directory to get paths for.

#### Usage:
```python
with pour() as (current_dir, parent_dir):
    print(f"Current Directory: {current_dir}")
    print(f"Parent Directory: {parent_dir}")
```

### melt() -> str

**Purpose**: Find the directory of the calling script, aiding in understanding the execution context.

#### Usage:
```python
caller_path = melt()
print(f"Caller Path: {caller_path}")

# Output:
# Caller Path: /path/to/calling/script.py
# This is the path of the script that called melt(), not the path of melt() itself.
# So if I had script /path/to/calling/script.py that called melt(), and melt() was located at /path/to/melt.py, the output would still be:
# Caller Path: /path/to/calling/script.py
```


### slurp() -> str

**Purpose**: Identify where the terminal command was executed from.

#### Usage:
```python
terminal_path = slurp()
print(f"Terminal Path: {terminal_path}")

# So if the script was located at /path/to/script.py and the terminal command was executed from /path/to, the output would be:
# Terminal Path: /path/to
```

### scoop(file: str, mode: str = 'r', ...) -> TextIO

**Purpose**: Simplify opening files by managing paths relative to the current script automatically.

#### Parameters:
Literally the same as the built-in `open()` function. It's just a wrapper around it that automatically manages paths relative to the current script.


#### Usage:
```python
with scoop('../data.txt', 'r') as file:
    data = file.read()
    print(data)
```

## 🔬 Running Tests

Keeping Slushie frosty with some cool tests:

- **For Linux:**
  ```
  ./run_tests.sh
  ```

- **For Windows:**
  ```
  run_tests.bat
  ```

## 🤝 Contributing

Contribute your own flavors to make Slushie even more delightful! 🌈

## 📜 License

Slushie is lovingly served under the MIT License. Scoop into the [LICENSE](LICENSE) file for the full details.
