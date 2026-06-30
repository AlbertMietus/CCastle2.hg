# (C) Albert Mietus, 2026. CodeAI=GH.Claude.Opus-4.8
#
# Type stub (signatures + usage docs) for ``castle.aigr.statements.flow``.
# Hand-maintained "manual autodoc" companion to flow.py.

import typing as PTH
from dataclasses import dataclass, KW_ONLY
from . import _statement as _statement, AIGR as AIGR

logger: PTH.Any

@dataclass
class If(_statement):
    """An ``if`` statement: a boolean ``test`` and at least a ``body``.

    The optional ``orelse`` is either a plain ``Body`` (an ``else``) or another
    :class:`If` (modelling ``elif`` as in Python). ``body``/``orelse`` are
    typically ``Body`` nodes.
    """
    _: KW_ONLY
    test: AIGR
    body: AIGR
    orelse: PTH.Optional[AIGR] = ...
