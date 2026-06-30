# (C) Albert Mietus, 2026. CodeAI=GH.Claude.Opus-4.8
#
# Type stub (signatures + usage docs) for ``castle.monorail.base.dispatch``.
# Hand-maintained "manual autodoc" companion to dispatch.py -- describes HOW to
# use the public API, for tools (mypy/pyright) and as context for CodeAI.

import typing as PTH

logger: PTH.Any

class MRO_Dispatch_Mixin:
    """Find a method by walking an object's MRO.

    Mix this into a class to get *type-based dispatch*: for a ``node`` and a
    ``prefix`` it looks up ``<prefix>_<ClassName>`` for every class in
    ``type(node).mro()`` (most-derived first), falling back to
    ``_default_<prefix>`` if nothing matches.

    Usage
    -----
    Subclass, list the prefixes you intend to use, and add the handlers::

        class MyDispatcher(MRO_Dispatch_Mixin):
            _prefixes = ('handle',)
            def handle_int(self, node): ...      # matches int (and bool via MRO)

        m = MyDispatcher()
        method = m.dispatch_find_method_by_mro(42, 'handle')   # -> handle_int

    Most callers do not use this class directly but the higher-level
    :class:`castle.monorail.base.visitors.Visitor`, which adds ``visit``/``depart``.
    """

    _prefixes: PTH.ClassVar[tuple[str, ...]]
    """Whitelist of prefixes this dispatcher uses; unknown prefixes are warned about."""

    def dispatch_check_prefix(self, prefix: str) -> bool:
        """Return ``True`` if *prefix* is declared in :attr:`_prefixes` (warns otherwise)."""
        ...

    def dispatch_find_method_by_mro(self, node: PTH.Any, prefix: str) -> PTH.Optional[PTH.Callable]:
        """Resolve the handler for *node*.

        Returns the bound ``<prefix>_<ClassName>`` method found by walking the
        MRO of ``type(node)``, or the ``_default_<prefix>`` fallback, or
        ``None`` when neither exists.
        """
        ...
