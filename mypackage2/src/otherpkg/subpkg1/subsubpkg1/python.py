import sys


def python_version() -> str:
    if sys.version_info >= (3, 10):
        return "Python version >= 3.10"
    elif sys.version_info >= (3, 9):
        return "Python version >= 3.9"
    elif sys.version_info >= (3, 8):  # noqa: UP036
        return "Python version >= 3.8"
    else:
        return "Python version < 3.8"
