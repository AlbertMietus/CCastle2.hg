# (C) Albert Mietus, 2025,2026- Part of Castle/CCastle project
import logging; logger = logging.getLogger(__name__)
import pytest

from castle import aigr

from . import *

def test_1_EmptyComponent(castle_parser):
    txt = """\
implement EmptyComponent
{
}
"""
    comp = castle_parser(txt, start='implement_component')
    logger.debug(f"{txt=} ==> {comp=}")
    verify_ComponentImplementation(comp, name="EmptyComponent")


def test_2_CompWithParms(castle_parser):
    txt = """\
implement CompWithParms(p1 :t1, p2 :type2)
{
}
"""
    comp = castle_parser(txt, start='implement_component')
    logger.debug(f"{txt=} ==> {comp=}")
    verify_ComponentImplementation(comp, name="CompWithParms", parameters=2)
    for parm, name, type_ in zip(
            comp.parameters,
            ('p1', 'p2'),
            ('t1', 'type2')):
        verify_parm(parm, name, type_)

def test_3_Comp_EH_with_proto(castle_parser):
    """An event-handler can be bound to proto.event and a port. That's easy to parse (and tested here).

       The is also an option to omit the protocol-part; which can be looked up via the port.
       More complex; and tested in `test_9b_comp_mix`"""
    txt = """\
implement Comp_EH_with_proto
{
    std.invoke() on self.std {}
}"""
    comp = castle_parser(txt, start='implement_component')
    logger.debug(f"{txt=} ==> {comp=}")
    verify_ComponentImplementation(comp, name="Comp_EH_with_proto", handlers=1)

def test_4_Comp_2EH(castle_parser):
    txt = """\
implement Comp_EH2
{
    std.invoke() on self.std {}
    foo.bar() on self.foo {}
}"""
    comp = castle_parser(txt, start='implement_component')
    logger.debug(f"{txt=} ==> {comp=}")
    verify_ComponentImplementation(comp, name="Comp_EH2", handlers=2)

def test_5_Comp_method(castle_parser):
    txt = """\
implement Comp_with_local_Method
{
    local_M() {}
}"""
    comp = castle_parser(txt, start='implement_component')
    logger.debug(f"{txt=} ==> {comp=}")
    verify_ComponentImplementation(comp, name="Comp_with_local_Method", local_names=['local_M'])

