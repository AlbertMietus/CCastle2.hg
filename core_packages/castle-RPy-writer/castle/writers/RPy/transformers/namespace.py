# (C) Albert Mietus, 2025. Part of Castle/CCastle project

import typing as PTH                                                                                  # Python TypeHints
from types import ModuleType

from castle import aigr
from castle.aigr_extra.scaffolding import ScaffolderNameSpace

from ..aigr.units import RPy_unit

EXTENTIONS=('.Moat', '.Castle')
RPY_EXT= 'py' # No need to use .rpy and rename later ...

OptStr = PTH.Optional[str]

def Source2RPy(src :aigr.Source_NS, filename :OptStr=None, ext :OptStr=None) -> RPy_unit:
    assert isinstance(src, aigr.Source_NS)
    if not filename:
        filename = str(src.source if src.source else src.name)

    target = RPy_unit(target_file=_replace_extention(filename, ext),
                          name=filename,
                          outer_ns=src.outer_ns)
    _copy_sourceNS_to_Unit(src, target)

    return target



def _replace_extention(filename: str, new_ext=None) -> str:
    new_ext = new_ext if new_ext  else RPY_EXT
    new_ext = new_ext if new_ext[0] == '.' else '.'+ new_ext

    for ext in EXTENTIONS:
        if filename.endswith(ext):
            return filename[:-1*len(ext)] + new_ext
    return filename + new_ext

def _copy_sourceNS_to_Unit(src:aigr.Source_NS, target:RPy_unit) ->None:
    wrapped  = ScaffolderNameSpace(target)
    for name, node in src._ns.items():
        wrapped.register(node, asName=name)
