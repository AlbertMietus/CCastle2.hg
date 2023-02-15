# (C) Albert Mietus, 2022, 2023. Part of Castle/CCastle project

import logging; logger = logging.getLogger(__name__)

from typing import Generator
from collections.abc import Callable

__all__ = ['CCompare', 'verify_indents']


def CCompare(ref_code: str, try_code: str, log=True, log_all=False) ->bool:
    """"Compare two piece of (simple) C-code and return whether they are similar.

        It ignores most whitespace, but not ATS-based. Make sure the ref in correctly formated!

        It will return a boolean to notice it "comparability". It will not assert.
        So, it is typically called as ``assert CCompare(...)```
        """
    if log_all: log=True

    try:
        for a, b in zip(text2tokens(ref_code), text2tokens(try_code),  strict=True):
            if a != b:
                if log: print(f'{a}!={b}')
                return False
            if log_all: print(f'{a}')
        return True
    except ValueError: # The zip-input do not have the same length ==> Not equal
        if log:
            print("Not the same length")
            print("**** ref_code:: ****\n" + ref_code +"\n********************\n")
            print("**** try_code:: ****\n" + try_code +"\n********************\n")
        return False


def text2tokens(text: str) -> Generator[str, None, None]:
        for txt in text.split():
            for t in txt.split(';'):
                yield ';' if t=='' else t


def verify_indents(ref: str, renderer: Callable[..., str]) -> None:
    """verify the indents of a render_XXX() method of CC_XXX class are correct.

       It will call the renderer, with a "stange" indent and compare that with the ref_text -- that is properly indented with ONE space as `indent`
       It does so line by line.

       When it correct, it returns (noting). Else it will ASSERT
       """
    try_indent="_-|"
    out = renderer(indent=try_indent, prepend="")
    logger.info("% results in::\n%s", renderer.__name__,  out)

    for ref_line,out_line in zip(ref.splitlines(), out.splitlines()):
        ref_indents = len(ref_line)-len(ref_line.lstrip(' '))
        logger.debug("ref_line: %s", ref_line); logger.debug("out_line: %s", out_line)

        assert out_line[:len(try_indent)*ref_indents] == try_indent*ref_indents
        if ref_indents >0:
            without_pref = out_line[len(try_indent*ref_indents):]
            assert without_pref[0:len(try_indent)] != try_indent

