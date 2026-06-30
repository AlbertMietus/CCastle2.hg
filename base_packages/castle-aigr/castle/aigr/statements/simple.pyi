# (C) Albert Mietus, 2026. CodeAI=GH.Claude.Opus-4.8
#
# Type stub (signatures + usage docs) for ``castle.aigr.statements.simple``.
# Hand-maintained "manual autodoc" companion to simple.py.

import typing as PTH
from dataclasses import dataclass, KW_ONLY
from . import _statement as _statement, AIGR as AIGR
from .. import expressions as expressions

logger: PTH.Any

@dataclass
class Become(_statement):
    """An assignment statement ``targets := values`` (Castle's ``:=``).

    Models single, multiple, tuple and (un)packing assignment via parallel
    ``targets``/``values`` tuples. Currently only single assignment is
    supported (both tuples have length 1)::

        Become(targets=(ID("a"),), values=(Constant(value=2),))
    """
    _: KW_ONLY
    targets: tuple[AIGR]
    values: tuple[AIGR]

@dataclass
class VoidCall(_statement):
    """Wrap a ``Call`` *expression* so it can stand alone as a *statement*.

    A function call is an expression; when its result is discarded it must be
    wrapped here. In Castle source this wrapper is implicit.
    """
    call: expressions.Call
