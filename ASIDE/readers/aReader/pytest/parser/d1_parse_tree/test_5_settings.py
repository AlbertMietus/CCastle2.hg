import pytest
import logging;logger = logging.getLogger(__name__)

from castle.readers.parser.grammar import language as grammar

import arpeggio
RE, S = arpeggio.RegExMatch, arpeggio.StrMatch                          # shortcut

from . import parse

def verify_setting(txt, name=None, value=None):
    parse_tree = parse(txt, grammar.setting)

    assert isinstance(parse_tree.rule, arpeggio.Sequence) and parse_tree.rule_name == "setting"
    assert len(parse_tree) == 4, "A setting is always a sequence of 4"
    assert str(parse_tree[1]) == "="
    assert str(parse_tree[3]) == ";"

    if name:  assert str(parse_tree[0]) == name
    if value: assert str(parse_tree[2]) == value

def test_setting_str0():	verify_setting("aSet = 'iets als dit' ;")
def test_setting_int1():	verify_setting("anInt = 42;",  name='anInt', value="42")
def test_setting_float1():	verify_setting("f = 3.14;",    name='f',    value="3.14")
def test_setting_compl1():	verify_setting("c = 3.14+j3;", name='c',    value="3.14+j3")
