# (C) Albert Mietus, 2025. Part of Castle/CCastle project
import logging; logger = logging.getLogger(__name__)

from castle import aigr

class Names():
    def nameID(self, ast):
        retval=aigr.ID.Def(ast)
        logger.debug(f"nameID: {ast=} ==> {retval=}")
        return retval
    def typeID(self, ast):
        return aigr.ID.Ref(name=ast, context='type')             # XXX HACK
    def auto_self(self, ast):
        retval = aigr.ID.Ref(name=ast, context='self')           # XXX HACK
        logger.debug(f"auto_self: {ast=} ==> {retval=}")
        return retval
    def qualID(self, ast):
        retval = [sub for item in ast for sub in (item if isinstance(item, (list, tuple)) else [item])]
        logger.debug(f"qualID: {ast=} ==> {retval=}")
        return retval
