# (C) Albert Mietus, 2025. Part of Castle/CCastle project

import logging; logger = logging.getLogger(__name__)
import typing as PTH                                                                                  # Python TypeHints

from .dispatch import MRO_Dispatch_Mixin


# The type of `node` is typically aigr.AIGR -- but we can't use that as monorail should not depend on aigr
class Visitor(MRO_Dispatch_Mixin):
    _prefixes = ('visit', 'depart',)
    _defaultType = lambda self: None  # Override this in subclasses if needed

    def _visitor(self, node, dispatch_on=None, prefix='visit'):
        """Call a a visitor, that depend on dispatch (or node).

           First, a method-name searched based on (the type of) `dispatch_on` and `prefix`
           Roughly that is ``$prefix_$cls_name(dispatch_on)``  -- See MRO_Dispatch_Mixin for details
           For $cls_name() the full MRO is examined

           Then, that method is called, passing `node`, in the used subclass

           .. node::

              * When `dispatch_on`, node will be used  -- this is default
              * It is possible to dispatch on/for another class, with `dispatch_on`.
                That instance is otherwise not used"""

        if dispatch_on is None:
                dispatch_on = node

        self.dispatch_check_prefix(prefix) # log for unknown prefixes
        method = self.dispatch_find_method_by_mro(dispatch_on, prefix)
        if not method:
            empty = self._defaultType()
            logger.warning("No dispatch found for dispatch_on=%s (prefix=%s), returning empty (%s) -- node=%s",
                               dispatch_on, prefix, empty, node)
            return empty
        logger.debug("Going to call %s for %s in phase: %s", method,  node, prefix)
        return method(node)

    def visit(self, node, dispatch_on=None):
        return self._visitor(node, dispatch_on, 'visit')

    def depart(self, node, dispatch_on=None):
        return self._visitor(node, dispatch_on, 'depart')

    def _default_visit(self, node):
        logger.warning(f"Default visitor for {type(self).__name__} is called for {node} --in phase=visit) that is often a mistake")
        return self._defaultType() # type: ignore

    def _default_depart(self, node):        # No depart visitor is fine.
        return None
