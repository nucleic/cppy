Error reporting
===============

In addition to `cppy::ptr`, cppy provides a set a convenience function for
reporting errors which all return a NULL pointer allowing them to be used as
follows:

.. code:: c++

    PyObject* function( PyObject* obj )
    {
        cppy::ptr obj_ptr( cppy::incref( obj ) );
        if( !obj_ptr.is_bool() )
            return type_error( obj_ptr.get(), 'bool' )
        return obj_ptr.get()
    }

Functions
---------

Functions taking two arguments provide sensible pre-formated error messages.

.. code:: c++

    inline PyObject* system_error( const char* message )

    inline PyObject* type_error( const char* message )

    inline PyObject* type_error( PyObject* ob, const char* expected )

    inline PyObject* value_error( const char* message )

    inline PyObject* runtime_error( const char* message )

    inline PyObject* attribute_error( const char* message )

    inline PyObject* attribute_error( PyObject* ob, const char* attr )
