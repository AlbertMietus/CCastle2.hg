# (C) Albert Mietus, 2025. Part of Castle/CCastle project

import typing as PTH                                       # Python TypeHints
from dataclasses import dataclass, KW_ONLY

from .. import AIGR, ID

@dataclass
class _DispatchTable(AIGR):
    """A DispatchTable is a mapping between *triggers* (like `Events`) on a specific port, and the Handler that handle it.

    The best known/documented trigger is the event, which mapping is stored in the ``EventDispatchTable``. See there for more info

    .. note::

       A DispatchTable is allways related to (exactly) one port, within (one) Component (implementation).

    .. important::

       * For now, the name/ID of both the Port & Component(Implementation) are stored in `_DispatchTable`.

       * Soon, when the AIGR-as-tree path-functions are designed, those values (both as name, and as ref) will be fetch from the AIGR.
         E.g. by:

         - ./../@name ==> Port-ID
         - ./../../@name ==> ComponentImplementation-ID
    """
    _: KW_ONLY
    comp : ID # XXX One day, we fill find it by the AIRG-as-tree
    port : ID # XXX One day, we fill find it by the AIRG-as-tree






