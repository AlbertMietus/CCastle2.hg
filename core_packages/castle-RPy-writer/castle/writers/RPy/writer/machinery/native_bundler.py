# (C) Albert Mietus, 2026. Part of Castle/CCastle project
import logging; logger = logging.getLogger(__name__)
import typing as PTH

from castle import aigr
from castle.writers.RPy.aid import TextBlock

from . import Bundler, ArgumentList, Signature

class NativeBundler(Bundler):

    def pack(self, arguments:ArgumentList, signature:Signature) -> TextBlock:
        if not arguments:
            return '[], {}'
        pos_parts = []
        for arg, param in zip(arguments, (p for p in (signature or ()))):
            value_txt = arg.value.value if isinstance(arg.value, aigr.fString) else repr(arg.value)
            wrapper   = f'CC_B_{param.type.represents}'
            pos_parts.append(f'{wrapper}("{value_txt}")')
        return f'[{", ".join(pos_parts)}], {{}}'

    def unpack(self, signature:Signature) -> TextBlock:
        return ""
