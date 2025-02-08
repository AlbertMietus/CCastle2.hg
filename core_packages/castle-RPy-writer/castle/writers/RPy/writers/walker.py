# (C) Albert Mietus, 2025. Part of Castle/CCastle project

import logging; logger = logging.getLogger(__name__)
import typing as PTH
# Python TypeHints

from castle import aigr
from castle.writers.RPy.aid import Block
from ..base.visitors import Visitor


class Walker(Visitor):
    _defaultType=tuple

    def visit__NameSpace(self, node) -> PTH.Optional[aigr.AIGR]:
        named_callables = node.find_byType(aigr.AIGR)
        logger.info(f"{node.name} has subnodes: {', '.join(f'{k}:<{type(v).__name__}>' for k,v in named_callables.items())}")
        return tuple(named_callables.values())

    # # Will inherit for visit_NamedSpace
    # def visit_ComponentImplementation(self, node) -> PTH.Optional[aigr.AIGR]:
    #    named_callables = node.find_byType(aigr.statements.callables._Named_callable)
    #    logger.info(f"{node.name} has subnodes: {', '.join(f'{k}:<{type(v).__name__}>' for k,v in named_callables.items())}")
    #    return tuple(named_callables.values())
