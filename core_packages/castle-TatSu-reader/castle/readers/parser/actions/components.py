# (C) Albert Mietus, 2025. Part of Castle/CCastle project
import logging; logger = logging.getLogger(__name__)

from castle import aigr
from castle.aigr_extra.blend import mangle_event_handler

from ._debug import add_debug_logging
from .support_functions import flat_list

@add_debug_logging
class Components():
    def component_definition(self, ast):
        if ast.parameters:
            assert False, "ComponentInterface does not yett support parameters: {ast.parameters}"
        ports = ast.ports if ast.ports else []
        return aigr.ComponentInterface(ast.name, based_on=ast.base, ports=ports)

    def implement_component(self, ast):
        parameters = () if ast.parameters is None else ast.parameters
        handlers   = [] if ast.handlers is None else ast.handlers
        return aigr.ComponentImplementation(ast.name, parameters=parameters, handlers=handlers,) #XXX

    def port_line(self, ast):
        return aigr.Port(ast.name, direction=ast.direction, type=ast.type)

    def port_direction(self, ast):
        try:
            dir = aigr.PortDirection[str.capitalize(ast.direction)]
        except KeyError as e:
            logger.error("Unknown port_direction: %s, will use 'PortDirection.Unknown' -- error: %s", ast.direction, e)
            dir = aigr.PortDirection.Unknown
        return dir

    def event_handler(self, ast):     #---- TODO: event-handler via port + protocol
        if len(ast.event)==2:
            protocol, event = ast.event[0], ast.event[1]
        elif len(ast.event)==1:
            assert False, "Need ComponentInterface to find proto via port"
            protocol, event = 'XXX_PROTO_VIA_PORT', ast.event[0]
        else:
            assert False, "event-qualID of more as 2 parst not yet supported: {ast.event}"
        port = ast.port
        return aigr.EventHandler(mangle_event_handler(protocol=protocol, event=event, port=port), # mangle now handle QualID/ID/str
                                 protocol=protocol, event=event, port=port,
                                 # outer_ns= self.current_ns,
                                 body=ast.body)

    def body(self, ast):
        statements = ast.statements if ast.statements else []
        logger.info(f"{ast=} ==> {statements=}")
        return aigr.Body(statements=statements)



