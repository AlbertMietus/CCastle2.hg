import pytest
import logging; logger = logging.getLogger(__name__)

from castle.ast import peg

from . import xml_serialize #@pytest.fixture
from . import assert_xml_Element, StdSequence_withAsserts

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
