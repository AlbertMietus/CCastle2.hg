# (C) Albert Mietus, 2022, 2023. Part of Castle/CCastle project

from typing import Generator

__all__ = ['CCompare']


def CCompare(ref_code: str, try_code: str, log=True, log_all=False) ->bool:
    """"Compare two piece of (simple) C-code and return whether they are similar.

        It ignores most whitespace, but not ATS-based. Make sure the ref in correctly formated!

        Note: this is down-ported as zip(... strict=True) is python-3.10
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
        if log: print("Not the same length")
        return False


def text2tokens(text: str) -> Generator[str, None, None]:
        for txt in text.split():
            for t in txt.split(';'):
                yield ';' if t=='' else t


