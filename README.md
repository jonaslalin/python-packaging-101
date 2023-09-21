# python-packaging-101

## Setup

```sh
python -m venv .venv
source .venv/bin/activate # or .venv\Scripts\activate for cmd.exe
pip install -r requirements-dev.txt
```

## Naming Conventions

### Distribution Package Name

> ```python
> name='sample',
> ```
>
> This is the name of your project, determining how your project is listed on PyPI. Per PEP 508, valid project names must:
>
> * Consist only of ASCII letters, digits, underscores (`_`), hyphens (`-`), and/or periods (`.`), and
> * Start & end with an ASCII letter or digit.
> 
> Comparison of project names is case insensitive and treats arbitrarily-long runs of underscores, hyphens, and/or periods as equal. For example, if you register a project named `cool-stuff`, users will be able to download it or declare a dependency on it using any of the following spellings:
>
> ```
> Cool-Stuff
> cool.stuff
> COOL_STUFF
> CoOl__-.-__sTuFF
> ```
>
> Source: https://packaging.python.org/en/latest/guides/distributing-packages-using-setuptools/#name

### Package and Module Names

> Modules should have short, all-lowercase names. Underscores can be used in the module name if it improves readability. Python packages should also have short, all-lowercase names, although the use of underscores is discouraged.
>
> When an extension module written in C or C++ has an accompanying Python module that provides a higher level (e.g. more object oriented) interface, the C/C++ module has a leading underscore (e.g. `_socket`).
>
> Source: https://peps.python.org/pep-0008/#package-and-module-names
