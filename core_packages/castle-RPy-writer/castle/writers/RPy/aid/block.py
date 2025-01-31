# (C) Albert Mietus, 2025. Part of Castle/CCastle project
# Base version with codeAI (chatGTP) -- needed work. Still needs more work. Bur for now ...

import logging; logger = logging.getLogger(__name__)
import typing as PTH

class Block:
    def __init__(self, text: PTH.Optional[str | PTH.Sequence[str] | 'Block']=None, indent: PTH.Optional[str]=None):
        self._txt: PTH.List[str | 'Block'] = []
        self.set_indent(indent)
        if text is not None:                                                              # ``if ""`` is False, None is needed
            self._addText(text, splitlines=True)

    def _addText(self, text: (str | PTH.Sequence[str] | 'Block'), splitlines: bool=False):
        lines:PTH.Sequence[str|'Block']
        if isinstance(text, str):
            if text == "" or splitlines==False:                                         # ``"".splitlines()`` gives empty list
                lines=[text]
            else: # Add every line, line by line
                lines=text.splitlines()
        elif isinstance(text, PTH.Sequence):
            lines = text
        elif isinstance(text, Block):
            lines = [text]
        else:
            assert False, f"Unknown type ({type(text)}) text: >>{text}<<"
        self._txt.extend(lines)
        return self
    def __iadd__(self, text):
        return self._addText(text, splitlines=False)

    def toStr(self, prefix="", end='\n'):
        return end.join(prefix+str(l) if isinstance(l, str) else l.toStr(prefix=prefix+self._indent, end=end) for l in self._txt)
    def __str__(self):
        return self.toStr()

    def set_indent(self, indent=None):
        """Set the prefix for the sub-blocks. Or None for the default)"""
        self._indent=str(indent) if indent is not None else ' '*4                                  #prefix when converting to str


