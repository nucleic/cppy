#------------------------------------------------------------------------------
# Copyright (c) 2014, Nucleic Development Team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file COPYING.txt, distributed with this software.
#------------------------------------------------------------------------------
__major_version__ = 1
__minor_version__ = 0
__patch_version__ = 1


__version_info__ = (__major_version__, __minor_version__, __patch_version__)


__version__ = '%s.%s.%s' % __version_info__


def get_include():
    import os
    return os.path.join(os.path.dirname(__file__), 'include')
