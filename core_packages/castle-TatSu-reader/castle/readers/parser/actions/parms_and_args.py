# (C) Albert Mietus, 2025. Part of Castle/CCastle project
import logging; logger = logging.getLogger(__name__)

from castle import aigr

class ParmsArgs():
    def parameter(self, ast):
        return aigr.TypedParameter(name=ast.name, type=ast.type) #XXX type: str OR aigr.type.string?
    def parameterTuple(self, ast):
        "a parameterTuple is a **TUPLE** (not a list)"
        logger.info(f"parameterTuple: {ast=}")
        return tuple(ast)

    def modifiers(self, ast):
        assert False, "modifiers -- like optional parameters-- are not yet supported in the AIGR"
