import pytest

import grammar
import visitor
import arpeggio

import sys; sys.path.append("./../AST/") ; sys.path.append("./../../AST/")
from castle import peg # has the AST clases


def parse(txt, rule):
    parser = arpeggio.ParserPython(rule)
    pt = parser.parse(txt)
    assert pt.position_end == len(txt), "Did not parse all input"       # JTBS
    ast = arpeggio.visit_parse_tree(pt, visitor.PegVisitor())
    assert ast.position == 0 and ast.position_end == len(txt), "Also the AST should include all input"
    return ast

def test_simple_str():
    txt="'a string'"
    ast = parse(txt, grammar.term)
    assert isinstance(ast, peg.Terminal),	"It should be a term ..."
    assert isinstance(ast, peg.StrTerm), 	"... and a str"
    assert ast.value == "a string", 		"It's correct value should be without quotes"

def test_simple_str_d3():
    txt='"""triple string"""'                                # A triple double quotes in Castle is also a simple string 
    ast = parse(txt, grammar.term)
    assert isinstance(ast, peg.Terminal),	"It should be a term ..."
    assert isinstance(ast, peg.StrTerm), 	"... and a str"
    assert ast.value == "triple string", 	"It's correct value should be without quotes"

def test_regex_RE():
    txt='/a reg.ex/'
    ast = parse(txt, grammar.term)
    assert isinstance(ast, peg.Terminal),	"It should be a term ..."
    assert isinstance(ast, peg.RegExpTerm), 	"... and a RegExp"
    assert ast.value == 'a reg.ex', 		"It's correct value should be without slahes -- note: the regex itself is a string"

def regex_variants(txt, expect):
    ast = parse(txt, grammar.term)
    assert isinstance(ast, peg.Terminal),	"It should be a term ..."
    assert isinstance(ast, peg.RegExpTerm), 	"... and a RegExp"
    assert ast.value == expect, 		"And the regex-pre/postfix should be removed from the value"

def testregex_variants():
    regex_variants(txt:="""/a reg.ex/""", expect=txt[1:-1])                 # Same a test_regex_RE
    regex_variants(txt:="""/re_slash/""", expect=txt[1:-1])

    regex_variants(txt:="""R're__Rstr_s1'""", expect=txt[2:-1])
    regex_variants(txt:="""r're__rstr_s1'""", expect=txt[2:-1])
    regex_variants(txt:='''R"re__Rstr_d1"''', expect=txt[2:-1])
    regex_variants(txt:='''r"re__rstr_d1"''', expect=txt[2:-1])

    regex_variants(txt:="""R'''re__Rstr_s3'''""", expect=txt[4:-3])
    regex_variants(txt:="""r'''re__rstr_s3'''""", expect=txt[4:-3])
    regex_variants(txt:='''R"""re__Rstr_d3"""''', expect=txt[4:-3])
    regex_variants(txt:='''r"""re__rstr_d3"""''', expect=txt[4:-3])


