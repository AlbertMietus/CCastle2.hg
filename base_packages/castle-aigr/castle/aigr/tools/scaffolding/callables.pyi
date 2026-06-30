# (C) Albert Mietus, 2026. CodeAI=GH.Claude.Opus-4.8
#
# Type stub (signatures + usage docs) for ``castle.aigr.tools.scaffolding.callables``.
# Hand-maintained "manual autodoc" companion to callables.py.

import typing as PTH
from . import ScaffolderNameSpace as ScaffolderNameSpace

logger: PTH.Any

class ScaffolderCallable(ScaffolderNameSpace):
    """Scaffolder for a callable (its scope *is* a namespace).

    On :meth:`auto_register` it registers the callable's parameters into its own
    namespace.
    """

    _nodeCls: type
    _kids_fields: frozenset[str]
    _attr_fields: frozenset[str]

    def auto_register(self) -> None:
        """Register the callable's parameters (see :meth:`auto_register_parameters`)."""
        ...

    def auto_register_parameters(self) -> None:
        """Register every ``TypedParameter`` of the wrapped callable into its namespace."""
        ...
