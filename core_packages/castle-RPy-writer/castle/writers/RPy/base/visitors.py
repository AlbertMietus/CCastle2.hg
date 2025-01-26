# (C) Albert Mietus, 2025. Part of Castle/CCastle project

import logging; logger = logging.getLogger(__name__)

from castle import aigr

class Visitor():
    _phases = ('visit', 'depart',)

    def _vistor(self, node, prefix='visit') -> str:
        if not prefix in self._phases:
            logger.warning("not a known phase: %s -- continuing with fingers crossed", prefix)
        cls_name = type(node).__qualname__
        method_name = f'{prefix}_{cls_name}'
        method = getattr(self, method_name, None)

        if not method: # Try default method
            method_name = f'_default_{prefix}'
            method = getattr(self, method_name, None)
            if not method:
                logger.warning("No vistor for phase %s for node %s - return empty string", prefix, node)
                return ""

        logger.debug("Going to call '%s' (%s) for %s in phase: %s", method, method_name, node, prefix)
        return method(node)

    def visit(self, node: aigr.AIGR) -> str:
        return self._vistor(node, 'visit')

    def depart(self, node):
        return self._vistor(node, 'depart')

    def _default_visit(self, node: aigr.AIGR) ->str:
        logger.warning(f"The default (phase=visit) visitor is called for {node} -- often that is a mistake")
        return "#XXX"

    def _default_depart(self, node: aigr.AIGR) ->str:
        # No depart visitor is fine.
        return ""

