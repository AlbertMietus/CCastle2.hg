1# (C) Albert Mietus, 2025. Part of Castle/CCastle project
import logging; logger = logging.getLogger(__name__)

from castle import aigr

from ._debug import add_debug_logging

@add_debug_logging
class Literals:
    def lit_string(self, ast):
        return aigr.fString(ast)
