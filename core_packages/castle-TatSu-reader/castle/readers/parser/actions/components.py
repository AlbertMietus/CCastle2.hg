# (C) Albert Mietus, 2025. Part of Castle/CCastle project
import logging; logger = logging.getLogger(__name__)

from castle import aigr

class Components():
    def implement_component(self, ast):
        parameters = () if ast.parameters is None else ast.parameters
        retval= aigr.ComponentImplementation(ast.name, parameters=parameters)
        logger.debug(f"implement_component: {ast=} ==> {retval}")
        return retval


