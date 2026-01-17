# (C) Albert Mietus, 2026- Part of Castle/CCastle project
import logging; logger = logging.getLogger(__name__)
import pytest

from . import *
from castle import aigr

def test_0(castle_parser):
    txt = """\
protocol StartSieve :EventProtocol {
     runTo(max :int);
     newMax(max :int);
}
protocol SimpleSieve :EventProtocol {
     input(try: int);
}
component Generator : Component {
  port controll :StartSieve<in>;
  port outlet   :SimpleSieve<out>;
}
"""
    N=3
    interfaces = castle_parser(txt, start='interface_definitions')
    logger.debug(f"{txt=} ==> {interfaces=}")
    assert isinstance(interfaces, list) and len(interfaces) == N, f"Expecting a list of {N}, {interfaces=}"

    logger.debug(f"{interfaces[0]=}")
    verify_EventProtocol(interfaces[0], name="StartSieve", base='EventProtocol', events_spec=[
        ('runTo',  [('max', 'int'),]),
        ('newMax', [('max', 'int'),])])

    logger.debug(f"{interfaces[1]=}")
    verify_EventProtocol(interfaces[1], name="SimpleSieve", base='EventProtocol', events_spec=[
        ('input', [('try', 'int'),])])

    logger.debug(f"{interfaces[2]=}")
    gen=interfaces[2]
    verify_ComponentInterface(gen, name="Generator", base="Component", ports=2)

    controll, outlet = gen.ports[0], gen.ports[1]
    verify_Port(controll, name="controll", type="StartSieve",  direction=aigr.PortDirection.In)
    verify_Port(outlet,   name="outlet",   type="SimpleSieve", direction=aigr.PortDirection.Out)

