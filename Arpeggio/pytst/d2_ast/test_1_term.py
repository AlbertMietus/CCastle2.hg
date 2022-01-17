import pytest

import grammar
from castle import peg # has the AST classes

from . import parse

def assert_Term(term, term_type:type(peg.Terminal), value:str=None, err_message="Not correct value"):
    assert value is not None
    assert isinstance(term, peg.Terminal),	"It should be a term ..."
    assert isinstance(term, term_type),		f"... of the correct kind: {term_type} "
    assert term.value == value, err_message if err_message  else f"Note correct name, expected {name}"


def test_simple_str():
    txt="'a string'"
    ast = parse(txt, grammar.term)
    assert_Term(ast, peg.StrTerm, txt[1:-1], "It's correct value should be without quotes")


def test_simple_str_d3():
    txt='"""triple string"""'                                # A triple double quotes in Castle is also a simple string 
    ast = parse(txt, grammar.term)
    assert_Term(ast, peg.StrTerm, txt[3:-3], "It's correct value should be without quotes")


def test_regex_RE():
    txt='/a reg.ex/'
    ast = parse(txt, grammar.term)
    assert_Term(ast, peg.RegExpTerm, txt[1:-1], "It's correct value should be without slahes -- note: the regex itself is a string")


def regex_variants(txt, expect):
    ast = parse(txt, grammar.term)
    assert_Term(ast, peg.RegExpTerm, expect, 	"And the regex-pre/postfix should be removed from the value")


def test_regex_variants():
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


def test_term_as_expressions():                                         # A term is **ALSO an expressions
    txt="'a string'"
    ast = parse(txt, grammar.expressions)
    # result is same a above
    assert isinstance(ast, peg.Expression),	"A (str)term is also an Expression"
    assert len(ast.value) == 1,			"An expression with length==1"
    assert ast.value[0].value == txt[1:-1], 	"It's correct value should be without quotes"
