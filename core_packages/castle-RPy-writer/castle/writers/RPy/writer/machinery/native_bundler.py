# (C) Albert Mietus, 2026. Part of Castle/CCastle project
import logging; logger = logging.getLogger(__name__)
import typing as PTH

from castle import aigr
from castle.aigr import types as CCTypes
from castle.writers.RPy.aid import TextBlock, Block

from . import Bundler, GeneratedCode, TypeTag
from ..portray import PortrayType


class NativeBundler(Bundler):
    placeholder_for_positionals_ = 'pos'
    placeholder_for_named_       = 'named'

    def __init__(self):
        super().__init__()
        self.portray = PortrayType()

    def box(self, argument:GeneratedCode, cc_type:CCTypes._types) -> TypeTag:
        cast= self.portray.prefix(cc_type)
        return f"{cast}({argument})"

    def pack(self, arguments:PTH.Sequence[TypeTag], formal_parameters:aigr.OptionalTypedParameterList) -> TextBlock:
        pos = '[' + (", ".join(arg for arg in arguments)) + ']'
        named = "{}"                           #XXX ToDO: support for named arguments/parameters
        return f"{pos}, {named}"

    def unbox(self, parm:str) -> GeneratedCode:
        return f"{parm}.value"

    def unpack(self, formal_parameters:aigr.OptionalTypedParameterList) -> Block:
        if formal_parameters is None: formal_parameters = () # always a sequence, for enumerate()
        txt = Block()
        for index, parm in enumerate(formal_parameters):
            val = self.unbox(f"{self.placeholder_for_positionals_}[{index}]")
            txt += f"{parm.name} = {val}"
        return txt


