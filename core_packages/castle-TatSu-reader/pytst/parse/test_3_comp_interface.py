# (C) Albert Mietus, 2025,2026- Part of Castle/CCastle project
import logging; logger = logging.getLogger(__name__)
import pytest

import typing as PTH                                                                                  # Python TypeHints
from castle import aigr

from . import *

def test_1a_EmptyComponent(castle_parser):
    txt = """\
component EmptyComponent
{
}
"""
    comp = castle_parser(txt, start='component_interface')
    logger.debug(f"{txt=} ==> {comp=}")
    verify_ComponentInterface(comp, name="EmptyComponent")

def test_1b_ComponentWithBase(castle_parser):
    txt = """\
component ComponentWithBase: aBase
{
}
"""
    comp = castle_parser(txt, start='component_interface')
    logger.debug(f"{txt=} ==> {comp=}")
    verify_ComponentInterface(comp, name="ComponentWithBase", base='aBase')

def verify_ComponentInterface(comp, name, base:PTH.Optional[aigr.ID]=None, ports=0):
    assert isinstance(comp, aigr.ComponentInterface), f"Expecting an ComponentInterface, got: {comp}"
    # direct attributes
    assert comp.name == name
    assert comp.based_on is None or str(comp.based_on) == base
    assert len(comp.ports) == ports
