#------------------------------------------------------------------------------
# Copyright (c) 2014-2022, Nucleic Development Team.
#
# Distributed under the terms of the BSD 3-Clause License.
#
# The full license is in the file LICENSE, distributed with this software.
# --------------------------------------------------------------------------------------
import os
import sys

from setuptools.command.build_ext import build_ext

from .version import __version__, __version_info__


def get_include():
    import os
    return os.path.join(os.path.dirname(__file__), 'include')
