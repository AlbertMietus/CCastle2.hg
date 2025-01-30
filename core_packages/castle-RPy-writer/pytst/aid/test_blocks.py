# (C) Albert Mietus, 2025. Part of Castle/CCastle project

import pytest
from castle.writers.RPy.aid import Block

@pytest.fixture
def txt():
    return "A B C\nKLM"

@pytest.fixture
def block(txt):
    return Block(txt)


def test_1_2line(txt, block):
    assert str(block) == txt

def test_1_3ways_of_aLine(txt):
    txt = txt.splitlines()[0]
    b1, b2, b3 = Block(txt), Block([txt]), Block((txt,))
    assert str(b1) == str(b2)
    assert str(b1) == str(b3)

def test_2_simpleAdd(txt):
    lines = txt.splitlines()
    b=Block(lines[0])
    b+=lines[1]
    assert str(b) == txt

def test_3a_indent_default_4space(block):
    indented = "InDeNtEd"
    block += Block.INDENT
    block += indented
    assert (' '*4 + indented) in str(block)

def test_3b_indent_late(block):
    indented = "InDeNtEd"
    block += Block.INDENT
    block += indented
    block.set_indent('\t')
    assert ' '*4 + indented not in str(block)
    assert '\t' + indented  in str(block)

def test_3b_indent_block(block):
    sub_block = Block("subBlock")
    block += block.INDENT
    block += sub_block
    block += Block.DEDENT
    block +="not indented"
    sub_block += "above last line"

    txt = str(block)
    assert " above" in txt, "This line in the sub_block should be indented"
    assert ("not indented" in txt) and (" not indented" not in txt), "There should be a space before the 'not indented'"

def test_4_blockblock(txt, block):
    b = Block(block)
    assert str(b) == txt

def test_buggy_notEmptyLines_areFine():
    b = Block()
    b += "line 1"
    b += "line 2" 
    b += "line 3"
    lines=str(b).splitlines()
    assert len(lines) == 3, f"Not correct number of lines: >>{lines}<<"

def test_buggy_anEmptyLines_isMissing():
    b = Block()
    b += "line 1"
    b += "" #empty line 2
    b += "line 3"

    lines=str(b).splitlines()
    assert len(lines) == 3, f"Not correct number of lines: >>{lines}<<"

