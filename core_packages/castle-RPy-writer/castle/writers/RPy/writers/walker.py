# (C) Albert Mietus, 2025. Part of Castle/CCastle project

import logging; logger = logging.getLogger(__name__)
import typing as PTH                                                  # Python TypeHints

from castle import aigr
from castle.writers.RPy.aid import Block
from ..base.visitors import Visitor

from castle.aigr_extra.scaffolding import ScaffolderBody

class Walker(Visitor):
    _defaultType=tuple

    def visit__NameSpace(self, node) -> PTH.Sequence[aigr.AIGR]:
        """Many general nodes have a namespace, like ComponentImplementation; they use this walker as default"""
        named_callables = node.find_byType(aigr.AIGR)
        logger.debug("%s (%s) has subnodes: %s", node.name, type(node).__name__, ', '.join(f'{k}:<{type(v).__name__}>' for k,v in named_callables.items()))
        return tuple(named_callables.values())

    def visit__Named_callable(self, node) -> PTH.Sequence[aigr.AIGR]: # Method, EventHandler, ...
        body = ScaffolderBody(node.body) #single node # GAM XXX ScaffolderBody or Body
        logger.debug("%s (%s) has %s body", node.name, type(node).__name__, "no" if body is None else "a")
        return tuple(body,)

    def visit_Body(self, node) -> PTH.Sequence[aigr.AIGR]:
        statements = node.statements #List of nodes
        logger.debug("%s (%s) has len=%s statements --  %s", node.name, type(node).__name__, len(statements), statements)
        return tuple(statements)

    def visit_VoidCall(self, node) -> PTH.Sequence[aigr.AIGR]:
        call = node.call #single node
        logger.debug("visit_VoidCall: %s in %s",  call, node)
        return tuple((call,))

    def visit_Call(self, node) -> PTH.Sequence[aigr.AIGR]:
        callable = node.callable #single node
        logger.debug("visit_Call: %s in %s",  callable, node)
        return tuple((callable,))

    def visit_fString(self, node) -> PTH.Sequence[aigr.AIGR]:
        return ()
