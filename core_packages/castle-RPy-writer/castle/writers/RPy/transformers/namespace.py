# (C) Albert Mietus, 2025. Part of Castle/CCastle project

import typing as PTH                                                                                  # Python TypeHints
from types import ModuleType

from castle import aigr

#from ..writers.targets import RPy_unit
from ..writers import RPy_unit

EXTENTIONS=('.Moat', '.Castle')

OptStr = PTH.Optional[str]

def Source2RPy(src: aigr.Source_NS, filename:OptStr=None, ext:OptStr=None) -> RPy_unit:
    assert isinstance(src, aigr.Source_NS)
    if not filename:
        filename = src.source if src.source else str(src.name)

    target = RPy_unit(target_file=replace_extention(filename, ext),
                          name=filename,
                          outer_ns=src.outer_ns)
    for name,node in src._dict.items():
        target.register(node, asName=name)
    return target



def replace_extention(filename: str, new_ext=None) -> str:
    if not new_ext: new_ext = '.rpy'
    if new_ext[0] != '.': new_ext = '.'+ new_ext
    for ext in EXTENTIONS:
        if filename.endswith(ext):
            return filename[:-1*len(ext)] + new_ext
    return filename + new_ext
