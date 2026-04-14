# (C) Albert Mietus, 2026. Part of Castle/CCastle project
import logging; logger = logging.getLogger(__name__)
import typing as PTH

from castle import aigr
from castle.aigr import types as CCTypes
from castle.writers.RPy.aid import TextBlock

from . import Bundler, GeneratedCode, TypeTag
from ..portray import PortrayType


class NativeBundler(Bundler):

    def __init__(self):
        super().__init__()
        self.portray = PortrayType()

    def box(self, argument:GeneratedCode, cc_type:CCTypes._types) -> TypeTag:
        cast= self.portray.prefix(cc_type)
        return f"{cast}({argument})"

    def pack(self, arguments:PTH.Sequence[TypeTag], formal_parameters:aigr.OptionalTypedParameterList) -> TextBlock:
        assert False

    def unpack(self, parameters:GeneratedCode, formal_parameters:aigr.OptionalTypedParameterList) -> TextBlock:
        assert False

    def unbox(self, parm:str) -> GeneratedCode:
        return f"{parm}.value"


    def OLD_XXXX_pack(self, arguments:aigr.ArgumentList, formal_parameters:aigr.OptionalTypedParameterList) -> TextBlock: #XXX

        pos_parts = []
        for arg, param in zip(arguments, (p for p in (formal_parameters or ()))):
            value_txt = arg.value.value if isinstance(arg.value, aigr.fString) else repr(arg.value) ### TODO: use vistor
            wrapper   = f'CC_B_{param.type.represents}'   #XXX ToDo Move CC_B prefix to portray
            pos_parts.append(f'{wrapper}("{value_txt}")')
        return f'[{", ".join(pos_parts)}], {{}}'
