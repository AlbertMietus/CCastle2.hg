# (C) Albert Mietus, 2026. CodeAI=GH.Claude.Opus-4.8
#
# Type stub (signatures + usage docs) for ``castle.aigr.statements.compounds``.
# Hand-maintained "manual autodoc" companion to compounds.py.

from dataclasses import dataclass, KW_ONLY
from . import _statement as _statement

@dataclass
class Body(_statement):
    """A ``Body`` -- the list of statements between ``{`` and ``}``.

    Used as the content of a callable, a component, an ``If`` branch, etc. The
    ``statements`` list is mutable; build an empty body and append, or pass a
    list up front. It is itself a statement, so a body may nest in a body.
    """
    _: KW_ONLY
    statements: list[_statement] = ...
