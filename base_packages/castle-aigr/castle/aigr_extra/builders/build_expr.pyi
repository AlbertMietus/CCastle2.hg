# (C) Albert Mietus, 2026. CodeAI=GH.Claude.Opus-4.8
#
# Type stub (signatures + usage docs) for ``castle.aigr_extra.builders.build_expr``.
# Hand-maintained "manual autodoc" companion to build_expr.py.
#
# NOTE: the builder functions below are generated at import time by
# ``_meta_build`` (one per public operator class). The ``if False:`` blocks in
# the source are intentional documentation, not dead code -- they show what each
# generated builder looks like. The signatures are declared here for tools.

import typing as PTH
from ...aigr.expressions import operators as operators
from ...aigr.expressions.operator_expressions import LRexpression as LRexpression, RLexpression as RLexpression

logger: PTH.Any

# --- Left-associative builders (-> LRexpression) ---
def Times(left: PTH.Any, right: PTH.Any, *more: PTH.Any) -> LRexpression:
    """Build an ``LRexpression`` for the ``*`` (Times) operator over the given values."""
    ...
def Div(left: PTH.Any, right: PTH.Any, *more: PTH.Any) -> LRexpression:
    """Build an ``LRexpression`` for the ``/`` (Div) operator over the given values."""
    ...
def Modulo(left: PTH.Any, right: PTH.Any, *more: PTH.Any) -> LRexpression:
    """Build an ``LRexpression`` for the ``%`` (Modulo) operator over the given values."""
    ...
def Add(left: PTH.Any, right: PTH.Any, *more: PTH.Any) -> LRexpression:
    """Build an ``LRexpression`` for the ``+`` (Add) operator over the given values."""
    ...
def Sub(left: PTH.Any, right: PTH.Any, *more: PTH.Any) -> LRexpression:
    """Build an ``LRexpression`` for the ``-`` (Sub) operator over the given values."""
    ...

# --- Right-associative builders (-> RLexpression) ---
def Power(left: PTH.Any, right: PTH.Any, *more: PTH.Any) -> RLexpression:
    """Build an ``RLexpression`` for the ``**`` (Power) operator over the given values."""
    ...

def _meta_build(super_op: type, expr: type) -> None:
    """Generate, into the module globals, one builder per subclass of *super_op*.

    Each generated builder has the name of the operator class and returns *expr*
    (``LRexpression`` or ``RLexpression``) wrapping that operator. Called twice
    at import time (for left- and right-associative operators).
    """
    ...
