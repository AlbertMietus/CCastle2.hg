# (C) Albert Mietus, 2026. CodeAI=GH.Claude.Opus-4.8
#
# Type stub (signatures + usage docs) for ``castle.aigr.expressions.literals``.
# Hand-maintained "manual autodoc" companion to literals.py.

import typing as PTH
from dataclasses import dataclass, KW_ONLY
from .. import AIGR as AIGR, ID as ID
from . import _expression as _expression
from ..base import types as types

logger: PTH.Any

@dataclass
class _literal(_expression):
    """Base for literal values: a ``value`` plus an optional AIGR ``type``."""
    _: KW_ONLY
    value: PTH.Any
    type: PTH.Optional[types._types] = ...

@dataclass
class Constant(_literal):
    """A literal constant written in code: ``0`` (int), ``3.14`` (float), ``"hi"`` (string)."""

@dataclass
class _TemplateLiteral(_literal):
    """Base for template literals (like a Python f-string), generalised beyond strings.

    Carries an optional ``formater`` and the ``args`` (the names spliced in).
    """
    _: KW_ONLY
    formater: PTH.Any = ...
    args: list[ID] = ...

@dataclass
class fString(_TemplateLiteral):
    """A string-producing template literal (f-string-like).

    Builds a string by substituting the (string) values of local variables.
    Pass the template text as ``value``; the ``type`` defaults to
    ``types.string``. (Name may still change.)
    """
    value: str
    _: KW_ONLY
    def __post_init__(self) -> None: ...
