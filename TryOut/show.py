# (C) Albert Mietus, 2025.
# May become Part of Castle/CCastle project

import logging; logger = logging.getLogger(__name__)
import typing as PTH                                                                                  # Python TypeHints

from castle import aigr

def Try_printNameType(n: aigr.NamedNode):
    try:
        print(n.name,'\t', type(n))
    except:
        pass


def showNS(ns: aigr.NamedSpace):
    Try_printNameType(ns)
    try:
        for k,v in ns._ns.items():
            print('\t',k, '\t', type(v))
    except AttributeError:
        pass
