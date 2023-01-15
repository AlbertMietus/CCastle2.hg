# (C) Albert Mietus, 2022, 2023. Part of Castle/CCastle project

from typing import Generator

__all__ = ['CCompare']


def CCompare(ref_code: str, try_code: str, log=True, log_all=False) ->bool:
    """"Compare two piece of (simple) C-code and return whether they are similar.

        It ignores most whitespace, but not ATS-based. Make sure the ref in correctly formated!

        Note: this is down-ported as zip(... strict=True) is python-3.10
        """
    if log_all: log=True

    ref_tokens = text2tokens(ref_code)
    try_tokens = text2tokens(try_code)
    for a, b in zip(ref_tokens, try_tokens):
        if a != b:
            if log: print(f'{a}!={b}')
            return False
        if log_all: print(f'{a}')
    if len(list(ref_tokens)) == len(list(try_tokens)):
        return True
    #else
    if log: print("Not the same length")
    return False


def text2tokens(text: str) -> Generator[str, None, None]:
        for txt in text.split():
            for t in txt.split(';'):
                yield ';' if t=='' else t


