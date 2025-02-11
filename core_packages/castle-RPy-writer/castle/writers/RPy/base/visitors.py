# (C) Albert Mietus, 2025. Part of Castle/CCastle project

import logging; logger = logging.getLogger(__name__)

from castle import aigr

class Visitor():
    _phases = ('visit', 'depart',)
    _defaultType=type(None)

    def _visitor(self, node, prefix='visit'):
        if not prefix in self._phases:
            logger.warning("not a known phase: %s -- continuing with fingers crossed", prefix)

        method = self._find_method_by_mro(node, prefix)
        if not method:
            method = self._find_default_method(node, prefix)
        if not method:
            empty = self._defaultType()
            logger.warning("No visitor for phase %s for node %s - returning empty (%s)", prefix, node, empty)
            return empty

        logger.debug("Going to call %s for %s in phase: %s", method,  node, prefix)
        return method(node)

    def _find_method_by_mro(self, node, prefix):
        supers = type(node).mro()
        for cls in supers:
            method = self._find_method_for_cls(prefix, cls)
            if method:
                return method
        return None

    def _find_method_for_cls(self, prefix, cls):
        cls_name = cls.__qualname__
        method_name = f'{prefix}_{cls_name}'
        method = getattr(self, method_name, None)
        return method # or None

    def _find_default_method(self, node, prefix):
        method_name = f'_default_{prefix}'
        method = getattr(self, method_name, None)
        return method # or None

    def visit(self, node: aigr.AIGR):
        return self._visitor(node, 'visit')

    def depart(self, node):
        return self._visitor(node, 'depart')

    def _default_visit(self, node: aigr.AIGR):
        logger.warning(f"Default visitor for {type(self).__name__} is called for {node} --in phase=visit) that is often a mistake")
        return self._defaultType() # type: ignore

    def _default_depart(self, node: aigr.AIGR):
        # No depart visitor is fine.
        return self._defaultType() # type: ignore 

