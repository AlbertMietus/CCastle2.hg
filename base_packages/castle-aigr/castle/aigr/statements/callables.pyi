# (C) Albert Mietus, 2026. CodeAI=GH.Claude.Opus-4.8
#
# Type stub (signatures + usage docs) for ``castle.aigr.statements.callables``.
# Hand-maintained "manual autodoc" companion to callables.py.

import typing as PTH
from dataclasses import dataclass, KW_ONLY
from ..namespaces import _hasScope as _hasScope
from . import _statement as _statement
from ..nodes import NamedNode as NamedNode
from .compounds import Body as Body
from ..aid import TypedParameter as TypedParameter, ReturnType as ReturnType
from ..base.names import ID as ID

logger: PTH.Any

@dataclass
class _callable(_hasScope, _statement):
    """Base of all callables (functions, methods, handlers, ...).

    Carries ``parameters`` (typed), an optional ``body`` and an optional
    ``returns`` type. It owns a scope (``_hasScope``) so its parameters/locals
    get a namespace. Not every callable is named, hence this is *not* a
    ``NamedNode``.
    """
    _: KW_ONLY
    parameters: tuple[TypedParameter, ...] = ...
    body: PTH.Optional[Body] = ...
    returns: PTH.Optional[ReturnType] = ...

@dataclass
class _Named_callable(NamedNode, _callable):
    """A :class:`_callable` that also has a name."""

@dataclass
class Method(_Named_callable):
    """A named callable bound to a component/class (a method)."""

@dataclass
class Initializer(Method):
    """A special :class:`Method` that initialises the component/class (``__init__``)."""

class _handlers(_Named_callable):
    """Base class for the various event/data handlers."""

@dataclass
class EventHandler(_handlers):
    """A callable run when a given protocol-event arrives on a given port.

    Each of ``protocol``, ``event`` and ``port`` is an :class:`ID` with a
    ``Ref`` context (a name/path, *not* the target object). ``'default'`` is a
    valid value for any of the three. The handler's ``name`` is a blend of the
    three -- compute it with
    :func:`castle.aigr_extra.blend.mangle.mangle_event_handler`.
    """
    _: KW_ONLY
    protocol: ID
    event: ID
    port: ID
