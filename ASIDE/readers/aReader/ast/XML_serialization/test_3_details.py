import pytest
import logging; logger = logging.getLogger(__name__)

from xml.etree import ElementTree as ET
from castle.ast import grammar

from . import xml_serialize #@pytest.fixture
from . import assert_xml_Element


def test_ParseRules(xml_serialize):
    r1 = grammar.Rule(name=grammar.ID(name='rule_1'), expr=grammar.Sequence(children=[grammar.ID(name='id1')]))
    r2 = grammar.Rule(name=grammar.ID(name='rule_2'), expr=grammar.Sequence(children=[grammar.StrTerm(value='str2')]))

    txt = xml_serialize(grammar.Rules(children=[r1,r2]))                    # Use generic 'Rules' not ParseRules/Settings
    logger.debug(f'XML:: {txt}')

    tree = ET.fromstring(txt)
    assert len(tree.findall('.//Rule')) == 2
    assert len(tree.findall('.//ID')) == 1
    assert len(tree.findall('.//StrTerm')) == 1

    assert  tree.findall('.//Rule[1]')[0].attrib['name'] == 'rule_1'
    assert  tree.findall('.//Rule[2]//StrTerm')[0].attrib['value'] == 'str2'



def test_Settings(xml_serialize):
    name_1, val_1 = 's1', '42'
    name_2, val_2 = 's2', '2.71828'
    s1 = grammar.Setting(name=grammar.ID(name=name_1), value=grammar.Number(value=val_1))
    s2 = grammar.Setting(name=grammar.ID(name=name_2), value=grammar.Number(value=val_2))

    txt = xml_serialize(grammar.Rules(children=[s1,s2]))                    # Use generic 'Rules' not ParseRules/Settings
    logger.debug(f'XML:: {txt}')

    assert_xml_Element(txt, tag=f".//Setting/ID[@name='{name_1}']/../Number", text=val_1)
    assert_xml_Element(txt, tag=f".//Setting/ID[@name='{name_2}']/../Number", text=val_2)

    tree = ET.fromstring(txt)
    assert len(tree.findall('.//Setting')) == 2
    assert len(tree.findall('.//ID')) == 2
