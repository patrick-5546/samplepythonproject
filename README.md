# samplepythonproject

| | |
| --- | --- |
| CI/CD | [![CI - Test](https://github.com/patrick-5546/samplepythonproject/actions/workflows/test.yml/badge.svg)](https://github.com/patrick-5546/samplepythonproject/actions/workflows/test.yml) [![CD - Build](https://github.com/patrick-5546/samplepythonproject/actions/workflows/build.yml/badge.svg)](https://github.com/patrick-5546/samplepythonproject/actions/workflows/build.yml) |
| Package | [![PyPI - Version](https://img.shields.io/pypi/v/samplepythonproject.svg?logo=pypi&label=PyPI&logoColor=gold)](https://pypi.org/project/samplepythonproject/) [![PyPI - Python Version](https://img.shields.io/pypi/pyversions/samplepythonproject.svg?logo=python&label=Python&logoColor=gold)](https://pypi.org/project/samplepythonproject/) |
| Meta | [![Hatch project](https://img.shields.io/badge/%F0%9F%A5%9A-Hatch-4051b5.svg)](https://github.com/pypa/hatch) [![code style - black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black) [![types - Mypy](https://img.shields.io/badge/types-Mypy-blue.svg)](https://github.com/ambv/black) [![License - MIT](https://img.shields.io/badge/license-MIT-9400d3.svg)](https://spdx.org/licenses/) |

-----

## Installation

```console
pip install samplepythonproject
```

## Version source

- The [hatch-vcs](https://github.com/ofek/hatch-vcs) version source plugin determines the project version using Git tags

## Environments

- Defined neatly in a standalone [`hatch.toml`](https://hatch.pypa.io/latest/intro/#configuration)
- The `test` matrix uses the [hatch-containers](https://github.com/ofek/hatch-containers) plugin to run each environment inside Docker containers; usage can be seen in the [test](.github/workflows/test.yml) GitHub workflow

## Build

- All build targets use the [hatch-vcs](https://github.com/ofek/hatch-vcs) build hook plugin to ship a `_version.py` file so the version can be used at runtime
- Wheels use the [hatch-mypyc](https://github.com/ofek/hatch-mypyc) build hook plugin to first compile all code with [Mypyc](https://github.com/mypyc/mypyc)
- The [build](.github/workflows/build.yml) GitHub workflow shows how to use [cibuildwheel](https://github.com/pypa/cibuildwheel) to distribute binary wheels for every platform

## License

`samplepythonproject` is distributed under the terms of the [MIT](https://spdx.org/licenses/MIT.html) license.
