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

def verify_line_by_line(expect, got):
    WIDTH  = 90
    exp_lines, got_lines = expect.splitlines(), got.splitlines()
    LINES = max(len(exp_lines), len(got_lines))
    exp_lines += [''] * (LINES - len(exp_lines)); got_lines += [''] * (LINES - len(got_lines));

    side_by_side = "\n".join(f"{e:{WIDTH}} {'=' if e==g else '!'}{g}" for e,g in zip(exp_lines, got_lines))

    for e,g, no in zip(exp_lines, got_lines, range(999)):
        assert e == g, f"At least line {no} is wrong\n{"EXPECT":{WIDTH}} |GOT\n{side_by_side}"
    assert len(expect) == len(got), f"Length differs: expect: {len(expect)} != got:{len(got)}\n{side_by_side}"



