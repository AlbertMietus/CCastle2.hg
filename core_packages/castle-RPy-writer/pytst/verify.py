# (C) Albert Mietus, 2025. Part of Castle/CCastle project

import logging; logger = logging.getLogger(__name__)
#import pytest


def verify_line(expect, got, line=None):
    logger.debug("verify_line\n\texpect:\t%s\ngot\t>>%s<<\n\tline=%s", expect, got, line)
    if expect == got:
        return
    try:
        txt = (got.splitlines()[line]) if line else got
    except IndexError:
        assert False, f"line={line} does not exist in got:>>{got}<< -- Expected: {expect}"
    assert expect in txt, imprint((expect,'EXPECT'),(txt, 'Txt'),(got, 'Got'))


def print_out(txt,label='print'):
    print(imprint((txt, label)))
    pass

def imprint(*parts):
    return "\n".join(f"\n=====[{label}:{len(txt)}/{len(txt.splitlines())}]=====\n{txt}\n=====[end]=====" for txt, label in parts)

def verify_line_by_line(expect, result):
    expect_lines, result_lines = expect.splitlines(), result.splitlines()
    logger.info("expect\n%s", expect)
    logger.info("result\n%s", result)
    for e,g, no in zip(expect_lines, result_lines, range(999)):
        NL,context="\n\t",3
        assert e == g, f'''Line: {no+1} not as expected :: >>{e}<< != <<{g}>>
expect:\t>{e}<
result:\t<{g}>
After_E\n {NL.join(expect_lines[no+1:][:context])}
After_G\n {NL.join(result_lines[no+1:][:context])}
Before\n{NL.join(result_lines[:no][-context:])}'''
    assert len(expect) == len(result), f"Not the same number of lines: expect: {len(expect)}, result: {len(result)}"



