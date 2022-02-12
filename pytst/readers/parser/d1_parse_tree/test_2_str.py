import pytest
import logging;logger = logging.getLogger(__name__)

from castle.readers.parser import grammar

import arpeggio
RE, S = arpeggio.RegExMatch, arpeggio.StrMatch                          # shortcut

from . import parse

def verify_str(txt, pattern=[S, RE, S]):
    parse_tree = parse(txt, grammar.str_term)

    assert isinstance(parse_tree.rule, arpeggio.OrderedChoice) and parse_tree.rule_name == "str_term"
    assert len(parse_tree) == 3, "regex_term is an Ordered_Choice of always 3 Terminals"
    for e in parse_tree: assert isinstance(e, arpeggio.Terminal)

    if pattern:
        validate_pattern(parse_tree, pattern=pattern)

def validate_pattern(parse_tree, pattern):
        for e,T in zip(parse_tree,pattern):
            if T is not None: assert isinstance(e.rule, T), f"{type(e.rule).__name__}  doesn't match {T.__name__}"


def test_s1():	verify_str("'single 1'")
def test_d1():	verify_str('"double 1"')
def test_s3():	verify_str(r"'''single 3 b'''")
def test_d3():	verify_str('"""double 3"""')

def test_multiline_s(): verify_str("""'''
line 1
line 2
'''""")
def test_multiline_d(): verify_str('''"""
line 1
line 2
"""''')

def test_multiline_only3():
    import arpeggio
    with pytest.raises(arpeggio.NoMatch):
        verify_str("""'
        line 1
        line 2
        '""")
    with pytest.raises(arpeggio.NoMatch):
        verify_str('''"
        line 1
        line 2
        "''')
