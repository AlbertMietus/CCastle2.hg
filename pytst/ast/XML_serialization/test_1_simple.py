import pytest
from xml.etree import ElementTree as ET
import logging; logger = logging.getLogger(__name__)

from castle.ast import  peg, serialization


class Sequence:
    def __init__(self):
        self.n1, self.v2, self.v3 = 'ID_1', 'str_2', 'regexp_3'
        e1 = peg.ID(name=self.n1)
        e2 = peg.StrTerm(value=self.v2)
        e3 = peg.RegExpTerm(value=self.v3)
        self.seq = peg.Sequence(value=[e1, e2, e3])
    def assert_xml_Element(self, txt):
        assert_xml_Element(txt, tag='.//Sequence')
        assert_xml_Element(txt, tag='.//ID', name=self.n1)
        assert_xml_Element(txt, tag='.//StrTerm',value=self.v2)
        assert_xml_Element(txt, tag='.//RegExpTerm', value=self.v3)

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



def test_Sequence_3(xml_serialize):
    seq = Sequence()
    txt= xml_serialize(seq.seq)
    logger.debug(f'XML:: {txt}')

    assert_xml_Element(txt, tag='Sequence')
    seq.assert_xml_Element(txt)


def test_Rule_1ID(xml_serialize):
    rule_name = "RuleName"
    xref = "cross_ref"
    expr = peg.Sequence(value=[peg.ID(name=xref)])

    txt = xml_serialize(peg.Rule(name=rule_name, expr=expr))
    logger.debug(f'XML:: {txt}')

    assert_xml_Element(txt, tag='Rule', name=rule_name)
    assert_xml_Element(txt, tag='.//ID', name=xref)


def test_Rule_Sequence(xml_serialize):
    rule_name = "Rule_Sequence"
    seq = Sequence()

    txt = xml_serialize(peg.Rule(name=rule_name, expr=seq.seq))
    logger.debug(f'XML:: {txt}')

    assert_xml_Element(txt, tag='Rule', name=rule_name)
    seq.assert_xml_Element(txt)

@pytest.mark.xfail(reason="Not yet done")
def test_Rules(xml_serialize):
    r1 = peg.Rule(name='rule_1', expr=peg.Sequence(value=[peg.ID(name='id1')]))
    r2 = peg.Rule(name='rule_2', expr=peg.Sequence(value=[peg.StrTerm(value='str2')]))

    txt = xml_serialize(peg.Rules(children=[r1,r2]))
    logger.debug(f'XML:: {txt}')

    assert False, "not yet done"

