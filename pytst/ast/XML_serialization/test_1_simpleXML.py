import pytest
from xml.etree import ElementTree as ET
import logging; logger = logging.getLogger(__name__)

from castle.ast import  peg, serialization


class StdSequence_withAsserts:
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


def assert_xml_Element(txt, tag,
                       version="0.0",
                       **attribs,):
    """Partially verify an xml-string; focusing on 'tag' -- a real tag, or a (limited) XPATH-expression.

    This `tag` (expression) should result in a single hit!. *Use e.g `[0]` as suffix to select one from a list*.
    Pass ``key=value`` **attribs** to verify the found tag has those attribs and values
    """

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

def assert_QuantityGroup(xml_serialize, pegGrp, tagName):
    seq = StdSequence_withAsserts()
    txt = xml_serialize(pegGrp(expr=seq.seq))
    logger.debug(f'XML:: {txt}')

    assert_xml_Element(txt, tagName)
    seq.assert_xml_Element(txt)


def test_OptionalSeq(xml_serialize):   assert_QuantityGroup(xml_serialize, peg.Optional, 'Optional')  			##  ` ( ...)? `
def test_ZeroOrMoreSeq(xml_serialize): assert_QuantityGroup(xml_serialize, peg.ZeroOrMore, 'ZeroOrMore')		##  ` ( ...)* `
def test_OneOrMoreSeq(xml_serialize):  assert_QuantityGroup(xml_serialize, peg.OneOrMore, 'OneOrMore')			##  ` ( ...)+ `
def test_UnorderedGroup(xml_serialize): assert_QuantityGroup(xml_serialize, peg.UnorderedGroup, 'UnorderedGroup')  	##  ` ( ...)# ` # Only useful for a group/sequence!!


def assert_QuantityID(xml_serialize, pegGrp, tagName, id_name='JustAName'):
    txt = xml_serialize(pegGrp(expr=peg.ID(name=id_name)))
    logger.debug(f'XML:: {txt}')

    assert_xml_Element(txt, tagName)
    assert_xml_Element(txt, tag='.//ID', name=id_name)

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
