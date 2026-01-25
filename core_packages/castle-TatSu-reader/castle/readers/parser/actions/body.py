# (C) Albert Mietus, 2025,2026. Part of Castle/CCastle project
import logging; logger = logging.getLogger(__name__)

from castle import aigr

from ._debug import add_debug_logging

@add_debug_logging
class Body():
    def body(self, ast):
        statements = ast.statements if ast.statements else []
        logger.info(f"{ast=} ==> {statements=}")
        return aigr.Body(statements=statements)

