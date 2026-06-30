# (C) Albert Mietus, 2026. CodeAI=GH.Claude.Opus-4.8
#
# Type stub for ``castle.readers.ladon.parser.actions.parms_and_args``.
# Hand-maintained companion to parms_and_args.py.

import typing as PTH
from castle import aigr

logger: PTH.Any


class ParmsArgs:
    """TatSu semantic-action mixin for Castle parameter and argument rules.

    Mixed into :class:`~..castle_actions.CastleActions`; handles both the
    definition side (typed parameters) and the call side (argument tuples),
    plus literal identifiers used as constant values.
    """

    def typedParameterTuple(self, ast: PTH.Any) -> tuple[PTH.Any, ...]:
        """Reduce ``typedParameterTuple``: flatten TatSu AST into a **tuple** of TypedParameters.

        Uses :func:`~.support_functions.flat_tuple` so nested sequences are
        collapsed into a single flat tuple.
        """
        ...

    def typedParameter(self, ast: PTH.Any) -> aigr.TypedParameter:
        """Reduce ``typedParameter``: return a :class:`~castle.aigr.TypedParameter(name, type)`."""
        ...

    def argumentTuple(self, ast: PTH.Any) -> list[PTH.Any]:
        """Reduce ``argumentTuple``: flatten TatSu AST into a **list** of Arguments.

        Uses :func:`~.support_functions.flat_list` so nested sequences are
        collapsed into a single flat list.
        """
        ...

    def argument(self, ast: PTH.Any) -> aigr.Argument:
        """Reduce ``argument``: return an :class:`~castle.aigr.Argument(name, value)`."""
        ...

    def literal_ID(self, ast: PTH.Any) -> aigr.Constant:
        """Reduce ``literal_ID``: wrap the identifier string in a :class:`~castle.aigr.Constant`."""
        ...

    def modifiers(self, ast: PTH.Any) -> PTH.NoReturn:
        """Reduce ``modifiers``: always raises ``AssertionError`` (not yet supported in AIGR)."""
        ...
