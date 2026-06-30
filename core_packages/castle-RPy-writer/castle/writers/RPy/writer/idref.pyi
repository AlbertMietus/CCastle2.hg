# (C) Albert Mietus, 2026. CodeAI=GH.Claude.Opus-4.8
#
# Type stub for ``castle.writers.RPy.writer.idref``.

import typing as PTH
from castle import aigr
from castle.monorail.base.visitors import Visitor

class IDRef(Visitor):
    """Reference-resolution sub-visitor: renders an ID according to what it points to.

    ``IDRef`` is one of the four helpers owned by :class:`Renderer`.  It
    answers *"how do I render this ``ID``, given what it points to?"* by
    dispatching on the *referenced* node's class via ``dispatch_on``.

    The key indirection is :meth:`portray`: it calls
    ``self.visit(id_node, dispatch_on=id_node.context.reference)``, so the
    handler is chosen by the *target* class, not the ``ID`` class.

    Usage
    -----
    ::

        idref = IDRef(renderer)
        text = idref.portray(some_id_node_with_ref_context)
        # -> 'cc_CI_Counter'  (if the ID refs a ComponentInterface named Counter)
    """

    def __init__(self, renderer: PTH.Any) -> None: ...

    def portray(self, node: aigr.ID) -> str:
        """Render *node* (an ``ID`` with a ``Ref`` context) as an RPy name.

        The handler is chosen by the *referenced* node's class.  Asserts that
        ``node.context`` is an ``aigr.Ref``.
        """
        ...

    def _default_visit(self, node: aigr.ID) -> str:
        """Fallback: raises ``NotImplementedError`` for unhandled reference targets."""
        ...

    def visit_ID(self, node: PTH.Any) -> str:
        """ID referencing another ID: recursively render the referenced ID."""
        ...

    def visit_ComponentInterface(self, node: PTH.Any) -> str:
        """ID referencing a ComponentInterface: return ``cc_CI_<Name>``."""
        ...

    def visit_ComponentImplementation(self, node: PTH.Any) -> str:
        """ID referencing a ComponentImplementation: return ``CC_<Name>``."""
        ...

    def visit__Named_callable(self, node: PTH.Any) -> str:
        """ID referencing a named callable: return the callable def name."""
        ...

    def visit_AIGR(self, node: PTH.Any) -> str:
        """Fallback catch-all: logs an error and returns ``str(node)``."""
        ...

    def visit_str(self, node: PTH.Any) -> str:
        """ID referencing a raw string: return the referenced string value."""
        ...
