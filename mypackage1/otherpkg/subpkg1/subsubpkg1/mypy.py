def greeting(name: str) -> str:
    return "Hello " + name


# def contains_type_error() -> str:
#     import sys

#     if sys.version_info >= (3, 10):
#         return greeting(123)
#     if sys.version_info >= (3, 9):
#         return greeting(b"Alice")
#     if sys.version_info >= (3, 8):
#         return greeting("Bob")
#     return greeting(True)
