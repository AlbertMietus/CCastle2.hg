import pytest
import logging; logger = logging.getLogger(__name__)

from castle.readers.parser import grammar
from castle.ast import peg

from . import parse, assert_PEG

def test_simple_grammar():
    txt="""R1 <- A;
           R2 <- B;"""
    ast = parse(txt, grammar.peg_grammar, with_comments=False)
    assert_PEG(ast, no_of_rules=2)

def test_simple_grammar_with_no_comment():
    txt="""R1 <- A;
           R2 <- B;"""
    ast = parse(txt, grammar.peg_grammar, with_comments=False)
    assert_PEG(ast, no_of_rules=2)


def test_with_mid_comment():
    txt="""R1 <- A;
           // COMMENT
           R2 <- B;"""
    ast = parse(txt, grammar.peg_grammar, with_comments=True)
    assert_PEG(ast, no_of_rules=2)


def test_with_start_comment():
    txt="""// COMMENT
           R1 <- A;
           R2 <- B;"""
    ast = parse(txt, grammar.peg_grammar, with_comments=True)
    assert_PEG(ast, no_of_rules=2)

def test_grammar_with_mixed_rules():
    txt="""M1 <- A;
           M2 =  B;"""
    ast = parse(txt, grammar.peg_grammar)

    assert isinstance(ast, peg.Grammar)
    assert_PEG(ast, no_of_rules=1, no_of_settings=1)

def test_grammar_with_many_rules():
    txt="""R1 <- a;
           R2 <- bb;
           S1 =  1;
           R3 <- ccc;
           R4 <- dddd;
           S2 =  2;
           R5 <- eeeee;
           S3 =  3;"""
    ast = parse(txt, grammar.peg_grammar)

    assert isinstance(ast, peg.Grammar)
    assert_PEG(ast, no_of_rules=5, no_of_settings=3)
