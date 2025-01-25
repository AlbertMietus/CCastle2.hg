# (C) Albert Mietus, 2025. Part of Castle/CCastle project

import logging; logger = logging.getLogger(__name__)

from castle import aigr

class Visitor():
    def visit(self, node):
        cls_name = type(node).__qualname__
        visit_name = f'visit_{cls_name}'
        visitor = getattr(self, visit_name, self._default_vistor)
        logger.debug("Going to use '%s' (%s) for %s", visitor, visit_name, node)
        return visitor(node)

    def _default_vistor(self, node: aigr.AIGR) ->str:
        logger.warning(f'The default visitor is called for {node} -- often that is a mistake')
        return ""

