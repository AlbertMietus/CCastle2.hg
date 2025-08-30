# (C) Albert Mietus, 2025. Part of Castle/CCastle project

import logging; logger = logging.getLogger(__name__)
import typing as PTH                                                                                  # Python TypeHints

class MRO_Dispatch_Mixin():
    _prefixes: tuple[str, ...] = () # Set this in the class -- f.e. to `('visit', 'depart',)` . It will be checked and logged. It will not fail

    def dispatch_check_prefix(self, prefix):
        known = prefix in self._prefixes
        if not known:
            logger.warning("not a known prefix: %s -- continuing with fingers crossed --- %s", prefix, self._prefixes)
        return known

    def dispatch_find_method_by_mro(self, node, prefix) -> PTH.Optional[PTH.Callable]:
        method = self._find_prefix_method_by_mro(node, prefix)
        if not method:
            method = self._find_default_method(node, prefix)
        if not method:
            logger.warning("No method found (not even a default) for prefix=%s for node=%s", prefix, node)

        return method # Can be Nome

    def _find_prefix_method_by_mro(self, node, prefix) -> PTH.Optional[PTH.Callable]:
        supers = type(node).mro()
        for cls in supers:
            method = self._find_method_for_cls(cls, prefix)
            if method:
                return method
        return None

    def _find_method_for_cls(self, cls, prefix)  -> PTH.Optional[PTH.Callable]:
        cls_name = cls.__qualname__
        method_name = f'{prefix}_{cls_name}'
        method = getattr(self, method_name, None)
        return method # or None

    def _find_default_method(self, node, prefix)  -> PTH.Optional[PTH.Callable]:
        method_name = f'_default_{prefix}'
        method = getattr(self, method_name, None)
        return method # or None
