# (C) Albert Mietus, 2026. CodeAI=GH.Claude.Opus-4.8
#
# Type stub (signatures + usage docs) for ``castle.aigr.events``.
# Hand-maintained "manual autodoc" companion to events.py.

import typing as PTH
from dataclasses import dataclass, KW_ONLY
from .aid import TypedParameter as TypedParameter
from .nodes import NamedNode as NamedNode

__all__ = ['Event']

@dataclass
class Event(NamedNode):
    """An event -- modelled like a (remote) function call.

    It has a ``name``, an optional ``return_type`` (``None`` means void) and an
    immutable sequence of typed parameters. Events are grouped into an
    ``EventProtocol`` (see :mod:`castle.aigr.protocols`)::

        Event("tick", typedParameters=(TypedParameter("n", types.int),))
    """
    _: KW_ONLY
    return_type: PTH.Optional[type] = ...
    typedParameters: PTH.Sequence[TypedParameter] = ...
