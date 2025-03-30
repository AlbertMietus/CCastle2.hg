# (C) Albert Mietus, 2025. Part of Castle/CCastle project

import logging; logger = logging.getLogger(__name__)
import typing as PTH

class Block:
    def __init__(self, text: PTH.Optional[str | PTH.Sequence[str] | 'Block']=None, indent: PTH.Optional[str]=None):
        self._txt: PTH.List[str | 'Block'] = []
        self.set_indent(indent)
        if text is not None:                                                              # ``if ""`` is False, None is needed
            self._addText(text, splitlines=True)
        logger.debug("Block is made: >>%s<<", repr(str(self)))

    def _addText(self, text: (None| str | PTH.Sequence[str] | 'Block'), splitlines: bool=False):
        lines:PTH.Sequence[str|'Block']
        if text is None:
            return self
        if isinstance(text, str):
            if text == "" or splitlines==False:                                         # ``"".splitlines()`` gives empty list
                lines=[text]
            else: # Add every line, line by line
                lines=text.splitlines()
        elif isinstance(text, PTH.Sequence):
            lines = text
        elif isinstance(text, Block): # extend semantics
            lines = text._txt
        else:
            assert False, f"Unknown type ({type(text)}) text: >>{text}<< self: {str(self)}"
        self._txt.extend(lines)
        logger.debug("_addText (%s) results in: >>%s<<", repr(text), repr(str(self)))
        return self

    def __iadd__(self, text): # 'extend semantics'
        return self._addText(text, splitlines=False)

    def sub(self, block:PTH.Optional['Block']): #append semantics
        if block:
            self._txt.append(block)
        logger.debug(".sub(<<%s>>) results in: >>%s<<", repr(str(block)), repr(str(self)))
        return self

    def toStr(self, prefix="", end='\n'):
        return end.join(prefix+str(l) if isinstance(l, str) else l.toStr(prefix=prefix+self._indent, end=end) for l in self._txt)+'\n'
    def __str__(self):
        return self.toStr()

    def set_indent(self, indent=None):
        """Set the prefix for the sub-blocks. Or None for the default)"""
        self._indent=str(indent) if indent is not None else ' '*4                                  #prefix when converting to str


