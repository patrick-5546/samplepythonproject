# SPDX-FileCopyrightText: 2023-present Patrick Creighton <pcreighton429@gmail.com>
#
# SPDX-License-Identifier: MIT
import click

from samplepythonproject.__about__ import __version__


@click.group(context_settings={"help_option_names": ["-h", "--help"]}, invoke_without_command=True)
@click.version_option(version=__version__, prog_name="samplepythonproject")
def samplepythonproject():
    click.echo("Hello world!")
