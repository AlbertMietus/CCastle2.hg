# (C) Albert Mietus, 2025. Part of Castle/CCastle project

import logging; logger = logging.getLogger(__name__)
import typing as PTH                                                                                  # Python TypeHints

from castle import aigr
from .dispatch import MRO_Dispatch_Mixin


class Visitor(MRO_Dispatch_Mixin):
    _phases = _prefixes = ('visit', 'depart',)
    _defaultType=type(None)

    def _visitor(self, node, prefix='visit'):
        self.dispatch_check_prefix(prefix)

        method = self.dispatch_find_method_by_mro(node, prefix)
        if not method:
            empty = self._defaultType()
            logger.warning("No visitor for phase %s for node %s - returning empty (%s)", prefix, node, empty)
            return empty

        logger.debug("Going to call %s for %s in phase: %s", method,  node, prefix)
        return method(node)


    def visit(self, node: aigr.AIGR):
        return self._visitor(node, 'visit')

    def depart(self, node):
        return self._visitor(node, 'depart')

    def _default_visit(self, node: aigr.AIGR):
        logger.warning(f"Default visitor for {type(self).__name__} is called for {node} --in phase=visit) that is often a mistake")
        return self._defaultType() # type: ignore

    def _default_depart(self, node: aigr.AIGR):        # No depart visitor is fine.
        return None
        #return self._defaultType() # type: ignore
