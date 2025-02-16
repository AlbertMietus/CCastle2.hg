import pytest
import logging; logger = logging.getLogger(__name__)

from castle.ast import grammar

from . import xml_serialize #@pytest.fixture
from . import assert_xml_Element, StdSequence_withAsserts


def test_ID(xml_serialize):
    txt = xml_serialize(grammar.ID(name='demo_ID'))
    assert_xml_Element(txt, tag='ID', name='demo_ID')

def test_StrTerm(xml_serialize):
    txt = xml_serialize(grammar.StrTerm(value='demo string'))
    assert_xml_Element(txt, tag='StrTerm', value='demo string')

def test_RegExpTerm(xml_serialize):
    txt = xml_serialize(grammar.RegExpTerm(value='demo RegExp'))
    assert_xml_Element(txt, tag='RegExpTerm', value='demo RegExp')

def test_Sequence_1(xml_serialize):
    e1 = grammar.ID(name='ID_1')
    txt = xml_serialize(grammar.Sequence(children=[e1]))
    logger.debug(f'XML:: {txt}')
    assert_xml_Element(txt, tag='Sequence')
    assert_xml_Element(txt, tag='.//ID', name='ID_1')


def test_Rule_1ID(xml_serialize):
    rule_name = "RuleName"
    xref = "cross_ref"
    expr = grammar.Sequence(children=[grammar.ID(name=xref)])

    txt = xml_serialize(grammar.Rule(name=grammar.ID(name=rule_name), expr=expr))
    logger.debug(f'XML:: {txt}')

    assert_xml_Element(txt, tag='Rule', name=rule_name)
    assert_xml_Element(txt, tag='.//ID', name=xref)


def test_OC_long(xml_serialize): # e1 | e2a e2b e2c
    e1, seq = grammar.ID(name='single_ID'), StdSequence_withAsserts()
    txt = xml_serialize(grammar.OrderedChoice(children=[e1, seq.seq]))
    logger.debug(f'XML:: {txt}')

    assert_xml_Element(txt, tag='OrderedChoice', child_count=2)


def test_OC3(xml_serialize): # e1 | e2 | e2
    e1, e2, e3 = grammar.ID(name='ID_1'), grammar.StrTerm(value='str_2'), grammar.RegExpTerm(value='regexp_3')
    txt = xml_serialize(grammar.OrderedChoice(children=[e1,e2,e3]))
    logger.debug(f'XML:: {txt}')
    assert_xml_Element(txt, tag='OrderedChoice', child_count=3)


def verify_Predicate(xml_serialize, grammarPredicate, tagName):
    txt = xml_serialize(grammarPredicate(expr=grammar.ID(name="PartOfSomePredicate")))
    logger.debug(f'XML:: {txt}')
    assert_xml_Element(txt, tag=tagName, child_count=1)

def test_AndPredicate(xml_serialize): verify_Predicate(xml_serialize, grammar.AndPredicate, 'AndPredicate')
def test_NotPredicate(xml_serialize): verify_Predicate(xml_serialize, grammar.NotPredicate, 'NotPredicate')


