# (C) Albert Mietus, 2026. CodeAI=GH.Claude.Opus-4.8
#
# Type stub (signatures + usage docs) for ``castle.aigr.expressions.calls``.
# Hand-maintained "manual autodoc" companion to calls.py.

import typing as PTH
from dataclasses import dataclass, KW_ONLY
from .. import AIGR as AIGR, ID as ID, errors as errors
from . import _expression as _expression

logger: PTH.Any

class _call(_expression):
    """Base for call-like expressions (the compiler resolves these to a method call)."""

@dataclass
class Call(_call):
    """A call expression: ``callable(arguments)``.

    ``callable`` is usually an ``ID`` reference but may be any AIGR node (e.g. a
    function-pointer). ``arguments`` is an optional tuple of AIGR argument
    nodes. To use a ``Call`` as a statement, wrap it in
    :class:`castle.aigr.statements.VoidCall`.
    """
    _: KW_ONLY
    callable: ID | AIGR
    arguments: PTH.Optional[tuple[AIGR, ...]] = ...

@dataclass
class Part(_call):
    """An attribute (``a.b``) or index (``a[1]``) access on ``base``.

    Exactly one of ``attribute`` / ``index`` must be set -- supplying both, or
    neither, raises :class:`castle.aigr.base.errors.PartError`. It is a
    ``_call`` because the compiler resolves it to a method on ``base``.
    """
    base: PTH.Optional[AIGR]
    _: KW_ONLY
    attribute: PTH.Optional[AIGR] = ...
    index: PTH.Optional[AIGR] = ...
    def __post_init__(self) -> None: ...
