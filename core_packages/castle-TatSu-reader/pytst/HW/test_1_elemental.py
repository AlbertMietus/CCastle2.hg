# (C) Albert Mietus, 2025,2026- Part of Castle/CCastle project
import logging; logger = logging.getLogger(__name__)
import pytest

from pprint import pprint

from importlib import resources

from . import *


@pytest.mark.xfail(reason="Dot-on-Horizon: elemental HelloWorld")
def test_1_file(castle_parser):
    """.. todo::

          * ```HelloWorld(label :string) { 			///GAM: fixed `name :type` order
                   print("Hello {label} World")
               }```

    """
    module, file  = "CastleCode.elemental", "HelloWorld.Castle"
    with resources.open_text( module, file) as f:
        logger.debug("Going to read %s", f.name)
        txt = f.read()
    if False:
        print(f"\n\n====={module}::{file}=====")
        print(txt)
        print("=====")

    eHW = castle_parser(txt)
    pprint(eHW)

    assert False, "Work to do -- but it parses!!"
