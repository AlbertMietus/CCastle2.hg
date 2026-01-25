# (C) Albert Mietus, 2025,2026- Part of Castle/CCastle project
import logging; logger = logging.getLogger(__name__)
import pytest

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
    verify_ComponentInterface(comp, name="ComponentWithPorts", ports_spec=[
         # name        type            #direction
        ("someData",   "a_type",       aigr.PortDirection.In),
        ("anEvent",    "StartSieve",   aigr.PortDirection.In),
        ("sender",     "Out",          aigr.PortDirection.Out),
    ])


def test_3_ComponentWith1Ports(castle_parser):
    txt = """\
component ComponentWith1Port {
    port p1 :a_type<in>;
}"""
    comp = castle_parser(txt, start='component_definition')
    logger.debug(f"{txt=} ==> {comp=}")
    verify_ComponentInterface(comp, name="ComponentWith1Port", ports_spec=[
         # name        type            #direction
        ("p1",         "a_type",       aigr.PortDirection.In),
        ])



def test_4_DocComponent(castle_parser):
    txt="""\
component Demo
'''Doc the component (interface)'''
{}
"""
    got = castle_parser(txt, start='component_definition')
    assert isinstance(got, aigr.ComponentInterface)
    assert False, "XXX: docstring"

