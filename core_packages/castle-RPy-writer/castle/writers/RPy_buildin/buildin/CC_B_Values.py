# (C) Albert Mietus, 2025. Part of Castle/CCastle project
# This is RPYthon code!

"""Argument-value wrappers for the ``*t, **kw``-style calling convention.

In RPy, using the NativeBundler, we pack/unpack arguments into `CC_B_Value` objects which then
is packed into an "arglist" (for positional-parameters) and a dict (for named-parameters)

Each ``CC_B_*`` class wraps a single Castle primitive value into the ``.value`` field of the subclass named to the
(Castle) type. That value is also "casted" (aka converted) to that type. This ensures that pypy's annotator will always
find the correct form. Typically, the pypy/rpython translater will optimize that "extra call".

As the ``.value`` field is uniform across all subclasses, unpacking is easy. (And again will be optimized by tge
pypy/rpython translater).

This set of classes will be extended when more Castle types/primitives a added.
And it MUST be kept in sync with ``PortrayType``(s) in the writer.

..note:: CC_B_Component

  ``CC_B_Component`` is in line with this; it's the type of an element

   .. todo: fix that detail
"""


class CC_B_Value:
    """Base class for all argument-value wrappers.
        Never instantiate directly -- use a concrete subclass like ``CC_B_int``."""

class CC_B_int(CC_B_Value):
    def __init__(self, v):
        self.value = int(v)

class CC_B_float(CC_B_Value):
    def __init__(self, v):
        self.value = float(v)

class CC_B_string(CC_B_Value):
    def __init__(self, v):
        self.value = str(v)

class CC_B_boolean(CC_B_Value):
    def __init__(self, v):
        self.value = bool(v)

