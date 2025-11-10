# (C) Albert Mietus, 2025. Part of Castle/CCastle project

import logging; logger = logging.getLogger(__name__)

import typing as PTH                                                                                  # Python TypeHints
from abc import ABC, abstractmethod

from castle.writers.RPy.aid import Block


class Machinery(ABC):
    _register      : dict    = {}
    _default_hint  : PTH.Any = None

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


    @abstractmethod
    def render_EventDispatchTable(self, renderer, node) ->  Block: pass

    @abstractmethod
    def render_EventOverPort(self, renderer, node) ->  Block:
        assert False

    @abstractmethod
    def render_EventToSub(self, renderer, node) ->  Block:
        assert False
