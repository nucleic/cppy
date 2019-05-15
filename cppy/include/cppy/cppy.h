/*-----------------------------------------------------------------------------
| Copyright (c) 2014, Nucleic
|
| Distributed under the terms of the BSD 3-Clause License.
|
| The full license is in the file LICENSE, distributed with this software.
|----------------------------------------------------------------------------*/
#pragma once

#define pyobject_cast( o ) ( reinterpret_cast<PyObject*>( o ) )
#define pytype_cast( o ) ( reinterpret_cast<PyTypeObject*>( o ) )
#define void_cast( o ) ( reinterpret_cast<void*>( o ) )

#include "defines.h"
#include "errors.h"
#include "ptr.h"
