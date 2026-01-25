# (C) Albert Mietus, 2025,2026- Part of Castle/CCastle project
import logging; logger = logging.getLogger(__name__)
import pytest

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
        txt = f.read()
    if False:
        print(f"\n\n====={module}::{file}=====")
        print(txt)
        print("=====")

    comp = castle_parser(txt)
    logger.debug(f"{txt=} ==> {comp=}")
    assert False
