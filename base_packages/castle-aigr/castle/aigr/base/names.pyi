# (C) Albert Mietus, 2026. CodeAI=GH.Claude.Opus-4.8
#
# Type stub (signatures + usage docs) for ``castle.aigr.base.names``.
# Hand-maintained "manual autodoc" companion to names.py.

import typing as PTH
from dataclasses import dataclass, KW_ONLY
from .AIGR import AIGR as AIGR

class _Context(AIGR):
    """Base class for the *context* of an ``ID`` (is it a Def, a Ref or a Set?)."""

class Def(_Context):
    """Context marking the place where a name is *defined*."""

_Def_cls = Def

@dataclass
class Ref(_Context):
    """Context marking a *reference* to a (defined) name.

    Optionally carries the resolved ``reference`` node once name resolution has
    run; until then it is ``None``.
    """
    _: KW_ONLY
    reference: PTH.Optional[AIGR] = ...

_Ref_cls = Ref

@dataclass
class Set(_Context):
    """Context marking the place where a name is *set*/changed (assignment target)."""
    _: KW_ONLY
    reference: PTH.Optional[PTH.Any] = ...

RefType = PTH.TypeVar("RefType", bound=AIGR)

class ID(str, AIGR):
    """A name as it appears in Castle code (components, callables, variables, ...).

    An ``ID`` *is* a ``str`` (so it prints and compares like its text) but also
    an AIGR node carrying an optional :class:`_Context`: is this occurrence a
    definition (:meth:`Def`) or a reference (:class:`Ref`)?

    Usage
    -----
    ::

        ID("foo")                     # a plain name
        ID.Def("foo")                 # a defining occurrence
        ID.Ref("foo", some_node)      # a reference, optionally resolved
        x: ID.Ref[Protocol]           # ID.Ref[...] also works as a type hint
    """

    context: PTH.Optional[_Context]
    """The Def/Ref/Set context of this occurrence, or ``None`` for a bare name."""

    def __new__(cls, name: str, context: PTH.Optional[_Context] = ...) -> ID: ...
    def __init__(self, name: str, context: PTH.Optional[_Context] = ...) -> None: ...

    @staticmethod
    def Def(name: str) -> ID:
        """Create an ``ID`` carrying a :class:`Def` context (a defining occurrence)."""
        ...

    class Ref(PTH.Generic[RefType]):
        """Create an ``ID`` with a :class:`Ref` context; also usable as ``ID.Ref[T]`` hint.

        Calling ``ID.Ref(name, target)`` wraps *target* in a :class:`Ref` (unless
        it already is one) and returns the reference ``ID``. Subscripting
        (``ID.Ref[Protocol]``) yields an optional type hint for such references.
        """
        def __new__(cls, name: str, context: RefType | _Ref_cls) -> ID.Ref: ...
        def __class_getitem__(cls, item: PTH.Any) -> PTH.Any: ...

class Label(str):
    """An internal AIGR name that, unlike :class:`ID`, never appears in Castle code."""

QualID = list[ID]
"""A dotted/qualified name, modelled as a list of :class:`ID` parts."""
