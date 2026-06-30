# (C) Albert Mietus, 2026. CodeAI=GH.Claude.Opus-4.8
#
# Type stub (signatures + usage docs) for the ``castle.aigr.expressions`` package.
# Hand-maintained "manual autodoc" companion to expressions/__init__.py.

from .. import AIGRNode as AIGRNode

class _expression(AIGRNode):
    """Base class of every AIGR *expression* (something that yields a value)."""

from .operator_expressions import *
from .calls import *
from .literals import *
