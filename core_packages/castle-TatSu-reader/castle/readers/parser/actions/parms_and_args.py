# (C) Albert Mietus, 2025. Part of Castle/CCastle project
import logging; logger = logging.getLogger(__name__)

from castle import aigr

from .support_functions import flat_tuple
from ._debug import add_debug_logging

@add_debug_logging
class ParmsArgs():
    def parameter(self, ast):
        return aigr.TypedParameter(name=ast.name, type=ast.type) #XXX type: str OR aigr.type.string?
    def parameterTuple(self, ast):
        "a parameterTuple is a **TUPLE** (not a list)"
        return flat_tuple(ast)
    def modifiers(self, ast):
        assert False, "modifiers -- like optional parameters-- are not yet supported in the AIGR"
