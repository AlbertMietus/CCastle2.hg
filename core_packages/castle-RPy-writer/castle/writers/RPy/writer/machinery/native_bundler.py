# (C) Albert Mietus, 2026. Part of Castle/CCastle project
from __future__ import annotations # ignore `CC_B_Value` annotation durung runtime

import logging; logger = logging.getLogger(__name__)
import typing as PTH

from castle import aigr
from castle.aigr import types as CCTypes
from castle.writers.RPy.aid import TextBlock, Block

from . import Bundler, GeneratedCode, TypeTag, CC_B_Value

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

    # XXX Move to portray?
    def _name_of_positionals(self):  return 'pos'
    def _name_of_named(self):        return 'named'

    def box(self, argument:GeneratedCode, cc_type:CCTypes._types) -> TypeTag[CC_B_Value]:
        wrapper = self.portray.prefix(cc_type)                                  ### ToDo/Q: is `prefix` the best name?
        return f"{wrapper}({argument})"

    def pack(self, arguments:PTH.Sequence[TypeTag[CC_B_Value]], formal_parameters:aigr.OptionalTypedParameterList) -> TextBlock:
        pos = '[' + (", ".join(arg for arg in arguments)) + ']'
        named = "{}"                           #XXX ToDO: support for named arguments/parameters
        return f"{pos}, {named}"

    def unbox(self, parm:str, cc_type:CCTypes._types) -> GeneratedCode:
        logger.info("unbox: parm=%s, cc_type=%s", parm, cc_type)   #XXX info/debug
        val_type = self.portray.prefix(cc_type)
        return f"{val_type}.unbox({parm})"

    def unpack(self, formal_parameters:aigr.OptionalTypedParameterList) -> list[tuple[aigr.ID, TypeTag[ParameterListElement]]]:
        if formal_parameters is None: formal_parameters = () # always a sequence, for enumerate()

        logger.warning("No support positionals yet")   #XXX
        pos = self._name_of_positionals()
        ret_list = [(parm.name, f"{pos}[{index}]") for index, parm in enumerate(formal_parameters)]

        logger.info("unpack --> %s -- %s", ret_list, formal_parameters)   #XXX info/debug

        return ret_list                                                   #type: ignore

    def unpack_unbox(self, formal_parameters:aigr.OptionalTypedParameterList) ->list[tuple[aigr.ID, GeneratedCode]]:
        if formal_parameters is None: formal_parameters = () # always a sequence, for enumerate()
        unpacked : list[tuple[aigr.ID, TypeTag[ParameterListElement]]]
        unpacked = self.unpack(formal_parameters)
        ret_list = []
        for inx, unp in enumerate(unpacked):
            name, boxed_value  = unp[0], unp[1]
            unboxed_value = self.unbox(boxed_value, formal_parameters[inx].type)
            ret_list.append((name, unboxed_value))
        return ret_list


class ParameterListElement: "Dummy class, only for TypeTag -- Is't code like 'name[anInt]'"




