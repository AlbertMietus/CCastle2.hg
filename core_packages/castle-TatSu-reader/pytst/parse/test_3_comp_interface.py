# (C) Albert Mietus, 2025,2026- Part of Castle/CCastle project
import logging; logger = logging.getLogger(__name__)
import pytest

import typing as PTH                                                                                  # Python TypeHints
from castle import aigr

from . import *

def test_1a_EmptyComponent(castle_parser):
    txt = """\
component EmptyComponent {
}
"""
    comp = castle_parser(txt, start='component_definition')
    logger.debug(f"{txt=} ==> {comp=}")
    verify_ComponentInterface(comp, name="EmptyComponent")

def test_1b_ComponentWithBase(castle_parser):
    txt = """\
component ComponentWithBase: aBase {
}
"""
    comp = castle_parser(txt, start='component_definition')
    logger.debug(f"{txt=} ==> {comp=}")
    verify_ComponentInterface(comp, name="ComponentWithBase", base='aBase')


def test_2_ComponentWith2Ports(castle_parser):
    """.. note:
          * here we use the NEW, STD ``name: type`` syntax for ports
          * The syntax for event, & date (etc) ports is the same!
            The port-type (or 'kind') can be regular/data type, or a protocols (for events
          * To 'parse' (only), the protocol/type/kind doesn't need to be definded -- they are all names """
    txt = """\
component ComponentWithPorts {
    port someData :a_type<in>;
    port anEvent  :StartSieve<in>;
    port sender   :Out<out>;
}
"""
    comp = castle_parser(txt, start='component_definition')
    logger.debug(f"{txt=} ==> {comp=}")
    verify_ComponentInterface(comp, name="ComponentWithPorts", ports=3)
    verify_Port(comp.ports[0], "someData", "a_type",     aigr.PortDirection.In)
    verify_Port(comp.ports[1], "anEvent",  "StartSieve", aigr.PortDirection.In)
    verify_Port(comp.ports[2], "sender",   "Out",        aigr.PortDirection.Out)




def verify_ComponentInterface(comp, name, base:PTH.Optional[aigr.ID]=None, ports=0):
    assert isinstance(comp, aigr.ComponentInterface), f"Expecting an ComponentInterface, got: {comp}"
    # direct attributes
    assert comp.name == name
    assert comp.based_on is None or str(comp.based_on) == base
    assert len(comp.ports) == ports

def verify_Port(port, name:str, type:str, direction:aigr.PortDirection.In):
    assert isinstance(port, aigr.Port), f"{port=}"
    assert isinstance(port.name, aigr.ID) and port.name == name, f"Got: {port.name=} -- expecting {name=}"
    assert isinstance(port.type, aigr.ID) and port.type == type, f"Got: {port.type=} -- expecting {type=}"
    assert isinstance(port.direction, aigr.PortDirection) and port.direction is direction, f"Got: {port.direction=} -- expecting {direction}"

