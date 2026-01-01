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




def verify_ComponentImplementation(comp, name, parameters=0, handlers=0):
    assert isinstance(comp, aigr.ComponentImplementation)
    # direct attributes
    assert comp.name == name
    assert comp.interface is None               #XXXX
    assert len(comp.parameters) == parameters
    assert len(comp.handlers)   == handlers
    # inherited via _hasScope --|> Scope --|> _NameSpace
    assert isinstance(comp._ns,      dict)
    assert isinstance(comp.outer_ns, (dict, type(None))) #.outer_ns is a ref that can be empty ...
    assert comp.outer_ns is None                         # .. Here it is/should be
