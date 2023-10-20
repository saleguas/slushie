# Slushie 🍧

Welcome to Slushie, an intuitive solution to Python's relative path disaster. 🍭 Ever wanted to just get a file from a sibling or parent directory without pulling your hair out? Slushie is the perfect "it just works" solution to all your path management problems. 🍦

## Table of Contents

- [🚀 Installation](#-installation)
- [🌈 Usage](#-usage)
- [🔬 Running Tests](#-running-tests)
- [🤝 Contributing](#-contributing)
- [📜 License](#-license)

## 🚀 Installation

Slushie is ready to chill in your project. Install it directly from PyPI:

```
pip install slushie
```

## 🌈 Usage

Slurp in the delightful functionalities of Slushie:

### sip(*parts: str) -> str

**Purpose**: Create absolute paths relative to the current script. Ideal for accessing files in parent or sibling directories without a fuss.

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
```

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

**Purpose**: Easily access the current and parent directory paths.

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
with scoop('data.txt', 'r') as file:
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
