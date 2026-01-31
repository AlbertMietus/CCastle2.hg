# (C) Albert Mietus, 2026. Part of Castle/CCastle project
import logging; logger = logging.getLogger(__name__)

from castle import aigr

from ._debug import add_debug_logging

@add_debug_logging
class Files():
    def castle_file(self, ast) ->aigr.Source_NS:
        l=[]
        for e in ast:
            if isinstance(e, dict):
                if 'docstring' in e:
                    logger.warning:("Can't handle docstring YET ignore for now) %s", e.docstring)
            elif isinstance(e, (tuple, list)):
                l.extend(e)
            else:
                l.append(e)
        return l

