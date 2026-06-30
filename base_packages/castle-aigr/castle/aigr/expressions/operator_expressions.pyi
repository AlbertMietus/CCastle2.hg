# (C) Albert Mietus, 2026. CodeAI=GH.Claude.Opus-4.8
#
# Type stub (signatures + usage docs) for ``castle.aigr.expressions.operator_expressions``.
# Hand-maintained "manual autodoc" companion to operator_expressions.py.

import typing as PTH
from dataclasses import dataclass, KW_ONLY
from .. import AIGR as AIGR
from . import _expression as _expression
from . import operators as operators

logger: PTH.Any

@dataclass
class LRexpression(_expression):
    """A left-associative operator expression: ``values[0] op values[1] op ...``.

    ``op`` is a :class:`operators._LeftAssociative` instance. Prefer the
    ``builders.build_expr`` helpers (e.g. ``Add(a, b)``) to construct these.
    """
    _: KW_ONLY
    op: operators._LeftAssociative
    values: tuple[AIGR]

@dataclass
class RLexpression(_expression):
    """A right-associative operator expression (e.g. ``a ** b ** c``)."""
    _: KW_ONLY
    op: operators._RightAssociative
    values: tuple[AIGR]

@dataclass
class Unaryexpression(_expression):
    """A unary operator applied to a single ``value`` (e.g. ``not x``, ``-x``)."""
    _: KW_ONLY
    op: operators._unart_op
    value: AIGR

@dataclass
class Compare(_expression):
    """A comparison of two or more ``values`` yielding a boolean.

    Supports cascaded comparison (``1 < 2 < 3``, even ``7 > 5 < 11``), evaluated
    left-to-right with each middle value evaluated once. ``ops`` is either:

    * a *single* compare operator reused between every pair of values, or
    * a tuple of operators with ``len(ops) == len(values) - 1``.

    For two values, ``ops`` must not be a tuple.
    """
    _: KW_ONLY
    ops: operators._compare_op | tuple[operators._compare_op]
    values: tuple[AIGR, ...]

@dataclass
class _ShortCircuitLogic(_expression):
    """Placeholder for short-circuit boolean logic expressions (work in progress)."""

@dataclass
class _OtherBoolean(_expression):
    """Placeholder for non-short-circuit boolean expressions (work in progress)."""
