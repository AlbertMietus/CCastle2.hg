===============
RPY-Translators
===============

The rpy-translator module drives the (external) “translators” that read the generated files and compile/evaluate them.

There are several translators; see below for an overview.

.. _RPY_Eval:

Evaluate
--------
The generated (r)python files are run by cpython (the normal python). This is a quick check to evaluate the generated files are actual python.

Also, as it captures the output, a check on correctness is possible. Conceptual, that result should be the same as the output of :ref:`RPY_Exe`.

.. _RPY_Compile:

Compile
-------

Translate the rpython intermediate files into C, and compile into an excutable. This uses the rpython-translator.

This results in a binary/executable (which isn’t “run” -- See:  :ref:`RPY_Exe` for that)

.. _RPY_Exe:

Execute
-------

Execute the compiled executable, and capture the output. -- See :ref:`RPY_Compile` for how to make that executable.


