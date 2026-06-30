# (C) Albert Mietus, 2026. CodeAI=GH.Claude.Opus-4.8
#
# Type stub for ``castle.writers.RPy_buildin.buildin.CC_B_Values``.
# Argument-value wrappers for the NativeBundler calling convention.

import typing as PTH

class CC_B_Value:
    """Base class for all Castle argument-value wrappers.

    In RPy generated code, Castle primitive values are boxed into a
    ``CC_B_<type>`` wrapper before being packed into an argument list.
    The ``.value`` attribute always holds the unwrapped Python primitive.

    Never instantiate this base directly -- use a concrete subclass.
    """

class CC_B_int(CC_B_Value):
    """Wrapper for a Castle ``int`` argument.  Stores ``int(v)`` in ``.value``."""
    value: int
    def __init__(self, v: PTH.Any) -> None: ...

class CC_B_float(CC_B_Value):
    """Wrapper for a Castle ``float`` argument.  Stores ``float(v)`` in ``.value``."""
    value: float
    def __init__(self, v: PTH.Any) -> None: ...

class CC_B_string(CC_B_Value):
    """Wrapper for a Castle ``string`` argument.  Stores ``str(v)`` in ``.value``."""
    value: str
    def __init__(self, v: PTH.Any) -> None: ...

class CC_B_boolean(CC_B_Value):
    """Wrapper for a Castle ``boolean`` argument.  Stores ``bool(v)`` in ``.value``."""
    value: bool
    def __init__(self, v: PTH.Any) -> None: ...
