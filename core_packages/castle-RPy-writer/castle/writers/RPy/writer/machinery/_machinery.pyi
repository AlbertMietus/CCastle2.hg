# (C) Albert Mietus, 2026. CodeAI=GH.Claude.Opus-4.8
#
# Type stub for ``castle.writers.RPy.writer.machinery._machinery``.

import typing as PTH
from abc import abstractmethod
from castle.writers.RPy.aid import Block
from ._bundler import Bundler

class Machinery:
    """Abstract strategy base that renders inter-component event plumbing.

    ``Machinery`` is the pluggable "backend" inside the :class:`Renderer`.
    It answers the question *"how do I emit the dispatch-table / event
    plumbing?"* independently of the rest of the renderer.

    Selecting a concrete backend
    ----------------------------
    ``Machinery.__new__`` acts as a factory: it consults an internal registry
    to find the concrete subclass matching *hint* (or the default), constructs
    that subclass, and returns it.  You never instantiate a concrete subclass
    directly.

    ::

        m = Machinery()                    # uses the registered default
        m = Machinery("chained-dict")      # selects M_DC_chained_dict explicitly

    Registering a new backend
    -------------------------
    Decorate a :class:`Machinery` subclass with ``@Machinery.register``:

    ::

        @Machinery.register("my-backend", default=True)
        class MyMachinery(Machinery):
            def render_EventDispatchTable(self, renderer, node): ...
            def render_EventOverPort(self, renderer, node): ...
            def render_EventToSub(self, renderer, node): ...

    Registered hints (built-in)
    ---------------------------
    * ``"chained-dict"`` / ``"chained_dict"`` / ``"DirectCall.dict.chained"``
      -> :class:`M_DC_chained_dict` (**default**)
    * ``"flat-dict"`` / ``"flat_dict"`` / ``"DirectCall.dict.flat"``
      -> :class:`M_DC_flat_dict`
    * ``"tuple"`` / ``"DirectCall.tuple"``  -> :class:`M_DC_tuple`
    * ``"list"``                            -> :class:`M_DC_list`
    """

    _register: PTH.ClassVar[dict[str, type]]
    """Class-level registry: hint string -> concrete Machinery subclass."""
    _default_hint: PTH.ClassVar[PTH.Any]
    """Hint string of the default backend (set via ``@Machinery.register(..., default=True)``)."""

    arg_bundler: Bundler
    """The argument-bundler strategy (always a :class:`NativeBundler` for now)."""

    def __new__(cls, hint: str = ..., **kwargs: PTH.Any) -> "Machinery": ...

    def __init__(self, **kwargs: PTH.Any) -> None: ...

    @classmethod
    def register(
        cls,
        *hints: str,
        default: bool = ...,
    ) -> PTH.Callable[[type], type]:
        """Class decorator to register a :class:`Machinery` subclass.

        Parameters
        ----------
        *hints:
            One or more string keys under which the subclass is registered.
        default:
            When ``True`` this subclass becomes the fallback when no hint
            matches.  Only one default is allowed; setting a second one logs
            a warning.
        """
        ...

    @abstractmethod
    def render_EventDispatchTable(self, renderer: PTH.Any, node: PTH.Any) -> Block:
        """Emit the RPy code for one event-dispatch table.

        Parameters
        ----------
        renderer:
            The active :class:`Renderer` instance (for name rendering via
            ``renderer.portray``).
        node:
            An :class:`EventDispatchTable_Scaffolder` instance.
        """
        ...

    @abstractmethod
    def render_EventOverPort(self, renderer: PTH.Any, node: PTH.Any) -> Block:
        """Emit the RPy code for an event-over-port send (WIP in some backends)."""
        ...

    @abstractmethod
    def render_EventToSub(self, renderer: PTH.Any, node: PTH.Any) -> Block:
        """Emit the RPy code for an event-to-sub-component send (WIP)."""
        ...
