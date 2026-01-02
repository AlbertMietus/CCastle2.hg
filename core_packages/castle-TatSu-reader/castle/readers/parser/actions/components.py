# (C) Albert Mietus, 2025. Part of Castle/CCastle project
import logging; logger = logging.getLogger(__name__)

from castle import aigr
from ._debug import add_debug_logging

@add_debug_logging
class Components():
    def implement_component(self, ast):
        parameters = () if ast.parameters is None else ast.parameters
        return aigr.ComponentImplementation(ast.name, parameters=parameters)


