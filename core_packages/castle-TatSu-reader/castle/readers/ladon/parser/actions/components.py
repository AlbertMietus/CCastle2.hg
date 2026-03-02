# (C) Albert Mietus, 2025,2026. Part of Castle/CCastle project
import logging; logger = logging.getLogger(__name__)

from castle import aigr
from castle.aigr_extra.blend import mangle_event_handler
from castle.aigr_extra import scaffolding

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
        parameters =  () if ast.parameters  is None else ast.parameters
        handlers   =  [] if ast.handlers    is None else ast.handlers

        logging.warning("XXX `%s.docstring` isn't supported yet --  %s", ast.name, ast.docstring)
        logging.warning("XXX `%s.interface` has to be added (later?)", ast.name)

        comp = aigr.ComponentImplementation(ast.name, parameters=parameters, handlers=handlers,) # XXXX
        wrapped = scaffolding.ScaffolderComponentImplementation(comp)
        self._implement_component_addLocals(wrapped, ast)
        wrapped.auto_register()
        return comp

    def _implement_component_addLocals(self, wrapped_comp, ast):
        local_names = []
        if ast.local_functions:
            local_names.extend(ast.local_functions)
        if ast.members:         # XXX members: ToDo
            local_names.extend(ast.members)
        for l_name in local_names:
            logger.info(f"addLocals: register:: {l_name=}) -- {wrapped_comp=}")
            wrapped_comp.register(l_name)



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
            assert False, "event-qualRef of more as 2 parst not yet supported: {ast.event}"
        port = ast.port
        return aigr.EventHandler(mangle_event_handler(protocol=protocol, event=event, port=port), # mangle now handled QualID/ID/str
                                 returns=ast.returns, # XXX convert to type?
                                 protocol=protocol, event=event, port=port,
                                 # outer_ns= self.current_ns,
                                 body=ast.body)


    def method(self, ast):
        return aigr.Method(ast.name,
                           returns=ast.returns, # XXX convert to type?
                           parameters=() if ast.parameters is None else ast.parameters,
                           body=ast.body,
                           )
