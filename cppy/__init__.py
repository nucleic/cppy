#------------------------------------------------------------------------------
# Copyright (c) 2014-2020, Nucleic
#
# Distributed under the terms of the BSD 3-Clause License.
#
# The full license is in the file LICENSE, distributed with this software.
#------------------------------------------------------------------------------
__major_version__ = 1
__minor_version__ = 1
__patch_version__ = 0


__version_info__ = (__major_version__, __minor_version__, __patch_version__)


__version__ = '%s.%s.%s' % __version_info__


def get_include():
    import os
    return os.path.join(os.path.dirname(__file__), 'include')
