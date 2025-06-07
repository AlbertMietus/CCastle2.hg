# (C) Albert Mietus, 2025. Part of Castle/CCastle project

import logging; logger = logging.getLogger(__name__)
import typing as PTH                                                                                  # Python TypeHints

from castle import aigr
from castle.writers.RPy.aid import Block

from . import Machinery, _M_DirectCall


@Machinery.register('DirectCall.tuple', "tuple")
class  M_DC_tuple(_M_DirectCall):
    pass

