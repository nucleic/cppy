Cppy Release Notes
==================

1.3.0 - 26/11/2024
------------------
- prevent liinking dynamically to MSVCP on windows

1.2.1 - 03/30/2022
------------------
- make the pyproject.toml fully PEP 621 compliant PR #19

1.2.0 - 03/11/2022
------------------
- expose a build_ext subclass that can be re-used in other projects PR #16
- use a PEP 517 compatible install procedure PR #16
- do not access directly ob_type on PyObject use Py_TYPE

1.1.0 - 06/25/2020
------------------
- drop Python 2 support PR #3
- add documentation and tests PR #3
- add cast_py_tp_doc to cast "cleanly" to void* for use in PyType_Slot

1.0.2 - 09/28/2014
------------------
- update license header

1.0.1 - 09/28/2014
------------------
- fix Python 3 int check

1.0.0 - 09/24/2014
------------------
- first release
