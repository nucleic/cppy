Cppy smart pointer
==================

CPython relies on reference counting to manage object lifetime. A large pitfall
when writing C-extension is to properly handle increfing and decrefing the
reference count. Cppy aims at simplifying this process by providing a smart
pointer class. Before diving into the details of it helps lets start a CPython
reference counting crash-course.

CPython reference counting crash course
---------------------------------------

Each object allocated by Python has a reference count, indicating how many
times this object is 'used'. When the reference count of an object goes to
zero, it is de-allocated. Outside of C extension, one does not need to manage
the reference count manually.

When a function part of Python C-API returns a Python object, it returns a
pointer to it. At the time at which the function returns, the referenced
object is live and its reference count is above zero. Depending of the
function, you do not have the same responsibility with respect to that object
reference count:

- Owned references:
  Most functions return a `new` reference which means that you  are responsible
  for decrefing the object reference count when you are done with it (basically
  the function increfed the object reference count before returning).
  In this situation you own a reference.

- Borrowed reference:
  Some functions (`PyList_GetItem`, `PyTuple_GetItem`) do not incref the object
  count before returning. In that case, you have only a borrowed reference, you
  are not responsible for decrefing the object reference count.

Borrowed references allow to avoid the cost of increfing/decrefing which is
nice. However since you do not own the reference, if the object referenced is
removed from its owner (list, tuple for the above two mentioned functions) it
may just disappear and your reference becomes invalid. This can cause issues.
If the object should outlive the container, or the time it will spend in the
container you have to incref it manually. Lets now discuss the convention when
calling a function.

When calling a function, the caller is expected to own a reference to each of
the arguments passed to the callee. The callee does not own the references, it
only borrows them. As a consequence, it should not decref the reference and if
it needs to store the object, in for example a C structure, it should incref
it. Note that this does not apply in general to Python container since those
are manipulated using functions that take care of it. There are however some
exceptions that steals a reference, meaning that you are not the owner of the
reference after the call. `PyList_SetItem`, for example, steal references.

An easy way to get reference count wrong is forgetting to decref some
intermediate object before leaving a function. This is particularly true if the
function has some early exit point because an exception should be raised. A
good practice is to have a single exit point, however it is not always
possible/practical and even like this it is possible to miss references, this
is typically where cppy can help.

This is a very brief introduction to reference counting. You can read a bit
more in the official `Python documentation`_ and in the `Python API`_
documentation.

.. _Python documentation: https://docs.python.org/3/c-api/intro.html#objects-types-and-reference-counts

.. _Python API: https://docs.python.org/3/c-api/refcounting.html

Cppy smart pointer class
------------------------

Cppy smart pointer (`cppy::ptr`) can be initialized with a pointer to a Python
object as follows:

.. code:: c++

    cppy::ptr obj_ptr( PyUnicode_FromString("test") )

When created, the class assume that you own the reference, if it is not the
case you should incref it first:

.. code:: c++

    PyObject* function( PyObject* obj )
    {
        cppy::ptr obj_ptr( cppy::incref( obj ) );
        cppy::ptr obj_ptr2( obj, true );
    }

.. note::

    Cppy provides convenient inline function for common reference manipulation:
    - `cppy::incref`, `cppy::xincref`, `cppy::decref`, `cppy::xdecref` use the
    the similarly named Python macros and return the input value.
    - `cppy::clear`, `cppy::replace` are similar but return void.

You can also initialize a `cppy::ptr` from another `cppy::ptr` in which case
the reference count will always be incremented.

The main advantage provided by `cppy::ptr` is that it implements a destructor
that will be invoked automatically by the c++ runtime when the `cppy::ptr`
goes out of scope. The destructor will decref the reference for you. As a
consequence you can be sure that your reference you always be decremented when
you leave the function.

Sometimes, however, that is not what you want, because you want to return the
reference the `cppy::ptr` manage. You can request the `cppy::ptr` to give back
the reference using its `release` method. Lets illustrate on a tiny example:

.. code:: c++

    PyObject* function( PyObject* obj )
    {
        cppy::ptr repr_ptr( PyObject_Repr( obj ) );
        return repr_ptr.release();
    }

Function which are part of Python C-API are not aware of of `cppy::ptr` and
when calling them you need to provide the original `PyObject*`. To access, you
simply need to call the `get` method of the `cppy::ptr` object.

.. code:: c++

    PyObject* function( PyObject* obj )
    {
        cppy::ptr l_ptr( PyList_New() );
        if( PyList_Append( l_ptr.get(), obj ) != 0 )
            return 0;
        return l_ptr.release();
    }

Here we see that because we use `cppy::ptr` to manage the list, we do not have
to worry about decrefing the reference if an exception occurs, the runtime
will do it for us. If no exception occurs, we stop managing the reference and
we are good.

Using cppy does not eliminate all the pitfalls of writing C-extensions. For
example if you release too early (for example when passing the object to a
function that may fail), you can still leak references. However it does
alleviate some of the complexity.

Cppy::ptr methods
-----------------

All methods that takes a `PyObject*` can also accept a `cppy::ptr`.
Most names should be self-explanatory, and apart from the is\_ methods most of
them rely on the PyObject\_ functions similarly named:

.. code:: c++

    bool is_none() const
    bool is_true() const
    bool is_false() const
    bool is_bool() const
    bool is_int() const
    bool is_float() const
    bool is_list() const
    bool is_dict() const
    bool is_set() const
    bool is_bytes() const
    bool is_str() const
    bool is_unicode() const
    bool is_callable() const
    bool is_iter() const
    bool is_type( PyTypeObject* cls ) const
    int is_truthy() const
    int is_instance( PyObject* cls ) const
    int is_subclass( PyObject* cls ) const
    PyObject* iter() const
    PyObject* next() const
    PyObject* repr() const
    PyObject* str() const
    PyObject* bytes() const
    PyObject* unicode() const
    Py_ssize_t length() const
    PyTypeObject* type() const
    int richcmp( PyObject* other, int opid ) const
    long hash() const
    bool hasattr( PyObject* attr ) const
    bool hasattr( const char* attr ) const
    bool hasattr( const std::string& attr ) const
    PyObject* getattr( PyObject* attr ) const
    PyObject* getattr( const char* attr ) const
    PyObject* getattr( const std::string& attr ) const
    bool setattr( PyObject* attr, PyObject* value ) const
    bool setattr( const char* attr, PyObject* value ) const
    bool setattr( const std::string& attr, PyObject* value ) const
    bool delattr( PyObject* attr ) const
    bool delattr( const char* attr ) const
    bool delattr( const std::string& attr ) const
    PyObject* getitem( PyObject* key ) const
    bool setitem( PyObject* key, PyObject* value ) const
    bool delitem( PyObject* key )
    PyObject* call( PyObject* args, PyObject* kwargs = 0 ) const
