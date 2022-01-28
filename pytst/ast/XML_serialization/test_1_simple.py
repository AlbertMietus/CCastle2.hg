import pytest
from xml.etree import ElementTree as ET
import logging; logger = logging.getLogger(__name__)

from castle.ast import  peg, serialization

@pytest.fixture
def xml_serialize():
    return serialization.Serialize('xml').serialize


def assert_xml_Element(txt, tag,
                       version="0.0",
                       **attribs,):
    tree = ET.fromstring(txt)
    if version:
        assert tree.attrib['version'] == version
    founds = tree.findall(tag)
    assert len(founds) == 1, f"Expected only one element; got: {len(founds)} :{founds}"
    found = founds[0]
    logger.debug(f'XXX1 tag={tag}:: found={found}')
    for attrib, value in attribs.items():
        logger.debug(f'XXX2 tag={tag}:: attrib={attrib}, value={value}')
        assert found.attrib[attrib] == value

def test_ID(xml_serialize):
    txt = xml_serialize(peg.ID(name='demo_ID'))
    assert_xml_Element(txt, tag='ID', name='demo_ID')

def test_StrTerm(xml_serialize):
    txt = xml_serialize(peg.StrTerm(value='demo string'))
    assert_xml_Element(txt, tag='StrTerm', value='demo string')

def test_RegExpTerm(xml_serialize):
    txt = xml_serialize(peg.RegExpTerm(value='demo RegExp'))
    assert_xml_Element(txt, tag='RegExpTerm', value='demo RegExp')

def test_Sequence_1(xml_serialize):
    e1 = peg.ID(name='ID_1')
    txt= xml_serialize(peg.Sequence(value=[e1]))
    logger.debug(f'XML:: {txt}')
    assert_xml_Element(txt, tag='Sequence')
    assert_xml_Element(txt, tag='.//ID', name='ID_1')

def test_Sequence_1(xml_serialize):
    n1, v2, v3 = 'ID_1', 'str_2', 'regexp_3'
    e1 = peg.ID(name=n1)
    e2 = peg.StrTerm(value=v2)
    e3 = peg.RegExpTerm(value=v3)

    txt= xml_serialize(peg.Sequence(value=[e1, e2, e3]))
    logger.debug(f'XML:: {txt}')

    assert_xml_Element(txt, tag='Sequence')
    assert_xml_Element(txt, tag='.//ID', name=n1)
    assert_xml_Element(txt, tag='.//StrTerm', value=v2)
    assert_xml_Element(txt, tag='.//RegExpTerm', value=v3)

