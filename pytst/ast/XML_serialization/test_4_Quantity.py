import pytest
import logging; logger = logging.getLogger(__name__)

from castle.ast import grammar

from . import xml_serialize #@pytest.fixture
from . import assert_xml_Element, StdSequence_withAsserts


def verify_QuantityID(xml_serialize, grammarGrp, tagName, id_name='JustAName'):
    txt = xml_serialize(grammarGrp(expr=grammar.ID(name=id_name)))
    logger.debug(f'XML:: {txt}')
    assert_xml_Element(txt, tagName)
    assert_xml_Element(txt, tag='.//ID', name=id_name)

def test_OptionalID(xml_serialize):    verify_QuantityID(xml_serialize, grammar.Optional, 'Optional')
def test_ZeroOrMoreID(xml_serialize):  verify_QuantityID(xml_serialize, grammar.ZeroOrMore, 'ZeroOrMore')
def test_OneOrMoreID(xml_serialize):   verify_QuantityID(xml_serialize, grammar.OneOrMore, 'OneOrMore')
def test_UnorderedID(xml_serialize):   verify_QuantityID(xml_serialize, grammar.UnorderedGroup, 'UnorderedGroup', 'strange') ## A bit uncommon: an unordered group of ONE! But it should work.


def verify_QuantityGroup(xml_serialize, grammarGrp, tagName):
    seq = StdSequence_withAsserts()
    txt = xml_serialize(grammarGrp(expr=seq.seq))
    logger.debug(f'XML:: {txt}')

    assert_xml_Element(txt, tagName)
    seq.assert_xml_Element(txt)

def test_OptionalSeq(xml_serialize):    verify_QuantityGroup(xml_serialize, grammar.Optional, 'Optional')  		##  ` ( ...)? `
def test_ZeroOrMoreSeq(xml_serialize):  verify_QuantityGroup(xml_serialize, grammar.ZeroOrMore, 'ZeroOrMore')		##  ` ( ...)* `
def test_OneOrMoreSeq(xml_serialize):   verify_QuantityGroup(xml_serialize, grammar.OneOrMore, 'OneOrMore')		##  ` ( ...)+ `
def test_UnorderedGroup(xml_serialize): verify_QuantityGroup(xml_serialize, grammar.UnorderedGroup, 'UnorderedGroup')  	##  ` ( ...)# ` # Only useful for a group/sequence!!


