# (C) Albert Mietus, 2025.
# May become Part of Castle/CCastle project

import logging; logger = logging.getLogger(__name__)
import typing as PTH                                                                                  # Python TypeHints

from castle import aigr

def walkKids(n: aigr.AIGR, recursive=False):
    for k in n._kids:
        m = getattr(n, k)
        logger.debug(f"yieldKid: {k}: {m}")
        yield m
        if recursive:
            walkKids(m, recursive)

def walkNS(ns: aigr.NamedSpace,recursive=False):
    for k,v in ns._dict.items():
        logger.debug(f"yieldName: {k} ({type(v)})")
        yield(v)
        if recursive:
            walkNS(v, recursive)


