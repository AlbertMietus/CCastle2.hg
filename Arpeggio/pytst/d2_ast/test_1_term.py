import pytest

import grammar

import sys; sys.path.append("./../AST/") ; sys.path.append("./../../AST/")
from castle import peg # has the AST clases

from . import parse

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

@pytest.mark.skip(reason="single_expr has no visitor -- as that is now in expressions")
def test_term_as_single_expr():                                         # A term is **ALSO** a single_expr
    txt="'a string'"
    ast = parse(txt, grammar.single_expr)
    assert isinstance(ast, peg.Expression),	"A (str)term is also an Expression"
    assert len(ast.value) == 1,			"An expression with length==1"
    assert ast.value[0].value == txt[1:-1], 	"It's correct value should be without quotes"


def test_term_as_expressions():                                         # A term is **ALSO an expressions
    txt="'a string'"
    ast = parse(txt, grammar.expressions)
    # result is same a above
    assert isinstance(ast, peg.Expression),	"A (str)term is also an Expression"
    assert len(ast.value) == 1,			"An expression with length==1"
    assert ast.value[0].value == txt[1:-1], 	"It's correct value should be without quotes"


