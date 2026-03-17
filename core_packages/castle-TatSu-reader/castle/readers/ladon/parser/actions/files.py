# (C) Albert Mietus, 2026. Part of Castle/CCastle project
import logging; logger = logging.getLogger(__name__)

from ...aigr import FileNS, ScaffolderFileNS
from ._debug import add_debug_logging

@add_debug_logging
class Files():
    def castle_file(self, ast) ->FileNS:

        if isinstance(ast, (tuple, list)):
            return self._old(ast)
        #else
        assert False, "new 'dict-style' ast is XXX ToDo"

    def _old(self, seq):
        logging.warning("Uning 'old-sequence' ast in files")
        source = FileNS()
        wrapped = ScaffolderFileNS(source)

        for e in seq:
            if isinstance(e, dict) and 'docstring' in e:
                logger.warning("Can't handle docstring YET ignore for now) %s", e.docstring)
            elif isinstance(e, (tuple, list)):
                for ee in e:
                    wrapped.register(ee)
            else:
                wrapped.register(ee)
        return source


