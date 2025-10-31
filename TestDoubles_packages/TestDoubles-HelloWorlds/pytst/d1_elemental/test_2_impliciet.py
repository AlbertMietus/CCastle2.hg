# (C) Albert Mietus 2025, Part of Castle/CCastle project

import logging; logger = logging.getLogger(__name__)
import pytest

from castle import aigr
from castle.aigr_extra.scaffolding import ScaffolderNameSpace
from . import elemental, HW

#TEST:
#  ///CastleCode
#  @impliciet ///GAM: This `rewriter` auto-generates ``component Elemental_HelloWorld``
#  implement Elemental_HelloWorld
#  {
#  ...

@pytest.fixture
def implicietComponent(HW):
    component = HW.interface
    return  component


def test_1_component_has_implicietInterface(implicietComponent):
    assert isinstance(implicietComponent, aigr.ComponentInterface)

def test_2_implicietDef_name_is_implemention_name(implicietComponent, HW):
    assert str(implicietComponent.name) == str(HW.name)
    assert str(implicietComponent.name) == "Elemental_HelloWorld"

def test_3_implicietDef_has_no_ports(implicietComponent):
    assert implicietComponent.ports == []

def test_4_implicietDef_is_basedOn(implicietComponent):
    base = implicietComponent.based_on
    assert isinstance(base, (aigr.ComponentInterface, type(None))) # this is a general check; here we expect it None
    assert base is None

def test_5a_implicietDef_not_with_typicalName_in_NS(implicietComponent, elemental):
    """An impliciet Component Interface is't in the (`elemental`) NS with it 'typically' name (as the ComponentImplementation is)"""
    typicalName = implicietComponent.name
    node = ScaffolderNameSpace(elemental).findNode(typicalName)
    assert node is not implicietComponent

def test_5_implicietDef_in_NS(implicietComponent, elemental):
    elemental = ScaffolderNameSpace(elemental)
    typicalName = str(implicietComponent.name)
    d = elemental.find_byType(aigr.ComponentInterface)
    assert len(d) >= 1, f"Expect to have at leat one ComponentImplementation; found: {len(d)}/{len(elemental)}"
    found = list((k,v) for k,v in d.items() if str(v.name) ==  typicalName)
    assert len(found) == 1, f"Expect to have exactly one ComponentImplementation; found: {len(d)}/{len(elemental)}"


