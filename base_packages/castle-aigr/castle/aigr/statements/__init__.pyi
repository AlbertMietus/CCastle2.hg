# (C) Albert Mietus, 2026. CodeAI=GH.Claude.Opus-4.8
#
# Type stub (signatures + usage docs) for the ``castle.aigr.statements`` package.
# Hand-maintained "manual autodoc" companion to statements/__init__.py.

from .. import AIGR as AIGR, AIGRNode as AIGRNode

class _statement(AIGRNode):
    """Base class of every AIGR *statement* (the things that make up a body)."""

from .simple import *
from .flow import *
from .compounds import *
from .defs import *
from .callables import *
