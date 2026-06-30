# (C) Albert Mietus, 2026. CodeAI=GH.Claude.Opus-4.8
#
# Type stub (signatures + usage docs) for ``castle.aigr_extra.blend.mangle``.
# Hand-maintained "manual autodoc" companion to mangle.py.

import typing as PTH
from castle.aigr import ID as ID, QualID as QualID

logger: PTH.Any

def mangle_event_handler(*,
                         protocol: PTH.Optional[str | ID | QualID] = ...,
                         event: PTH.Optional[str | ID | QualID] = ...,
                         port: PTH.Optional[str | ID | QualID] = ...) -> ID:
    """Blend the three parts of an event-handler into a single ``ID``.

    This is the canonical way to compute an :class:`castle.aigr.statements.EventHandler`
    name. Any part left as ``None`` becomes ``'default'``. The result is
    ``ID(f'{protocol}_{event}__{port}')``::

        mangle_event_handler(protocol="Clock", event="tick", port="p")
        # -> ID('Clock_tick__p')
    """
    ...

def qualID_2_str(quid: QualID | ID | str) -> str:
    """Flatten an ``ID``/``QualID``/``str`` to a string, dropping a leading ``'self'``."""
    ...
