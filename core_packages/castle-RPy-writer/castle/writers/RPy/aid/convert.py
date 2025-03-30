# (C) Albert Mietus, 2025. Part of Castle/CCastle project

import logging; logger = logging.getLogger(__name__)
import typing as PTH

__all__ = ['fstring_2_modulo']

START,END = '{','}'
TXT       = "STATE_TEXT"
VAL       = "STATE_VALUE"

def fString_2_modulo(s:str) -> PTH.Tuple[str, tuple]:
    state=TXT
    result, args = "", []
    for c in s:
        if state==TXT and c!=START:
            result+=c
        elif state==TXT and c==START:
            result+= "%s"
            state=VAL
            currentVal=""
        elif state==VAL and c!=END:
            currentVal+=c
        elif state==VAL and c==END:
            args.append(currentVal)
            state=TXT
    return result, tuple(args)
