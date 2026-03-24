# (C) Albert Mietus, 2025,2026- Part of Castle/CCastle project
import logging; logger = logging.getLogger(__name__)
import pytest

from castle.aigr import ComponentInterface, ComponentImplementation
from castle.aigr_extra.scaffolding import ScaffolderNameSpace

from . import castle_parser

###
### test_0*: Same as before ...(but now a CastleFile)
###          Acts as a base to the real test (1+)
def test_0a_InterfaceOnly(castle_parser):
    txt = """component InterfaceOnly {}"""
    ns = castle_parser(txt)
    logger.debug(f"{txt=} ==> {ns=}")
    wrapped = ScaffolderNameSpace(ns)
    comp = wrapped.findNode('InterfaceOnly')
    assert isinstance(comp, ComponentInterface)

def test_0b_ImplementOnly(castle_parser):
    txt = """implement ImplementOnly {} """
    ns = castle_parser(txt)
    logger.debug(f"{txt=} ==> {ns=}")
    wrapped = ScaffolderNameSpace(ns)
    comp = wrapped.findNode('ImplementOnly')
    assert isinstance(comp, ComponentImplementation)



def test_1_Given_InterfaceAndImplementation_theImplementation_isNS(castle_parser):
    txt = """\
component InterfaceAndImplementation {}
implement InterfaceAndImplementation {}"""
    ns = castle_parser(txt)
    logger.debug(f"{txt=} ==> {ns=}")
    wrapped = ScaffolderNameSpace(ns)
    comp = wrapped.findNode('InterfaceAndImplementation')
    assert isinstance(comp, ComponentImplementation), f"When implement & component are in one file, the ComponentImplementation should be in the ns"
    assert isinstance(comp.interface, ComponentInterface), f".interface should give interface, but doesn't: {comp.interface=}"

def test_2_ReverseOrder_theImplementation_is_still_inNS(castle_parser):
    txt = """\
implement ReverseOrder {}
component ReverseOrder {}"""
    ns = castle_parser(txt)
    logger.debug(f"{txt=} ==> {ns=}")
    wrapped = ScaffolderNameSpace(ns)
    comp = wrapped.findNode('ReverseOrder')
    assert isinstance(comp, ComponentImplementation), f"Wrong type {type(comp).__name__}:: When implement & component are in one file, the ComponentImplementation should be in the ns"
    assert isinstance(comp.interface, ComponentInterface), f".interface should give interface, but doesn't: {comp.interface=}"
