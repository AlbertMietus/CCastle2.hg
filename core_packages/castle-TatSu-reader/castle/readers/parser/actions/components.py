# (C) Albert Mietus, 2025. Part of Castle/CCastle project
import logging; logger = logging.getLogger(__name__)

from castle import aigr
from castle.aigr_extra.blend import mangle_event_handler

from ._debug import add_debug_logging

def portID_2_str(quid):
    """Given a qualID, remove 'self', and return as str"""
    if not isinstance(quid, (list, tuple)):
        logging.warning("Not a quilID (list of IDs): %s use as it (fingers crossed)", quid)
        return str(quid)
    #else
    short = quid[1:] if quid[0] == 'self' else quid
    return "_".join(str(n) for n in short)


@add_debug_logging
class Components():
    def implement_component(self, ast):
        parameters = () if ast.parameters is None else ast.parameters
        return aigr.ComponentImplementation(ast.name, parameters=parameters)
    def event_handler(self, ast):
        event, port, protocol = ast.event, ast.port, 'XXX_PROTO_VIA_PORT'

        assert False, "Need ComponentInterface to find proto via port"

        #return aigr.EventHandler(mangle_event_handler(str(protocol), str(event), portID_2_str(port)), ...)



