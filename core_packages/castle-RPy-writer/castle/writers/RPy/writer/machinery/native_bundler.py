# (C) Albert Mietus, 2026. Part of Castle/CCastle project
import logging; logger = logging.getLogger(__name__)
import typing as PTH

from castle import aigr
from castle.writers.RPy.aid import TextBlock

from . import Bundler



class NativeBundler(Bundler):

    def pack(self, arguments:aigr.ArgumentList, formal_parameters:aigr.OptionalTypedParameterList) -> TextBlock:
        logging.warning("TODO: move the 2 (hardcoded and non-vistor) lines out")

        pos_parts = []
        for arg, param in zip(arguments, (p for p in (formal_parameters or ()))):
            value_txt = arg.value.value if isinstance(arg.value, aigr.fString) else repr(arg.value) ### TODO: use vistor
            wrapper   = f'CC_B_{param.type.represents}'   #XXX ToDo Move CC_B prefix to portray
            pos_parts.append(f'{wrapper}("{value_txt}")')
        return f'[{", ".join(pos_parts)}], {{}}'

    def unpack(self, formal_parameters:aigr.OptionalTypedParameterList) -> TextBlock:
        return ""
