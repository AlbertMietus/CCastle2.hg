# (C) Albert Mietus, 2025. Part of Castle/CCastle project

import logging; logger = logging.getLogger(__name__)

from castle.monorail.base.visitors import Visitor
from castle import aigr

class IDRef(Visitor):
    """An ID with an aigr.Ref() as should be rendered depending on the AIGR it reffers.
       IDRef is an auxility class of Renderer, for those case.

       It main entry-point is ``portray()`` which returns (a typical short) string."""

    _defaultType=str                      #used in Visitor, to return a default value of the right type

    def __init__(self, renderer):
        self._renderer = renderer

    def portray(self, node: aigr.ID) ->str: # MAYBE: add 'hint', then also in Visitor
        return self.visit(node)

    def _default_visit(self, node:aigr.ID): # XXX TMP
        raise NotImplementedError("No IDRef::visit_%s, Can't portray: %s", type(node).__name__, node )

    def visit_ID(self, node):
        """This node (an ID) refers anotherID: easy - render it"""
        return self._renderer.visit(node.context.reference)

        
