# (C) Albert Mietus, 2025. Part of Castle/CCastle project

import logging; logger = logging.getLogger(__name__)

import typing as PTH                                                                                  # Python TypeHints
from abc import ABC, abstractmethod

from castle.writers.RPy.aid import Block
from ._bundler import Bundler

class Machinery(ABC):
    """The ``Machinery`` deals with the technicalities how events and other data is send over a connection.

       This ABC defines the interface, and can instantiate a concrete Machinery. This is done by passing a "hint"
       to :class:`Machinery`().

       A concrete Machinery can register itself with the `@Machinery.register` decorator -- this is "pluggable".
       As a machinery can have sub-variants, they typically have multiple name/hint -- long hierarchical ones and short, practical ones

       Some concrete (built-in) Machineries with the hint
       --------------------------------------------------

       - :class:`M_DC_chained_dict` | ``chained-dict`` | ``chained_dict`` 		| ``DirectCall.dict.chained`` | (default)
       - :class:`M_DC_flat_dict`    | ``flat-dict``    | ``flat_dict``    		| ``DirectCall.dict.flat``	  |
       - :class:`M_DC_tuple`        | ``tuple``        | ``DirectCall.tuple`` 	|
       - :class:`M_DC_list`			| ``list``         |

       .. note:: Typically, the Machinery is only called from :class:`Renderer` class, inside a writer."""

    _register     : PTH.ClassVar[dict[str, type]]  ={} # hint:str -> concrete Machinery subclass
    _default_hint : PTH.ClassVar[str]=""               # default machinery


    @classmethod
    def register(cls, *hints: str, default: bool = False):
        """Decorator to register sub classes of Machinery with multiple names."""
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
            logger.warning("No Machinery for %s; trying default: %s -- Available: %s --%s", hint, cls._default_hint, cls._register, e)
            m = cls._register[cls._default_hint]
        assert m, "No Machinery, not even a default"
        logger.debug("Machinery %s selected", m)
        return super().__new__(m, **kwargs)


    def __init__(self, **kwargs):
         self.arg_bundler = Bundler()    # pyright: ignore[reportAbstractUsage]  # Now: always: `NativeBundler'
         logger.debug("arg_bundler=%s", self.arg_bundler)

    @abstractmethod
    def render_EventDispatchTable(self, renderer, node) ->  Block:
        """Generate the code for a event dispatch table"""

    @abstractmethod
    def render_EventOverPort(self, renderer, node) ->  Block:
        """Generate the code for an event-over-port send"""

    @abstractmethod
    def render_EventToSub(self, renderer, node) ->  Block:
        """Generate the code for sending an event a sub-component"""

# LocalWords:  pluggable Renderer Machineries
