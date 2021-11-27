import pytest
from grammar import *

import arpeggio
RE, S = arpeggio.RegExMatch, arpeggio.StrMatch                          # shortcut

show_dot=True

def parse_rule(txt, pattern=None):
    print(f'\nXXX >>{txt}<<')
    parser = ParserPython(rule, comment, debug=show_dot)
    tree = parser.parse(txt)
    assert tree.position_end == len(txt) , f"Not parsed whole input; Only: >>{txt[tree.position: tree.position_end]}<<; Not: >>{txt[tree.position_end:]}<<."

    print(f'\nTREE\n{tree.tree_str()}')

#    assert len(tree) == 3, "txt_term is an Ordered_Choice of always 3 Terminals"
#    assert isinstance(tree.txt, arpeggio.OrderedChoice) and tree.txt_name == "rule_term"


#    for e in tree: assert isinstance(e, arpeggio.Terminal)
#    if pattern:
#        for e,T in zip(tree,pattern):
#            if T is not None: assert isinstance(e.rule, T), f"{type(e.rule).__name__}  doesn't match {T.__name__}"

    return tree

def test_simple():	parse_rule(r"R <- A  B C ;")


