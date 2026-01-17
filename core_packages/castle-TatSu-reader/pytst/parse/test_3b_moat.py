# (C) Albert Mietus, 2026- Part of Castle/CCastle project
import logging; logger = logging.getLogger(__name__)
import pytest

from . import *
from .test_3a_comp_interface import verify_ComponentInterface

def test_AGiven_CompDef_canAlsoBeParsedWith_interface_definitions(castle_parser):
    """ This the same test as 'test_3a_comp_interface.py::test_1a_EmptyComponent' but for the start.
    When `start='interface_definitions'` a list (of 1) is returned."""
    txt = """\
component EmptyComponent {
}
"""
    interfaces = castle_parser(txt, start='interface_definitions')
    logger.debug(f"{txt=} ==> {interfaces=}")
    assert isinstance(interfaces, list) and len(interfaces) == 1, f"Expecting a list of 1, got: {interfaces=}"
    verify_ComponentInterface(interfaces[0], name="EmptyComponent")



