import pytest
from xml.etree import ElementTree as ET
import logging; logger = logging.getLogger(__name__)

from castle.ast import  peg, serialization

from . import StdSequence_withAsserts, assert_xml_Element


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
    txt = xml_serialize(peg.Sequence(children=[e1]))
    logger.debug(f'XML:: {txt}')
    assert_xml_Element(txt, tag='Sequence')
    assert_xml_Element(txt, tag='.//ID', name='ID_1')


def test_Sequence_3(xml_serialize):
    seq = StdSequence_withAsserts()
    txt = xml_serialize(seq.seq)
    logger.debug(f'XML:: {txt}')

    assert_xml_Element(txt, tag='Sequence')
    seq.assert_xml_Element(txt)


def test_Rule_1ID(xml_serialize):
    rule_name = "RuleName"
    xref = "cross_ref"
    expr = peg.Sequence(children=[peg.ID(name=xref)])

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


def test_ParseRules(xml_serialize):
    r1 = peg.Rule(name=peg.ID(name='rule_1'), expr=peg.Sequence(children=[peg.ID(name='id1')]))
    r2 = peg.Rule(name=peg.ID(name='rule_2'), expr=peg.Sequence(children=[peg.StrTerm(value='str2')]))

    txt = xml_serialize(peg.Rules(children=[r1,r2]))                    # Use generic 'Rules' not ParseRules/Settings
    logger.debug(f'XML:: {txt}')

    tree = ET.fromstring(txt)
    assert len(tree.findall('.//Rule')) == 2
    assert len(tree.findall('.//ID')) == 1
    assert len(tree.findall('.//StrTerm')) == 1

    assert  tree.findall('.//Rule[1]')[0].attrib['name'] == 'rule_1'
    assert  tree.findall('.//Rule[2]//StrTerm')[0].attrib['value'] == 'str2'



def verify_QuantityGroup(xml_serialize, pegGrp, tagName):
    seq = StdSequence_withAsserts()
    txt = xml_serialize(pegGrp(expr=seq.seq))
    logger.debug(f'XML:: {txt}')

    assert_xml_Element(txt, tagName)
    seq.assert_xml_Element(txt)

def test_OptionalSeq(xml_serialize):    verify_QuantityGroup(xml_serialize, peg.Optional, 'Optional')  			##  ` ( ...)? `
def test_ZeroOrMoreSeq(xml_serialize):  verify_QuantityGroup(xml_serialize, peg.ZeroOrMore, 'ZeroOrMore')		##  ` ( ...)* `
def test_OneOrMoreSeq(xml_serialize):   verify_QuantityGroup(xml_serialize, peg.OneOrMore, 'OneOrMore')			##  ` ( ...)+ `
def test_UnorderedGroup(xml_serialize): verify_QuantityGroup(xml_serialize, peg.UnorderedGroup, 'UnorderedGroup')  	##  ` ( ...)# ` # Only useful for a group/sequence!!


def verify_QuantityID(xml_serialize, pegGrp, tagName, id_name='JustAName'):
    txt = xml_serialize(pegGrp(expr=peg.ID(name=id_name)))
    logger.debug(f'XML:: {txt}')

    assert_xml_Element(txt, tagName)
    assert_xml_Element(txt, tag='.//ID', name=id_name)

def test_OptionalID(xml_serialize):    verify_QuantityID(xml_serialize, peg.Optional, 'Optional')
def test_ZeroOrMoreID(xml_serialize):  verify_QuantityID(xml_serialize, peg.ZeroOrMore, 'ZeroOrMore')
def test_OneOrMoreID(xml_serialize):   verify_QuantityID(xml_serialize, peg.OneOrMore, 'OneOrMore')
def test_UnorderedID(xml_serialize):   verify_QuantityID(xml_serialize, peg.UnorderedGroup, 'UnorderedGroup', 'strange') ## A bit uncommon: an unordered group of ONE! But it should work.



def test_OC3(xml_serialize): # e1 | e2 | e2
    e1, e2, e3 = peg.ID(name='ID_1'), peg.StrTerm(value='str_2'), peg.RegExpTerm(value='regexp_3')
    txt = xml_serialize(peg.OrderedChoice(children=[e1,e2,e3]))
    logger.debug(f'XML:: {txt}')

    assert_xml_Element(txt, tag='OrderedChoice', child_count=3)


