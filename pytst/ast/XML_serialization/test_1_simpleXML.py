import pytest
from xml.etree import ElementTree as ET
import logging; logger = logging.getLogger(__name__)

from castle.ast import  peg, serialization

from . import StdSequence_withAsserts, assert_xml_Element, assert_QuantityGroup, assert_QuantityID


@pytest.fixture
def xml_serialize():
    return serialization.Serialize('xml').serialize



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
    seq = StdSequence_withAsserts()
    txt= xml_serialize(seq.seq)
    logger.debug(f'XML:: {txt}')

    assert_xml_Element(txt, tag='Sequence')
    seq.assert_xml_Element(txt)


def test_Rule_1ID(xml_serialize):
    rule_name = "RuleName"
    xref = "cross_ref"
    expr = peg.Sequence(value=[peg.ID(name=xref)])

    txt = xml_serialize(peg.Rule(name=peg.ID(name=rule_name), expr=expr))
    logger.debug(f'XML:: {txt}')

    assert_xml_Element(txt, tag='Rule', name=rule_name)
    assert_xml_Element(txt, tag='.//ID', name=xref)


def test_Rule_Sequence(xml_serialize):
    rule_name = "Rule_Sequence"
    seq = StdSequence_withAsserts()

    txt = xml_serialize(peg.Rule(name=peg.ID(name=rule_name), expr=seq.seq))
    logger.debug(f'XML:: {txt}')

    assert_xml_Element(txt, tag='Rule', name=rule_name)
    seq.assert_xml_Element(txt)


def test_Rules(xml_serialize):
    r1 = peg.Rule(name=peg.ID(name='rule_1'), expr=peg.Sequence(value=[peg.ID(name='id1')]))
    r2 = peg.Rule(name=peg.ID(name='rule_2'), expr=peg.Sequence(value=[peg.StrTerm(value='str2')]))

    txt = xml_serialize(peg.Rules(children=[r1,r2]))
    logger.debug(f'XML:: {txt}')

    tree = ET.fromstring(txt)
    assert len(tree.findall('.//Rule')) == 2
    assert len(tree.findall('.//ID')) == 1
    assert len(tree.findall('.//StrTerm')) == 1

    assert  tree.findall('.//Rule[1]')[0].attrib['name'] == 'rule_1'
    assert  tree.findall('.//Rule[2]//StrTerm')[0].attrib['value'] == 'str2'


def test_OptionalSeq(xml_serialize):   assert_QuantityGroup(xml_serialize, peg.Optional, 'Optional')  			##  ` ( ...)? `
def test_ZeroOrMoreSeq(xml_serialize): assert_QuantityGroup(xml_serialize, peg.ZeroOrMore, 'ZeroOrMore')		##  ` ( ...)* `
def test_OneOrMoreSeq(xml_serialize):  assert_QuantityGroup(xml_serialize, peg.OneOrMore, 'OneOrMore')			##  ` ( ...)+ `
def test_UnorderedGroup(xml_serialize): assert_QuantityGroup(xml_serialize, peg.UnorderedGroup, 'UnorderedGroup')  	##  ` ( ...)# ` # Only useful for a group/sequence!!


def test_OptionalID(xml_serialize):   assert_QuantityID(xml_serialize, peg.Optional, 'Optional')
def test_ZeroOrMoreID(xml_serialize): assert_QuantityID(xml_serialize, peg.ZeroOrMore, 'ZeroOrMore')
def test_OneOrMoreID(xml_serialize):  assert_QuantityID(xml_serialize, peg.OneOrMore, 'OneOrMore')
## A bit uncommon: unordered group  of ONE  :`` Always#`` but it should work
def test_UnorderedID(xml_serialize):  assert_QuantityID(xml_serialize, peg.UnorderedGroup, 'UnorderedGroup', 'strange')


@pytest.mark.xfail(reason="Can't test as peg.OrderedChoice() isn't implemented")
def test_OrderedChoice(xml_serialize): # e1 | e2 | e2
    e1 = peg.ID(name='ID_1')
    e2 = peg.StrTerm(value='str_2')
    e3 = peg.RegExpTerm(value='regexp_3')
    txt = xml_serialize(peg.OrderedChoice())                            # not implemented; never peg.OrderedChoice is never called

    assert False
