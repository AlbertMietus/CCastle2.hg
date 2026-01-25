# (C) Albert Mietus, 2025,2026. Part of Castle/CCastle project
import logging; logger = logging.getLogger(__name__)

from castle import aigr

from .support_functions import *
from ._debug import add_debug_logging

@add_debug_logging
class Body():
    def body(self, ast):
        statements = [] if not isinstance(ast, list) else ast # Hack, for when there are no statements
        logging.info(f"BODY: {ast=}, {statements=}")
        return aigr.Body(statements=statements)
