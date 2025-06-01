# (C) Albert Mietus, 2025. Part of Castle/CCastle project

import logging; logger = logging.getLogger(__name__)
import typing as PTH                                                                                  # Python TypeHints

from castle import aigr
#from castle.writers.RPy.aid import Block


class Machinery:
    _register, _default_hint = {}, None # placeholders

    @classmethod
    def register(cls, *hints, default: bool = False):
        """Decorator to register subclasses of Machinery with multiple names."""
        def decorator(subclass):
            for hint in hints:
                cls._register[hint] = subclass
            if default:
                if cls._default_hint:
                    logger.warning("Set another default Machinery; was %s, becomes %s", cls._default_hint, hints[0])
                cls._default_hint = hints[0]
            return subclass
        return decorator

    def __new__(cls, hint:str="", **kwargs):
        _hint = hint if hint not in ["", None] else cls._default_hint
        try:
            m = cls._register[_hint]
        except KeyError as e:
            logger.warning("No Machinery for %s; trying default: %s -- Available: %s", hint, cls._default_hint, cls._register)
            m = cls._register[cls._default_hint]
        assert m, "No Machinery, not even a default"
        logger.debug("Machinery %s selected", m)
        return super().__new__(m, **kwargs)


class _M_DirectCall(Machinery): # Abstract
    pass

@Machinery.register('DirectCall.tuple', "tuple")
class  M_DC_tuple(_M_DirectCall):
    pass

@Machinery.register('DirectCall.list', "list")
class  M_DC_list(_M_DirectCall):
    pass

class _M_DC_dict(_M_DirectCall): #Abstract
    pass

@Machinery.register('DirectCall.dict.flat', "flat.dict", "flat_dict", "flat-dict")
class M_DC_flat_dict(_M_DC_dict):
  pass

@Machinery.register('DirectCall.dict.chained', "chained.dict", "chained_dict", "chained-dict", default=True)
class M_DC_chained_dict(_M_DC_dict):
    pass
