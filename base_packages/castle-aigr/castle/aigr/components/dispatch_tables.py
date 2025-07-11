# (C) Albert Mietus, 2025. Part of Castle/CCastle project

import typing as PTH                                       # Python TypeHints
from dataclasses import dataclass, KW_ONLY

from .. import AIGR, ID

@dataclass
class _DispatchTable(AIGR):
    """A DispatchTable is a mapping between *triggers* (like `Events`) on a specific port, and the Handler that handle it.

    The best known/documented trigger is the event, which mapping is stored in the ``EventDispatchTable``. See there for more info

    .. error::

       * See .../castle-aigr/designNotes/warning.html (BUSY on that)
       * See the note about .port in EventDispatchTable
    """
    _: KW_ONLY
    port : ID





