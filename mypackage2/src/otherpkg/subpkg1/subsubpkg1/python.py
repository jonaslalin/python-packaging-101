import sys


def python_version() -> str:
    if sys.version_info >= (3, 10):
        return "Python version >= 3.10"
    if sys.version_info >= (3, 9):
        return "Python version >= 3.9"
    if sys.version_info >= (3, 8):
        return "Python version >= 3.8"
    return "Python version < 3.8"
