# (C) Albert Mietus, 2026. CodeAI=GH.Claude.Opus-4.8
#
# Type stub for ``castle.writers.RPy.writer.machinery._bundler``.

import typing as PTH
from castle import aigr
from castle.aigr import types as CCTypes
from castle.writers.RPy.aid import TextBlock

TypeTag = str
"""A type-cast code fragment produced by :meth:`Bundler.box`.

Typically looks like ``CC_B_int(expr)`` -- a string of generated Python code
that wraps a value in the appropriate Castle type wrapper.
"""

GeneratedCode = PTH.Optional[str | TextBlock]
"""A fragment of generated RPy Python code, or a type-tag string."""


class Bundler(PTH.Protocol):
    """Abstract strategy for packing/unpacking Castle call arguments.

    ``Bundler.__new__`` always returns a :class:`NativeBundler` instance.
    Subclasses override the four abstract methods to implement a specific
    calling convention.

    The four-step calling convention
    ---------------------------------
    1. :meth:`box` -- wrap each actual argument value in its Castle type.
    2. :meth:`pack` -- combine all boxed arguments into the argument list
       passed at the call site.
    3. (in the callee) :meth:`unpack` -- destructure the packed argument list
       back into individual parameters.
    4. :meth:`unbox` -- extract the raw value from a single boxed argument.

    Usage
    -----
    ::

        bundler = Bundler()           # returns NativeBundler
        tag  = bundler.box("42", CCTypes.int)      # -> 'CC_B_int(42)'
        args = bundler.pack([tag], params)          # -> '[CC_B_int(42)], {}'
    """

    def __new__(cls, hint: str = ..., **kwargs: PTH.Any) -> "Bundler": ...

    def box(self, argument: GeneratedCode, cc_type: CCTypes._types) -> TypeTag:
        """Box a single generated argument into the Castle type wrapper.

        Returns a code fragment like ``CC_B_int(argument)``.
        """
        ...

    def pack(
        self,
        arguments: PTH.Sequence[TypeTag],
        formal_parameters: aigr.OptionalTypedParameterList,
    ) -> TextBlock:
        """Combine all boxed arguments into the call-site argument representation.

        The exact representation depends on the bundler's calling convention.
        :class:`NativeBundler` produces ``[arg, ...], {}`` (a list + empty dict).
        """
        ...

    def unpack(
        self,
        parameters: GeneratedCode,
        formal_parameters: aigr.OptionalTypedParameterList,
    ) -> TextBlock:
        """Generate code to destructure the packed argument list in the callee.

        Note: currently raises ``AssertionError`` in :class:`NativeBundler` (WIP).
        """
        ...

    def unbox(self, parm: str) -> GeneratedCode:
        """Generate code to extract the raw value from a single boxed argument.

        :class:`NativeBundler` returns ``parm.value``.
        """
        ...
