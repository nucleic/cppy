#------------------------------------------------------------------------------
# Copyright (c) 2014, Nucleic Development Team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file COPYING.txt, distributed with this software.
#------------------------------------------------------------------------------
from distutils.core import setup


setup(
    name='cppy',
    version='1',
    author='The Nucleic Development Team',
    author_email='sccolbert@gmail.com',
    url='https://github.com/nucleic/cppy',
    description='C++ headers for C extension development',
    long_description=open('README.md').read(),
    packages=['cppy'],
    package_data={'cppy': ['include/cppy/*.h']},
)
