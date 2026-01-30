# (C) Albert Mietus, 2025. Part of Castle/CCastle project
import logging; logger = logging.getLogger(__name__)

from castle import aigr

from .support_functions import flat_list
from ._debug import add_debug_logging

@add_debug_logging
class Names():
    def nameID(self, ast):
        return aigr.ID.Def(ast)
    def nameRef(self, ast):
        return aigr.ID.Ref(ast, context=None)
    def typeID(self, ast):
        return aigr.ID.Ref(name=ast, context='type')             # XXX HACK
    def auto_self(self, ast):
        return aigr.ID.Ref(name=ast, context='self')           # XXX HACK
    def qualRef(self, ast):
        return flat_list(ast)
