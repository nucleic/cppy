#------------------------------------------------------------------------------
# Copyright (c) 2014-2019, Nucleic
#
# Distributed under the terms of the BSD 3-Clause License.
#
# The full license is in the file LICENSE, distributed with this software.
#------------------------------------------------------------------------------
"""Test getting the include directory.

"""

def test_getting_include_directory():
    """Test getting the include directory.

    """
    from cppy import get_include
    assert get_include()
