# (C) Albert Mietus, 2025. Part of Castle/CCastle project

import logging; logger = logging.getLogger(__name__)
import typing as PTH                                                                                  # Python TypeHints

from castle import aigr

from ._machinery import Machinery

# A few abstract sub-types
class _M_DirectCall(Machinery): pass            # Abstract
class _M_DC_dict(_M_DirectCall): pass           # Abstract


# load some build-in Machineries
from .chained_dict_DCM import M_DC_chained_dict
from .flat_dict_DCM    import M_DC_flat_dict
from .tuple_DCM        import M_DC_tuple
from .list_DCM         import M_DC_list




