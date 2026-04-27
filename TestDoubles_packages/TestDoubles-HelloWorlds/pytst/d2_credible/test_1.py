# (C) Albert Mietus 2025, Part of Castle/CCastle project

import logging; logger = logging.getLogger(__name__)
import pytest

from castle import aigr
#from castle.aigr_extra.blend import mangle_event_handler
#from castle.aigr.tools.scaffolding import ScaffolderNameSpace

from . import credible, HW
from . import dummy


def test_0(HW):
    logger.info("Reading `Hello_World` is a test in itself")
