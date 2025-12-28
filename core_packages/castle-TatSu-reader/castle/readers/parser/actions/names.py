# (C) Albert Mietus, 2025. Part of Castle/CCastle project
import logging; logger = logging.getLogger(__name__)

from castle import aigr

class Names():
    def nameID(self, ast):
        return aigr.ID.Def(ast)
    def typeID(self, ast):
        return aigr.ID.Ref(name=ast, context='type')  # XXX HACK

