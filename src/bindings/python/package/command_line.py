# SPDX-License-Identifier: BSD-3-Clause
# Copyright Contributors to the OpenColorIO Project.

import os
import subprocess
import sys


BIN_DIR = os.path.join(os.path.dirname(__file__), 'bin')


def call_program(name, args):
    return subprocess.call([os.path.join(BIN_DIR, name)] + args)


def main():
    name = os.path.basename(sys.argv[0])
    raise SystemExit(call_program(name, sys.argv[1:]))
