# (C) Albert Mietus, 2025. Part of Castle/CCastle project

import pytest
from castle.writers.RPy.aid import Block

@pytest.fixture
def txt():
    return "A B C\nKLM\n"

@pytest.fixture
def block(txt):
    return Block(txt)

@pytest.fixture
def indented_txt():
    return "InDeNtEd"

@pytest.fixture
def indented_block(indented_txt):
    return Block(indented_txt)

def print_block(b): # For debugging
    print(f"\n=====[str(b), b._txt]=====\n{str(b)}\n{b._txt}\n==========\n")


def test_1_2line(txt, block):
    assert str(block) == txt

def test_1_3ways_of_aLine(txt):
    txt = txt.splitlines()[0]
    b1, b2, b3 = Block(txt), Block([txt]), Block((txt,))
    assert str(b1) == str(b2)
    assert str(b1) == str(b3)

def test_2a_simpleAdd(txt):
    lines = txt.splitlines()
    b=Block(lines[0])
    b+=lines[1]
    assert str(b) == txt

def verify_BlockOf4(b, txt):
    result=str(b)
    assert len(result.splitlines()) == 4, f"Adding 2 lines to a block ({b._txt})of 2 lines should give 4 lines"
    assert result == txt*2

def test_2a_extendTxt_results_in_moreLines(block,txt):
    for l in txt.splitlines():
        block += l
    verify_BlockOf4(block,txt)

def test_2_extendBlock_results_in_moreLines(block,txt):
    block += Block(txt)
    verify_BlockOf4(block,txt)

def test_3a_indent_default_4space(block, indented_txt, indented_block):
    block.sub(indented_block)
    assert (' '*4 + indented_txt) in str(block)

def test_3b_indent_late(block, indented_txt, indented_block):
    block.sub(indented_block)
    block.set_indent('\t')
    assert ' x'*4 + indented_txt not in str(block)
    assert '\t' + indented_txt  in str(block)

def test_3b_indent_block(block):
    sub_block = Block("subBlock")
    block.sub(sub_block)
    block +="not indented"
    sub_block += "above last line"

    block.set_indent('MARK_')
    txt = str(block)
    assert "MARK_above" in txt, "This line in the sub_block should be indented"
    assert (
        ("MARK_not indented" not in txt) and   # check on no prefix, before the text
        ("not indented" in txt)                # check the test is there
        ),  "'not indented' shouldn't be indented (with MARK_)"

def test_buggy_notEmptyLines_areFine():
    b = Block()
    b += "line 1"
    b += "line 2"
    b += "line 3"
    lines=str(b).splitlines()
    assert len(lines) == 3, f"Not correct number of lines: >>{lines}<<"

def test_buggy_EmptyLines_areFineTo():
    """This used to go wring in all codeAI generated code ... (My version works:-)"""
    b = Block()
    b += "line 1"
    b += "" #empty line 2
    b += "line 3"
    lines=str(b).splitlines()
    assert len(lines) == 3, f"Not correct number of lines: >>{lines}<<"

def test_subsubsub():
    b1=Block('X', indent='_1_')
    b2=Block('X', indent='_2_');
    b3=Block('X', indent='_3_');
    b4=Block('X', indent='_4_')
    b1.sub(b2); b2.sub(b3); b3.sub(b4)
    txt=str(b1)
    assert '_1__2__3_' in txt, "Each sub-block should be indented by concatenated prefixes of outer-blocks"

def test_subBlock_returnsSelf():
    top = Block('top')
    b = top.sub(Block('sub'))
    assert b is top
