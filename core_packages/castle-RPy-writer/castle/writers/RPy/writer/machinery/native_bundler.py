# (C) Albert Mietus, 2026. Part of Castle/CCastle project
import logging; logger = logging.getLogger(__name__)
import typing as PTH

from castle import aigr
from castle.aigr import types as CCTypes
from castle.writers.RPy.aid import TextBlock, Block

from . import Bundler, GeneratedCode, TypeTag
from ..portray import PortrayType

class NativeBundler(Bundler):
    """ (Desing) Notes (on :meth:`Bundler.box` & :meth:`Bundler.unbox`)

        The AIGR uses :class:`types._types` ("cc_type");  they are passed to box/unbox.
        As and example: `string`  (which is defined as ``CC_buildin('string')`

        The generated (PTy) code has coresponsing buildin types (see :mod:`castle.writers.RPy_buildin.buildin`).
        But also "wrappers";  subclasses of :class:`CC_B_Value`. The latter are used for (un)boxing.
        The combination of a wrapper and the argument,value (as text) is called a :class:`TypeTag` -basicly also text.

        The textual representation for those wrappers is defined in the :class:`Portray` class -- not in the Bundler"""

    def __init__(self):
        super().__init__()
        self.portray = PortrayType()

    def box(self, argument:GeneratedCode, cc_type:CCTypes._types) -> TypeTag:
        wrapper = self.portray.prefix(cc_type)
        return f"{wrapper}({argument})"

    def pack(self, arguments:PTH.Sequence[TypeTag], formal_parameters:aigr.OptionalTypedParameterList) -> TextBlock:
        pos = '[' + (", ".join(arg for arg in arguments)) + ']'
        named = "{}"                           #XXX ToDO: support for named arguments/parameters
        return f"{pos}, {named}"

    def unbox(self, parm:str, cc_type:CCTypes._types) -> GeneratedCode:
        val_type = self.portray.prefix(cc_type)
        return f"{val_type}.unbox({parm})"

    def unpack(self, formal_parameters:aigr.OptionalTypedParameterList):
        if formal_parameters is None: formal_parameters = () # always a sequence, for enumerate()
        ret_list = []
        for index, parm in enumerate(formal_parameters):
            ret_list.append((parm.name, f"pos[{index}]"))
        logger.debug("unpack --> %s -- %s", ret_list, formal_parameters)
        return ret_list



    def XXX_OLD_unpack(self, formal_parameters:aigr.OptionalTypedParameterList) -> Block:
        if formal_parameters is None: formal_parameters = () # always a sequence, for enumerate()
        txt = Block()
        for index, parm in enumerate(formal_parameters):
            val = self.unbox(f"{self.placeholder_for_positionals_}[{index}]", "XXXXX")
            txt += f"{parm.name} = {val}"
        return txt


