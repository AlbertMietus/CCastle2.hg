# (C) Albert Mietus, 2025. Part of Castle/CCastle project
# This is RPYthon code!

"""Argument-value wrappers for the ``*t, **kw``-style calling convention.

In RPy, using the NativeBundler, we pack/unpack arguments into `CC_B_Value` objects which then
is packed into an "arglist" (for positional-parameters) and a dict (for named-parameters)

Each ``CC_B_*`` class wraps a single Castle primitive value into the ``.__value`` field of the subclass named to the
(Castle) type. That value is also "casted" (aka converted) to that type. This ensures that pypy's annotator will always
find the correct form. Typically, the pypy/rpython translater will optimize that "extra call".

Even though every value is stored in ``.__value``; we can't unpack it directly -- rpython can't handle that (python does)
To help pypy's translator, we use *staticmethod* ``unbox(self)`` -- not a classmethod

This set of classes will be extended when more Castle types/primitives a added.
And it MUST be kept in sync with ``PortrayType``(s) in the writer.

Note, we use `.__value` now (not the old .value), so that we force to use unbox()

.. hint:: Template

   All CC_B_Value subtypes are almost the same. Use the following "template" and change $T to the (python) type

   .. code-block:: python

      class CC_B_$T(CC_B_Value):
          def __init__(self, v):
              self.__value = $T(v)

          @staticmethod
          def unbox(self):
              if isinstance(self, CC_B_$T):
                  return self.__value
              raise TypeError("unbox: expected CC_B_$T")

.. warning::

   RPython supports polymorphic methods, but not polymorphic attributes.

.. note:: CC_B_Component

  ``CC_B_Component`` is in line with this; it's the type of an element

   .. todo: fix that detail
"""


class CC_B_Value:
    """Base class for all argument-value wrappers.
        Never instantiate directly -- use a concrete subclass like ``CC_B_int``."""

    def __init__(self, v): pass # Box it
    @staticmethod
    def unbox(self): pass

class CC_B_int(CC_B_Value):
    def __init__(self, v):
        self.__value = int(v)

    @staticmethod
    def unbox(self):
        if isinstance(self, CC_B_int):
            return self.__value
        raise TypeError("unbox: expected CC_B_int")

class CC_B_float(CC_B_Value):
    def __init__(self, v):
        self.__value = float(v)

    @staticmethod
    def unbox(self):
        if isinstance(self, CC_B_float):
            return self.__value
        raise TypeError("unbox: expected CC_B_float")

class CC_B_string(CC_B_Value):
    def __init__(self, v):
        self.__value = str(v)

    @staticmethod
    def unbox(self):
        if isinstance(self, CC_B_string):
            return self.__value
        raise TypeError("unbox: expected CC_B_string")

class CC_B_boolean(CC_B_Value):
    def __init__(self, v):
        self.__value = bool(v)

    @staticmethod
    def unbox(self):
        if isinstance(self, CC_B_boolean):
            return self.__value
        raise TypeError("unbox: expected CC_B_boolean")
