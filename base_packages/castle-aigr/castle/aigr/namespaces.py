# (C) Albert Mietus, 2023. Part of Castle/CCastle project

"""This file contains AIGR-classes to model (all kind of) namespaces, including "scopes". A namespace can be named, or unamed.

There are several kind of namespaces, like:
 * ``Source_NS`` : roughly, the file that contains (Castle) code.
 * ``Scope``     : an (unamed) namespace like the body of a function, class, component ect
 * ``SubScope``  : roughly anything between '{'  and '}' which defines names.

.. note::

   * Many namespaces have a name (where the name is registered in the outer NS).
   * That dataclasses is called NamedSpace (with a ``d``) and use NamedNode as a MixIn
   * Unnamed namedspace are often called a scope
"""

from __future__ import annotations

import logging; logger = logging.getLogger(__name__)
import typing as PTH                                                                                  # Python TypeHints
from enum import Enum
from dataclasses import dataclass, KW_ONLY
from dataclasses import field as dc_field
from pathlib import Path

from .nodes import NamedNode,  ID
from .base import AIGRNode



@dataclass
class _NameSpace(AIGRNode):
    """This models a namespace and/or scope (baseclass).

    It contained *"named nodes"* that should be :method:`register()`ed and can be found by :method:`getID()` and/or :method:`findNode()`.

    Most namespace have a ``outer_ns`` which is also used to lookup names. Howver, qua interface it is optional.
    """
    _: KW_ONLY
    outer_ns   :PTH.Optional[_NameSpace]=None
    _dict      :PTH.Dict[ID, NamedNode]=dc_field(init=None, default_factory=lambda: dict()) #type: ignore[call-overload]


@dataclass
class NamedSpace(NamedNode, _NameSpace):
    """A ``NamedSpace`` is a namedspace with a name ...."""



@dataclass
class Source_NS(NamedSpace):
    """This namespace is used for CCastle source files (so: *.Moat- & *.Castle-files). That filename is stored in ``source``"""
    _: KW_ONLY
    source       :PTH.Optional[Path|str]=None

    def __post_init__(self):
        if isinstance(self.source, str):
            self.source = Path(self.source)

@dataclass
class _Target_NS(_NameSpace):
    """This ABSTARCT namespace is used to "store" AIGR-parts that will rendered into one *low-level* code-file.
       Typical, each Backend.Writer will subclass this class for the specifics for that language."""
    _: KW_ONLY
    target_file     :PTH.Optional[Path|str]=None

    def __post_init__(self):
        if isinstance(self.target_file, str):
            self.target_file = Path(self.target_file)



@dataclass
class Scope(_NameSpace):
    """An body (```{ ....}```) has it own namespace, as it defines a scope. But many names (``ID``s) in that namespace
    are defines (registered) in an outer namespace . Therefore we have this special namespace *Scope* dataclass"""
    _: KW_ONLY
    outer_ns : _NameSpace

class _hasScope(Scope):
    """This Mixin adds a (sub)scope to an Class, and 'forward' the namespace-API to that scope-namespace
    Typical, the class to which this Mixin is added has a 'aigr.Body' but that is not mandatory"""

    def _register_parameters(self, post_init=False):
        """CONVINIANT FUNCTION: when `self` has parameters, register them in the scope.
           Usually called by __post_init__()"""

        if post_init:
            logger.debug(f"Auto register parameters -- post_init: {post_init}")
        if getattr(self, 'parameters', False):
            logger.debug(f"{type(self)} has parameters: {self.parameters} -- {self}")
            for p in self.parameters:
                self.register(p)


