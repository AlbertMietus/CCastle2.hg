 # (C) Albert Mietus, 2024. Part of Castle/CCastle project

import pytest
from .. import  Dummy, verifyMark, verifyKids

from castle.aigr import ComponentImplementation
from castle.aigr import ComponentInterface, Port
from castle.aigr import Body, ID


def verifyKidsTypes(comp):
    if isinstance (comp, ComponentInterface):
        assert isinstance(comp.based_on, ComponentInterface)
        assert isinstance(comp.ports, (list, tuple))
        for p in comp.ports:
            assert isinstance(p, Port)
    elif isinstance (comp, ComponentImplementation):
        assert isinstance(comp.interface, (ComponentInterface, type(None)))
        assert isinstance(comp.parameters, tuple)
        assert isinstance(comp.body, (Body, type(None)))
    else:
        assert False, f"{comp} is not a comp (ComponentInterface or ComponentImplementation)"


def test_0a_Interface_kids():
    comp = ComponentInterface(ID('KW_component'))
    verifyKidsTypes(comp)
    verifyKids(comp)

def test_0b_Implementation_kids():
    comp = ComponentImplementation(ID('KW_implement'))
    verifyKidsTypes(comp)
    verifyKids(comp)