def test_OC_long(xml_serialize): # e1 | e2a e2b e2c
    e1, seq = peg.ID(name='single_ID'), StdSequence_withAsserts()
    txt = xml_serialize(peg.OrderedChoice(children=[e1, seq.seq]))
    logger.debug(f'XML:: {txt}')

    assert_xml_Element(txt, tag='OrderedChoice', child_count=2)

def verify_Predicate(xml_serialize, pegPredicate, tagName):
    txt = xml_serialize(pegPredicate(expr=peg.ID(name="PartOfSomePredicate")))
    logger.debug(f'XML:: {txt}')

    assert_xml_Element(txt, tag=tagName, child_count=1)

def test_AndPredicate(xml_serialize): verify_Predicate(xml_serialize, peg.AndPredicate, 'AndPredicate')
def test_NotPredicate(xml_serialize): verify_Predicate(xml_serialize, peg.NotPredicate, 'NotPredicate')


def verify_setting_NumVal(xml_serialize, number):
    txt = xml_serialize(peg.Number(value=number))
    logger.debug(f'XML:: {txt}')
    assert_xml_Element(txt, tag='Number', text=number)

def test_setting_NumVal_int(xml_serialize):		verify_setting_NumVal(xml_serialize, '42')
def test_setting_NumVal_float(xml_serialize):		verify_setting_NumVal(xml_serialize, '3.14')
def test_setting_NumVal_complex1(xml_serialize):	verify_setting_NumVal(xml_serialize, '-1+j1')
def test_setting_NumVal_complex2(xml_serialize):	verify_setting_NumVal(xml_serialize, '+1-i1')


def verify_Number_setting(xml_serialize, name, value, pegVal=peg.Number):
    txt = xml_serialize(peg.Setting(name=peg.ID(name=name), value=pegVal(value=value)))
    logger.debug(f'XML:: {txt}')

    assert_xml_Element(txt, tag='.//Setting/ID', name=name)
    assert_xml_Element(txt, tag='.//Setting/Number', text=value)

def test_setting_int(xml_serialize):		verify_Number_setting(xml_serialize, name='anInt', value='42')
def test_setting_float(xml_serialize):		verify_Number_setting(xml_serialize, name='anInt', value='3.14')
def test_setting_complex(xml_serialize):	verify_Number_setting(xml_serialize, name='anInt', value='1+j1')


def verify_txt_setting(xml_serialize, name, pegTxt, value, tag):
    txt = xml_serialize(peg.Setting(name=peg.ID(name=name), value=pegTxt(value=value)))
    logger.debug(f'XML:: {txt}')

    assert_xml_Element(txt, tag='.//Setting/ID', name=name)
    assert_xml_Element(txt, tag=f'.//Setting/{tag}', value=value)

def test_setting_StrTerm(xml_serialize):	verify_txt_setting(xml_serialize, name='string', pegTxt=peg.StrTerm, value='StrVal', tag='StrTerm')
def test_setting_RegExTerm(xml_serialize):	verify_txt_setting(xml_serialize, name='regexp', pegTxt=peg.RegExpTerm, value='/RegExp/', tag='RegExpTerm')


def test_setting_XID(xml_serialize):
    name, xref = 'SetTo', 'anOtherID'
    txt = xml_serialize(peg.Setting(name=peg.ID(name=name), value=peg.ID(name=xref)))
    logger.debug(f'XML:: {txt}')

    assert_xml_Element(txt, tag='.//Setting/ID[1]', name=name)
    assert_xml_Element(txt, tag='.//Setting/ID[2]', name=xref)

def test_Settings(xml_serialize):
    name_1, val_1 = 's1', '42'
    name_2, val_2 = 's2', '2.71828'
    s1 = peg.Setting(name=peg.ID(name=name_1), value=peg.Number(value=val_1))
    s2 = peg.Setting(name=peg.ID(name=name_2), value=peg.Number(value=val_2))

    txt = xml_serialize(peg.Rules(children=[s1,s2]))                    # Use generic 'Rules' not ParseRules/Settings
    logger.debug(f'XML:: {txt}')

    assert_xml_Element(txt, tag=f".//Setting/ID[@name='{name_1}']/../Number", text=val_1)
    assert_xml_Element(txt, tag=f".//Setting/ID[@name='{name_2}']/../Number", text=val_2)

    tree = ET.fromstring(txt)
    assert len(tree.findall('.//Setting')) == 2
    assert len(tree.findall('.//ID')) == 2



    
