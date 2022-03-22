Installation and use with setuptools
====================================

Since Cppy is nothing else than a collection of header that are only compiled
when used, installing it is extremely straightforward using pip::

    $ pip install cppy

If you want to run the development version, you can install directly from
GitHub::

    $ pip install git+https://github.com/nucleic/cppy


Using Cppy in an extensions
---------------------------

To use Cppy in your extension (written in C++), you simply need to include it.

.. code:: c++

    #include <cppy/cppy.h>

Cppy includes Python.h so when including cppy.h you do not need to also include
Python.h.

Every functions, classes exposed by Cppy are stored in the `cppy` namespace.

.. code:: c++

    cppy::ptr obj_ptr( PyUnicode_FromString("test") )


Use with setuptools
-------------------

Cppy is only needed during the installation step of the projects using it.

When using a PEP 517 compatible build system, one can simply specify cppy as a
build requirement in ```pyproject.toml``::

    [build-system]
    requires =  ["setuptools>=42", "wheel", "cppy>=1.2"]

Which will ensure that cppy is available in setup.py allowing to import it at the
top level of the module. This allows in particular to import ``CppyBuildExt``
which enforces the use of C++11 and provide access to the cppy headers. On Windows,
FH4 Exception Handling can be disabled by setting the CPPY_DISABLE_FH4 environment
variable. This avoids requiring VCRUNTIME140_1.dll

In one is not using a PEP 517 compatible install, the following example setup.py
script illustrates how to use Cppy without requiring it to be installed before
`setup.py` is run.

.. code:: python

    from setuptools import setup, Extension
    from setuptools.command.build_ext import build_ext

    ext_modules = [
        Extension(
            'project',
            ['module.cpp'],
            include_dirs=['.'],
            language='c++',
        ),
    ]

    class BuildExt(build_ext):

        def build_extensions(self):

            # Delayed import of cppy to let setup_requires install it if
            # necessary
            import cppy

            ct = self.compiler.compiler_type
            for ext in self.extensions:
                # cppy.get_include() collect the path of the header files
                ext.include_dirs.insert(0, cppy.get_include())
            build_ext.build_extensions(self)

    setup(
        name='project',
        python_requires='>=3.5',
        setup_requires=['cppy'],
        ext_modules=ext_modules,
        cmdclass={'build_ext': BuildExt},
    )
