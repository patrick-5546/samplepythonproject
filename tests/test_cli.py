# SPDX-FileCopyrightText: 2021-present Ofek Lev <oss@ofek.dev>
#
# SPDX-License-Identifier: MIT


def test(samplepythonproject):
    result = samplepythonproject("fib", "32")

    assert result.exit_code == 0, result.output
    assert result.output == "2178309\n"
