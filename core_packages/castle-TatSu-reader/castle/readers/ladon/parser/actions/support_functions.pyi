# (C) Albert Mietus, 2026. CodeAI=GH.Claude.Opus-4.8
#
# Type stub for ``castle.readers.ladon.parser.actions.support_functions``.
# Hand-maintained companion to support_functions.py.

import typing as PTH

logger: PTH.Any

_T = PTH.TypeVar("_T", list, tuple)


def _flat_sequence(
    ast: PTH.Any,
    to_type: PTH.Callable[[PTH.Iterator[PTH.Any]], _T],
) -> _T:
    """Flatten a TatSu AST sequence (whose elements may themselves be lists or tuples).

    Each element of *ast* is expanded if it is a ``list`` or ``tuple``;
    scalars are yielded as-is.  The resulting generator is passed to
    *to_type* (e.g. ``list`` or ``tuple``) to produce the final collection.
    """
    ...


def flat_list(ast: PTH.Any) -> list[PTH.Any]:
    """Return a flat :class:`list` of all scalar elements in *ast*, expanding nested lists/tuples.

    Used by :class:`~.names.Names` (``qualRef``) and
    :class:`~.parms_and_args.ParmsArgs` (``argumentTuple``).
    """
    ...


def flat_tuple(ast: PTH.Any) -> tuple[PTH.Any, ...]:
    """Return a flat :class:`tuple` of all scalar elements in *ast*, expanding nested lists/tuples.

    Used by :class:`~.parms_and_args.ParmsArgs` (``typedParameterTuple``).
    """
    ...
