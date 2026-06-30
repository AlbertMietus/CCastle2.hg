# (C) Albert Mietus, 2026. CodeAI=GH.Claude.Opus-4.8
#
# Type stub (signatures + usage docs) for ``castle.aigr.tools.scaffolding.namespaces``.
# Hand-maintained "manual autodoc" companion to namespaces.py.

import typing as PTH
from castle import aigr as aigr
from castle.aigr import NamedNode as NamedNode, ID as ID, QualID as QualID
from castle.monorail.base import MRO_Dispatch_Mixin as MRO_Dispatch_Mixin
from . import ScaffolderNode as ScaffolderNode

logger: PTH.Any

class ScaffolderNameSpace(ScaffolderNode, MRO_Dispatch_Mixin):
    """The behavioural namespace API for any wrapped ``_NameSpace`` node.

    Wrap a namespace node (or anything that *has* a scope) and use this to
    register names and look them up::

        ns = ScaffolderNameSpace(some_namespace_node)
        ns.register(a_named_node)             # type-dispatched registration
        node = ns.getID("foo")                # raises NameError if missing
        node = ns.findNode("foo")             # returns None if missing
        node = ns.search("a.b.c")             # walk dotted names across nested NS

    Registration is dispatched by node type (via ``MRO_Dispatch_Mixin`` with the
    ``register`` prefix): add a ``register_<ClassName>`` method to handle a new
    node kind; ``_default_register`` warns for unhandled types.
    """

    _prefixes: PTH.ClassVar[tuple[str, ...]]
    _nodeCls: type
    _link_fields: frozenset[str]
    _kids_fields: frozenset[str]

    def register(self, named_node: aigr.NamedNode, asName: PTH.Optional[ID | str] = ...) -> None:
        """Register *named_node* in this namespace (optionally under *asName*).

        The concrete ``register_<Type>`` handler is chosen by the node's type.
        Passing an already-wrapped node is a mistake; it is unwrapped with a warning.
        """
        ...

    def __len__(self) -> int: ...

    def findNode(self, name: ID | str) -> PTH.Optional[NamedNode]:
        """Return the node registered under *name* (searching outer namespaces), or ``None``."""
        ...

    def getID(self, name: ID) -> NamedNode:
        """Like :meth:`findNode` but raise :class:`castle.aigr.base.errors.NameError` if absent."""
        ...

    def search(self, dottedName: ID | str) -> PTH.Optional[NamedNode]:
        """Resolve a dotted name part-by-part across nested namespaces; return the deepest node or ``None``."""
        ...

    def find_byType(self, cls: type) -> dict[ID, NamedNode]:
        """Return the local entries whose value is an instance of *cls*, as ``{name: node}``."""
        ...

    def list_names(self) -> tuple[ID, ...]:
        """Return the names registered directly in this namespace."""
        ...

    def search_qualNames(self) -> tuple[QualID, ...]:
        """Return all names, recursively, as qualified-name (``QualID``) tuples."""
        ...

    def search_dottedNames(self) -> tuple[str, ...]:
        """Return all names, recursively, as dotted strings (see :meth:`search_qualNames`)."""
        ...

    def _findNode(self, name: ID) -> PTH.Optional[NamedNode]:
        """Core look-up used by every public finder: this namespace then its ``outer_ns``."""
        ...

    def _default_register(self, named_node: aigr.NamedNode, asName: PTH.Optional[ID | str] = ...) -> None:
        """Fallback registration handler -- warns; reaching it is usually a mistake."""
        ...

    def register_NamedNode(self, named_node: aigr.NamedNode, asName: PTH.Optional[ID | str] = ...) -> None:
        """Register any plain :class:`NamedNode` by its name (or *asName*)."""
        ...

    def register__NameSpace(self, named_node: aigr.namespaces._NameSpace, asName: PTH.Optional[ID | str] = ...) -> None:
        """Register a nested namespace and set its ``outer_ns`` to this one."""
        ...

    def register_Method(self, named_node: aigr.Method, asName: PTH.Optional[ID | str] = ...) -> None:
        """Register a :class:`castle.aigr.statements.Method` and link its ``outer_ns``."""
        ...

    def register_ComponentInterface(self, comp: aigr.ComponentInterface, asName: PTH.Optional[ID | str] = ...) -> None:
        """Register a component *interface*, merging it onto an already-registered implementation when present."""
        ...

    def register_ComponentImplementation(self, comp: aigr.ComponentImplementation, asName: PTH.Optional[ID | str] = ...) -> None:
        """Register a component *implementation*, adopting an already-registered interface when present."""
        ...
