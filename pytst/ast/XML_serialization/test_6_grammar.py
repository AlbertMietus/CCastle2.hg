import pytest
import logging; logger = logging.getLogger(__name__)

from castle.ast import peg

from . import xml_serialize #@pytest.fixture
from . import assert_xml_Element, StdSequence_withAsserts

def test_a_Grammar_with_ParseRules_only(xml_serialize):
    name1, seq1  = 'aParseRule',  StdSequence_withAsserts()
    name2, seq2  = 'rule_2',      StdSequence_withAsserts()
    r1 = peg.Rule(name=peg.ID(name=name1), expr=seq1.seq)
    r2 = peg.Rule(name=peg.ID(name=name2), expr=seq2.seq)

    g = peg.Grammar(all_rules=(r1,r2))
    txt = xml_serialize(g)
    logger.debug(f'XML:: {txt}')

    assert_xml_Element(txt, tag='Grammar', child_count=2)
    assert_xml_Element(txt, tag='Grammar/Rule[1]', name=name1)
    assert_xml_Element(txt, tag='Grammar/Rule[2]', name=name2)

def test_a_Grammar_with_MixedRules(xml_serialize):
    name1, seq1  = 'aParseRule',  StdSequence_withAsserts()
    name2, val2  = 'setting2',    "1965"
    name3, seq3  = 'rule_3',      StdSequence_withAsserts()
    r1 = peg.Rule(name=peg.ID(name=name1), expr=seq1.seq)
    r2 = peg.Setting(name=peg.ID(name=name2), value=peg.Number(value=val2))
    r3 = peg.Rule(name=peg.ID(name=name3), expr=seq3.seq)

    g = peg.Grammar(all_rules=(r1,r2,r3))
    txt = xml_serialize(g)
    logger.debug(f'XML:: {txt}')

    assert_xml_Element(txt, tag='Grammar', child_count=3)
    assert_xml_Element(txt, tag='Grammar/Rule[1]', name=name1)
    assert_xml_Element(txt, tag='Grammar/Setting/ID', name=name2)
    assert_xml_Element(txt, tag='Grammar/Rule[2]', name=name3)

