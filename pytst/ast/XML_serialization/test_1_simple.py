import pytest
from xml.etree import ElementTree as ET

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
    for attrib, value in attribs.items():
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
