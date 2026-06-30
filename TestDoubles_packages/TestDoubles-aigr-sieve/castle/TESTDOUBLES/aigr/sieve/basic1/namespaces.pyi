# (C) Albert Mietus, 2026. CodeAI=GH.Claude.Opus-4.8
#
# Type stub for ``castle.TESTDOUBLES.aigr.sieve.basic1.namespaces``.
#
# Provides the ``Source_NS`` namespace fixtures that mirror the file-level
# structure of the Sieve Castle source (one namespace per Castle file).
# Imports between namespaces are wired via ``ScaffolderNameSpace.register``.
#
# Typical test usage::
#
#   from castle.TESTDOUBLES.aigr.sieve.basic1 import namespaces
#   from castle import aigr
#
#   def test_protocols_ns_exists():
#       assert isinstance(namespaces.protocols, aigr.Source_NS)
#       assert str(namespaces.protocols.name) == "protocols"
#
#   def test_interfaces_imports_protocols():
#       # interfaces.Moat imports from protocols.Moat
#       ns = namespaces.interfaces
#       assert any(str(n.name) == "protocols" for n in ns._ns.values())

import typing as PTH

from castle.aigr import Source_NS
from castle.aigr.tools.scaffolding import ScaffolderNameSpace

protocols: Source_NS
"""Namespace fixture for ``protocols.Moat`` (source file).

Contains ``StartSieve`` and ``SimpleSieve`` protocol definitions.
Has no imports from other namespaces."""

interfaces: Source_NS
"""Namespace fixture for ``interfaces.Moat`` (source file).

Contains ``Generator``, ``Sieve``, and ``Finder`` component interfaces.
Imports: ``protocols``."""

comps: dict[str, Source_NS]
"""Mapping of component-name -> ``Source_NS`` fixture (one per Castle file).

Keys: ``"generator"``, ``"sieve"``, ``"finder"``.
Each namespace imports both ``interfaces`` and ``protocols``."""

main: Source_NS
"""Namespace fixture for ``main.Moat`` (the top-level Castle file).

Imports: ``interfaces``, ``protocols``, and (when ``_OPT_MAIN_IMPORTS_COMPS``
is true) all three component namespaces."""

wrapped_main: ScaffolderNameSpace
"""``ScaffolderNameSpace`` wrapper around ``main``; used to register imports."""

_OPT_MAIN_IMPORTS_COMPS: bool
"""Build-time flag: when ``True``, the ``main`` namespace also imports all
three component namespaces (``generator``, ``sieve``, ``finder``)."""

def _main_imports_comps() -> None:
    """Register each component namespace into ``wrapped_main``.

    Called once at module import when ``_OPT_MAIN_IMPORTS_COMPS`` is true.
    Not normally called from tests directly."""
    ...
