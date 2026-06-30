# (C) Albert Mietus, 2026. CodeAI=GH.Claude.Opus-4.8
#
# Type stub (signatures + usage docs) for ``castle.monorail.base.visitors``.
# Hand-maintained "manual autodoc" companion to visitors.py.

import typing as PTH
from .dispatch import MRO_Dispatch_Mixin as MRO_Dispatch_Mixin

logger: PTH.Any

class Visitor(MRO_Dispatch_Mixin):
    """Type-dispatching visitor base class (the foundation of every CCastle walker).

    Subclass it and add ``visit_<ClassName>`` methods; call :meth:`visit` with a
    node and the right handler is chosen by walking the node's MRO -- so a
    ``visit_<BaseClass>`` handler acts as a catch-all for all its subclasses.

    Two phases are available, selected by the method *prefix*:

    * ``visit``  -- run *before* the children (the main phase).
    * ``depart`` -- run *after* the children; default is a no-op.

    Usage
    -----
    ::

        class Printer(Visitor):
            def visit_AIGR(self, node):       # catch-all (AIGR is the base)
                print('node:', node)
            def depart_Component(self, node): # runs after a Component's children
                print('done:', node.name)

        Printer().visit(some_node)

    Dispatch on a different object
    ------------------------------
    ``visit(node, dispatch_on=other)`` selects the handler by ``type(other)`` but
    still passes ``node`` to it. This indirection is what enables reference
    resolution (e.g. the RPy-writer's ``IDRef``).

    Customising the mechanism
    -------------------------
    The phases come from :attr:`_prefixes`. Override it (e.g. ``('prefix',)``) to
    build a non visit/depart dispatcher that calls ``prefix_<ClassName>``.
    """

    _prefixes: PTH.ClassVar[tuple[str, ...]]
    """The phases/prefixes this visitor recognises. Default ``('visit', 'depart')``."""
    _defaultType: PTH.Callable
    """Factory for the value returned when no handler is found (default: ``lambda: None``)."""

    def _visitor(self, node: PTH.Any, dispatch_on: PTH.Any | None = ..., prefix: str = ...) -> PTH.Any:
        """Low-level dispatch primitive that :meth:`visit` and :meth:`depart` wrap.

        Override the *prefix* to add your own phase. This is the hook a custom
        dispatcher uses, e.g. ``return self._visitor(node, prefix='prefix')``
        together with ``_prefixes = ('prefix',)`` and ``prefix_<ClassName>`` handlers.
        """
        ...

    def visit(self, node: PTH.Any, dispatch_on: PTH.Any | None = ...) -> PTH.Any:
        """Run the ``visit`` phase for *node*.

        The handler is ``visit_<ClassName>`` resolved over the MRO of
        ``type(dispatch_on or node)``. Returns the handler's result, or
        ``_defaultType()`` when nothing matches.
        """
        ...

    def depart(self, node: PTH.Any, dispatch_on: PTH.Any | None = ...) -> PTH.Any:
        """Run the ``depart`` phase for *node* (after its children). See :meth:`visit`."""
        ...

    def _default_visit(self, node: PTH.Any) -> PTH.Any:
        """Fallback for the ``visit`` phase. Warns -- relying on it is usually a mistake.

        Override in a subclass to provide a real catch-all instead of a warning.
        """
        ...

    def _default_depart(self, node: PTH.Any) -> None:
        """Fallback for the ``depart`` phase. No-op by design (departing is optional)."""
        ...
