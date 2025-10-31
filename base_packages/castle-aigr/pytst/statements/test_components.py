 # (C) Albert Mietus, 2024. Part of Castle/CCastle project

import pytest
from .. import  Dummy, verifyMark

from castle.aigr import ComponentImplementation
from castle.aigr import ComponentInterface, Port
from castle.aigr import Body, ID


def verifyKidsTypes(comp):
    if isinstance (comp, ComponentInterface):
        assert isinstance(comp.based_on, (ComponentInterface, type(None)))
        assert isinstance(comp.ports, (list, tuple))
        for p in comp.ports:
            assert isinstance(p, Port)
    elif isinstance (comp, ComponentImplementation):
        # Note: a Componentimplementation has no body, but has a namespace (``_hasScope``)
        assert isinstance(comp.interface, (ComponentInterface, type(None)))
        assert isinstance(comp.parameters, tuple)
    else:
        assert False, f"{comp} is not a comp (ComponentInterface or ComponentImplementation)"


def test_0a_Interface_kids():
    comp = ComponentInterface(ID('KW_component'))
    verifyKidsTypes(comp)

def test_0b_Implementation_kids():
    comp = ComponentImplementation(ID('KW_implement'))
    verifyKidsTypes(comp)


