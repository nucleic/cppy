Installation and use with setuptools
====================================

Since cppy is nothing else than a collection of header that are only compiled
when used, installing it is extremely straightforward using pip::

    $ pip install cppy

If you want to run the development version, you can install directly from
Github::

    $ pip install https://github.com/nucleic/cppy


Using cppy in an extensions
---------------------------

To use cppy in your extension (written in C++), you simply need to include it.

.. code:: c++

    #include <cppy/cppy.h>

Cppy includes Python.h so when including cppy.h you do not need to also include
Python.h.

Every functions, classes exposed by cppy are stored in the `cppy` namespace.

.. code:: c++

    cppy::ptr obj_ptr( PyUnicode_FromString("test") )


Use with setuptools
-------------------

Cppy is only needed during the installation step of the projects using it. The
following example setup.py script illustrates how to use cppy without requiring
it to be installed before `setup.py` is run.

.. code:: python

    from setuptools import setup, Extension
    from setuptools.command.build_ext import build_ext

    ext_modules = [
        Extension(
            'project',
            ['module.cpp],
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
