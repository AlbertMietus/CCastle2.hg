# (C) Albert Mietus, 2025. Part of Castle/CCastle project
import logging; logger = logging.getLogger(__name__)

from castle import aigr

from .support_functions import *
from ._debug import add_debug_logging

@add_debug_logging
class ParmsArgs():
    #parms
    def typedParameterTuple(self, ast):
        "a parameterTuple is a **TUPLE** (not a list)"
        return flat_tuple(ast)
    def typedParameter(self, ast):
        return aigr.TypedParameter(name=ast.name, type=ast.type) #XXX type: str OR aigr.type.string?
    #parms
    def argumentTuple(self, ast):
        "an argumentTuple is a **LIST**"
        return flat_list(ast)
    def argument(self, ast):
        return aigr.Argument(name=ast.name, value=ast.value)
    def literal_ID(self, ast):
        return aigr.Constant(value=ast)





    # --ToDo
    def modifiers(self, ast):
        assert False, "modifiers -- like optional parameters-- are not yet supported in the AIGR"

