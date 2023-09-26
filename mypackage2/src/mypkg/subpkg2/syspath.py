import sys

if __name__ == "__main__":
    print("\n".join(repr(p) for p in sys.path))
