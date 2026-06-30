# (C) Albert Mietus, 2026. CodeAI=GH.Claude.Opus-4.8
#
# Type stub for ``castle.writers.RPy.writer.walker``.

import typing as PTH
from castle import aigr
from castle.monorail.base.visitors import Visitor

class Walker(Visitor):
    """Tree-traversal sub-visitor: answers "what are the children of this node?".

    ``Walker`` is one of the four helper visitors owned by :class:`Renderer`.
    For each AIGR node type it knows about, a ``visit_<ClassName>`` method
    returns the tuple of child nodes that the ``Renderer`` should descend into.

    The ``Renderer`` calls ``walker.visit(node)`` and iterates the result.
    ``_defaultType = tuple`` means an unhandled node type returns an empty
    tuple (no children), which is the correct default.

    Usage
    -----
    Normally instantiated inside :class:`Renderer`; you can also use it
    standalone::

        from castle.writers.RPy.writer.walker import Walker

        walker = Walker()
        children = walker.visit(component_implementation_node)
        # -> tuple of (ns_nodes..., handlers...)
    """

    def visit__NameSpace(self, node: PTH.Any) -> PTH.Sequence[aigr.AIGR]:
        """Walk a namespace node: return all named items in the namespace.

        Works with both raw AIGR nodes and already-scaffolded wrappers.
        """
        ...

    def visit__Named_callable(self, node: PTH.Any) -> PTH.Sequence[aigr.AIGR]:
        """Walk a callable node (Method, EventHandler, ...): return its body."""
        ...

    def visit_ComponentImplementation(self, node: PTH.Any) -> PTH.Sequence[aigr.AIGR]:
        """Walk a ComponentImplementation: return namespace items + handlers."""
        ...

    def visit_Body(self, node: PTH.Any) -> PTH.Sequence[aigr.AIGR]:
        """Walk a Body: return its statement list."""
        ...

    def visit_VoidCall(self, node: PTH.Any) -> PTH.Sequence[aigr.AIGR]:
        """Walk a VoidCall: return the single wrapped Call node."""
        ...

    def visit_Call(self, node: PTH.Any) -> PTH.Sequence[aigr.AIGR]:
        """Walk a Call: return the callable node (the target of the call)."""
        ...

    def visit_fString(self, node: PTH.Any) -> PTH.Sequence[aigr.AIGR]:
        """Walk an fString: return an empty tuple (no children to descend)."""
        ...
