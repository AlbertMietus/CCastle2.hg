# (C) Albert Mietus, 2025. Part of Castle/CCastle project
import logging; logger = logging.getLogger(__name__)

from castle import aigr

from .support_functions import flat_tuple
from ._debug import add_debug_logging

@add_debug_logging
class Protocols():
    def event_definition(self, ast):
        return aigr.Event(ast.name, typedParameters=ast.parameters, return_type=ast.type)

    def event_protocol(self, ast):
        return aigr.EventProtocol(ast.name, events=ast.events) #XXX based_on, typedParameters
