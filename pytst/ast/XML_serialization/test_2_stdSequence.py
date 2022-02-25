import pytest
import logging; logger = logging.getLogger(__name__)

from castle.ast import peg

from . import xml_serialize #@pytest.fixture
from . import assert_xml_Element, StdSequence_withAsserts


def test_Sequence_3(xml_serialize):
    seq = StdSequence_withAsserts()
    txt = xml_serialize(seq.seq)
    logger.debug(f'XML:: {txt}')

    assert_xml_Element(txt, tag='Sequence')
    seq.assert_xml_Element(txt)


def test_Rule_Sequence(xml_serialize):
    rule_name = "Rule_Sequence"
    seq = StdSequence_withAsserts()

    txt = xml_serialize(peg.Rule(name=peg.ID(name=rule_name), expr=seq.seq))
    logger.debug(f'XML:: {txt}')

    assert_xml_Element(txt, tag='Rule', name=rule_name)
    seq.assert_xml_Element(txt)



