# (C) Albert Mietus, 2025,2026. Part of Castle/CCastle project
import logging; logger = logging.getLogger(__name__)

from castle import aigr

from .support_functions import *
from ._debug import add_debug_logging

@add_debug_logging
class Body():
    def body(self, ast):
        statements = [] if not isinstance(ast, list) else ast # Hack, for when there are no statements
        return aigr.Body(statements=statements)
    def stat_voidcall(self, ast):
        name = ast.longname[0] if len(ast.longname) == 1 else ast.longname
        args = ast.args if ast.args is not None else []
        callable = aigr.Call(callable=name, arguments=args)
        return aigr.VoidCall(callable)
