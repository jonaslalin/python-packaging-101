def greeting(name: str) -> str:
    return "Hello " + name


# def contains_type_error() -> str:
#     import sys

#     if sys.version_info >= (3, 10):
#         return greeting(123)
#     elif sys.version_info >= (3, 9):
#         return greeting(b"Alice")
#     elif sys.version_info >= (3, 8):  # noqa: UP036
#         return greeting("Bob")
#     else:
#         return greeting(True)
