# (C) Albert Mietus, 2026. CodeAI=GH.Claude.Opus-4.8
#
# Type stub (signatures + usage docs) for ``castle.aigr.namespaces``.
# Hand-maintained "manual autodoc" companion to namespaces.py.

import typing as PTH
from dataclasses import dataclass, KW_ONLY
from dataclasses import field as dc_field
from pathlib import Path
from .nodes import NamedNode as NamedNode, ID as ID
from .base import AIGRNode as AIGRNode

logger: PTH.Any

@dataclass
class _NameSpace(AIGRNode):
    """Base class for AIGR namespaces and scopes.

    Holds the named children in ``_ns`` and an optional ``outer_ns`` used for
    name look-up. The *behavioural* namespace API (register / findNode / getID /
    search) is provided by the scaffolding wrapper
    :class:`castle.aigr.tools.scaffolding.ScaffolderNameSpace`; this dataclass
    only stores the data.
    """
    _: KW_ONLY
    outer_ns: PTH.Optional[_NameSpace] = ...
    _ns: PTH.Dict[ID, NamedNode] = dc_field(init=False, default_factory=dict)
    """The local name -> node mapping (populated via the scaffolder's ``register``)."""

@dataclass
class NamedSpace(NamedNode, _NameSpace):
    """A namespace that itself has a name (registered in its outer namespace)."""

@dataclass
class Source_NS(NamedSpace):
    """The namespace of a CCastle source file; its filename is kept in ``source``."""
    _: KW_ONLY
    source: PTH.Optional[Path | str] = ...
    def __post_init__(self) -> None: ...

@dataclass
class _Target_NS(_NameSpace):
    """Abstract namespace collecting AIGR that renders into one output file.

    Each backend writer subclasses this with language specifics; the eventual
    output file is ``target_file``.
    """
    _: KW_ONLY
    target_file: PTH.Optional[Path | str] = ...
    def __post_init__(self) -> None: ...

@dataclass
class Scope(_NameSpace):
    """An unnamed namespace for a body (``{ ... }``).

    Its own names may actually be *defined* in an outer namespace, hence the
    distinct dataclass.
    """
    _: KW_ONLY

class _hasScope(Scope):
    """Mixin adding a (sub)scope to a class and forwarding the namespace API to it."""
