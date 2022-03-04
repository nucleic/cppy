# ------------------------------------------------------------------------------
# Copyright (c) 2014-2022, Nucleic
#
# Distributed under the terms of the BSD 3-Clause License.
#
# The full license is in the file LICENSE, distributed with this software.
# ------------------------------------------------------------------------------
from setuptools import setup

setup(
    name="cppy",
    author="The Nucleic Development Team",
    author_email="sccolbert@gmail.com",
    maintainer_email="m.dartiailh@gmail.com",
    url="https://github.com/nucleic/cppy",
    description="C++ headers for C extension development",
    long_description=open("README.rst").read(),
    packages=["cppy"],
    package_data={"cppy": ["include/cppy/*.h"]},
)
