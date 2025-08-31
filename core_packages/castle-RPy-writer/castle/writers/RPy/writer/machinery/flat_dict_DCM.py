# (C) Albert Mietus, 2025. Part of Castle/CCastle project

import logging; logger = logging.getLogger(__name__)
import typing as PTH                                                                                  # Python TypeHints

from castle import aigr
from castle.writers.RPy.aid import Block

from . import Machinery, _M_DC_dict

@Machinery.register('DirectCall.dict.flat', "flat.dict", "flat_dict", "flat-dict")
class M_DC_flat_dict(_M_DC_dict): 
  pass
