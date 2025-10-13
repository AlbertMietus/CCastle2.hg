# (C) Albert Mietus, 2025. Part of Castle/CCastle project

import logging; logger = logging.getLogger(__name__)
import pytest

from castle import aigr
from castle.writers import RPy
from castle.aigr_extra.scaffolding import  ScaffolderNameSpace

from castle.TESTDOUBLES.aigr.HelloWorlds.credible.HelloWorld import Hello_World

@pytest.fixture
def wrapped_Hello_World():
    return ScaffolderNameSpace(Hello_World)

def test_0_dummy_HW():
    "Just check the aigr-TestDouble can be read"
    assert isinstance(Hello_World, aigr.Source_NS),  f"Unexpected class: {Hello_World}"
    assert Hello_World.name == 'HelloWorld'

def test_1_all_inTopNS(wrapped_Hello_World):
    for (name, T) in [
            ('SetLabel',            aigr.EventProtocol),
            ('component_Credible',  aigr.ComponentInterface),
            ('Credible',            aigr.ComponentImplementation),
            ('__impliciet_Main_Credible_HelloWorld',  aigr.ComponentInterface),
            ('Credible_HelloWorld',   aigr.ComponentImplementation),
            ]:
        node = wrapped_Hello_World.findNode(name)
        assert node, f"Can't find node for for {name}"
        assert isinstance(node, T), f"Node name={name} isn't expected class - got {node.__class__.__name__}, expected {T.__name__}"

