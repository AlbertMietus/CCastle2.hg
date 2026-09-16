# (C) Albert Mietus, 2026. CodeAI=GH.Claude.Opus-4.8
#
# Type stub for ``castle.writers.RPy.writer.machinery._bundler``.

import typing as PTH
from castle import aigr
from castle.aigr import types as CCTypes
from castle.writers.RPy.aid import TextBlock

TypeTag = str
GeneratedCode = PTH.Optional[str | TextBlock]

class Bundler(PTH.Protocol):

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
