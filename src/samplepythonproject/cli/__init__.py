# SPDX-FileCopyrightText: 2023-present Patrick Creighton <pcreighton429@gmail.com>
#
# SPDX-License-Identifier: MIT
import click

from samplepythonproject._version import version
from samplepythonproject.fib import fibonacci

# NOTE: The group/command decorators must come last to avoid the following issue at
# runtime: https://github.com/pallets/click/issues/1199


@click.version_option(version=version, prog_name="samplepythonproject")
@click.group(
    context_settings={"help_option_names": ["-h", "--help"]},
    invoke_without_command=True,
)
def samplepythonproject():
    pass


@click.argument("n", type=int)
@samplepythonproject.command()
def fib(n: int):
    click.echo(fibonacci(n))
