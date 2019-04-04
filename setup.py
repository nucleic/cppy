#------------------------------------------------------------------------------
# Copyright (c) 2014-2019, Nucleic
#
# Distributed under the terms of the BSD 3-Clause License.
#
# The full license is in the file LICENSE, distributed with this software.
#------------------------------------------------------------------------------
from setuptools.core import setup

# Before releasing the version needs to be updated here and in
# docs/source/conf.py

setup(
    name='cppy',
    version='1.1.0',
    author='The Nucleic Development Team',
    author_email='sccolbert@gmail.com',
    url='https://github.com/nucleic/cppy',
    description='C++ headers for C extension development',
    long_description=open('README.md').read(),
    packages=['cppy'],
    package_data={'cppy': ['include/cppy/*.h']},
)
