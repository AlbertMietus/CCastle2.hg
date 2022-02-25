import pytest
import logging; logger = logging.getLogger(__name__)

from castle.ast import peg

from . import xml_serialize #@pytest.fixture
from . import assert_xml_Element, StdSequence_withAsserts


def verify_QuantityID(xml_serialize, pegGrp, tagName, id_name='JustAName'):
    txt = xml_serialize(pegGrp(expr=peg.ID(name=id_name)))
    logger.debug(f'XML:: {txt}')
    assert_xml_Element(txt, tagName)
    assert_xml_Element(txt, tag='.//ID', name=id_name)

def test_OptionalID(xml_serialize):    verify_QuantityID(xml_serialize, peg.Optional, 'Optional')
def test_ZeroOrMoreID(xml_serialize):  verify_QuantityID(xml_serialize, peg.ZeroOrMore, 'ZeroOrMore')
def test_OneOrMoreID(xml_serialize):   verify_QuantityID(xml_serialize, peg.OneOrMore, 'OneOrMore')
def test_UnorderedID(xml_serialize):   verify_QuantityID(xml_serialize, peg.UnorderedGroup, 'UnorderedGroup', 'strange') ## A bit uncommon: an unordered group of ONE! But it should work.


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


