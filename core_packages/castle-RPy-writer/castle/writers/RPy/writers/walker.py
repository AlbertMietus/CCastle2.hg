# (C) Albert Mietus, 2025. Part of Castle/CCastle project

import logging; logger = logging.getLogger(__name__)
import typing as PTH                                                  # Python TypeHints

from castle import aigr
from castle.writers.RPy.aid import Block
from ..base.visitors import Visitor

from castle.aigr_extra.scaffolding import ScaffolderBody, ScaffolderNameSpace

class Walker(Visitor):
    _defaultType=tuple

    """Walk over aigr._<type>, or it corresponding Scaffolding instance.

    note: data-fields of `node` --even when (already) "scaffolded"--are directly accessible!"""

    def visit__NameSpace(self, node) -> PTH.Sequence[aigr.AIGR]:
        """General walker for all Nodes that have a NS (See aigr._NameSpace) - walk over that NS"""
        if isinstance(node, aigr.AIGR):
                node = ScaffolderNameSpace(node)
        named_callables = node.find_byType(aigr.AIGR)
        logger.debug("%s (%s) has sub-nodes: %s", node.name, type(node).__name__, ', '.join(f'{k}:<{type(v).__name__}>' for k,v in named_callables.items()))
        return tuple(named_callables.values())

    def visit__Named_callable(self, node) -> PTH.Sequence[aigr.AIGR]: # Method, EventHandler, ...
        # `node` as callable, has a body (field) -- no need for scaffolding. Even when it already is, .body is readable
        body = node.body
        logger.debug("%s (%s) has %s body", node.name, type(node).__name__, "no" if body is None else "a")
        return tuple((body,))

    def visit_ComponentImplementation(self, node) -> PTH.Sequence[aigr.AIGR]:
        """Walk over the NS, and over the handlers"""
        ns_tuple = self.visit__NameSpace(node)
        handlers_tuple = tuple(node.handlers)
        all = ns_tuple + handlers_tuple
        logger.debug("Component %s has %s named-subnodes, & %s handlers: %s ",
                         node.name, len(ns_tuple), len(handlers_tuple), ', '.join(f'{e}:<{type(e).__name__}>' for e in all))
        return all


    def visit_Body(self, node) -> PTH.Sequence[aigr.AIGR]:
        statements = node.statements #List of nodes
        logger.debug("Body of <%s> has len=%s statements --  %s",  type(node).__name__, len(statements), statements)
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
