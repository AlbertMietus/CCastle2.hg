import pytest
import logging;logger = logging.getLogger(__name__)

from castle.readers.parser import grammar


import arpeggio
RE, S = arpeggio.RegExMatch, arpeggio.StrMatch                          # shortcut


def parse_str(str, pattern=[S, RE, S]):
    logger.debug(f'>>{str}<<')
    parser = arpeggio.ParserPython(grammar.str_term, grammar.comment)
    tree = parser.parse(str)
    assert tree.position_end == len(str) , f"Not parsed whole input; Only: >>{str[tree.position: tree.position_end]}<<; Not: >>{str[tree.position_end:]}<<."

    assert isinstance(tree.rule, arpeggio.OrderedChoice) and tree.rule_name == "str_term"
    assert len(tree) == 3, "regex_term is an Ordered_Choice of always 3 Terminals"

    for e in tree: assert isinstance(e, arpeggio.Terminal)
    if pattern:
        for e,T in zip(tree,pattern):
            if T is not None: assert isinstance(e.rule, T), f"{type(e.rule).__name__}  doesn't match {T.__name__}"


    return tree


def test_s1():	parse_str("'single 1'")
def test_d1():	parse_str('"double 1"')
def test_s3():	parse_str(r"'''single 3 b'''")
def test_d3():	parse_str('"""double 3"""')

def test_multiline_s(): parse_str("""'''
line 1
line 2
'''""")
def test_multiline_d(): parse_str('''"""
line 1
line 2
"""''')

def test_multiline_only3():
    import arpeggio
    with pytest.raises(arpeggio.NoMatch):
        parse_str("""'
        line 1
        line 2
        '""")
    with pytest.raises(arpeggio.NoMatch):
        parse_str('''"
        line 1
        line 2
        "''')
