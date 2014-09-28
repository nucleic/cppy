/*-----------------------------------------------------------------------------
| Copyright (c) 2014, Nucleic
|
| Distributed under the terms of the BSD 3-Clause License.
|
| The full license is in the file LICENSE, distributed with this software.
|----------------------------------------------------------------------------*/
#pragma once

#include <Python.h>

#define CPPY_MAJOR_VERSION 1
#define CPPY_MINOR_VERSION 0
#define CPPY_PATCH_VERSION 2

#define CPPY_VERSION "1.0.2"

#if PY_MAJOR_VERSION >= 3
#define IS_PY3K
#endif
