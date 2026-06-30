# (C) Albert Mietus, 2026. CodeAI=GH.Claude.Opus-4.8
#
# Type stub for ``castle.writers.RPy.writer.portray``.

import typing as PTH
from castle import aigr
from castle.monorail.base.visitors import Visitor

class Portray:
    """Naming sub-visitor: converts AIGR names to their RPy spellings.

    ``Portray`` is one of the four helpers owned by :class:`Renderer`.  It
    answers the question *"how is this AIGR name spelled in the generated
    Python?"*.  It is a plain class (not a ``Visitor``) because name
    translation is pure string logic -- no MRO dispatch needed.

    Every generated symbol has a well-defined prefix that encodes its role:

    =================== =============================================
    Prefix              Role
    =================== =============================================
    ``CC_<Name>``       Generated component *class* (Python class)
    ``cc_C_<Name>``     Component-class *element* (CC_B_ComponentClass)
    ``cc_CI_<Name>``    Component-interface element
    ``cc_S_<Comp>_<P>`` Event dispatch-table for port *P* on *Comp*
    ``CC_P_<Pr>_<Ev>``  Event trigger key in a dispatch table
    ``cc_P_<Name>``     Protocol element
    =================== =============================================

    Usage
    -----
    ::

        from castle.writers.RPy.writer.portray import Portray

        p = Portray(renderer)
        p.CC_cls_prefix("Counter")      # -> 'CC_Counter'
        p.cc_CI_elm_prefix("Counter")   # -> 'cc_CI_Counter'
        p.cc_S_dispatchTable("Counter", "clk")  # -> 'cc_S_Counter_clk'
    """

    def __init__(self, renderer: PTH.Any) -> None: ...

    # --- Built-in class name helpers ---

    def BuildInComponent(self) -> str:
        """Return the import path for the base component class: ``'buildin.CC_B_Component'``."""
        ...

    def BuildInProtocol(self) -> str:
        """Return the import path for the base protocol class: ``'buildin.CC_B_Protocol'``."""
        ...

    def BuildInComponentInterface(self) -> str:
        """Return the import path for the component-interface class: ``'buildin.CC_B_ComponentInterface'``."""
        ...

    # --- Prefixing helpers ---

    def CC_cls_prefix(self, name: str) -> str:
        """Return the generated Python class name: ``CC_<Name>``."""
        ...

    def cc_C_elm_prefix(self, name: str) -> str:
        """Return the component-class element name: ``cc_C_<Name>``."""
        ...

    def cc_CI_elm_prefix(self, name: str) -> str:
        """Return the component-interface element name: ``cc_CI_<Name>``."""
        ...

    def cc_S_dispatchTable(self, comp: str, port: str) -> str:
        """Return the dispatch-table variable name: ``cc_S_<Comp>_<Port>``."""
        ...

    def CC_P_eventTrigger(self, protocol: str, event: str) -> str:
        """Return the event-trigger key: ``CC_P_<Protocol>_<Event>``."""
        ...

    def callDef_name(self, name: str) -> str:
        """Return the generated method/function name (no prefix added)."""
        ...

    def CC_ProtocolName_prefix(self, name: str) -> str:
        """Return the protocol element name: ``cc_P_<Name>``."""
        ...

    def prefix(self, prefix: str, name: str) -> str:
        """Apply *prefix* to the last segment of a dotted *name*.

        Preserves any leading namespace (e.g. ``ns.CC_Foo`` from
        ``prefix("CC_", "ns.Foo")``).
        """
        ...

    def default_component(self) -> str:
        """Return the default component base: ``'base.cc_CI_Component'``."""
        ...

    # --- AIGR-node -> string helpers ---

    def Port2Protocol(self, port: aigr.Port) -> str:
        """Return the RPy name for *port*'s protocol.

        Only ``Protocol``-typed ports are currently supported; others raise
        ``NotImplementedError``.
        """
        ...

    def PortDirection(self, port: aigr.Port) -> str:
        """Return the RPy expression for *port*'s direction constant.

        Result looks like ``'buildin.CC_PortDirection.In'``.
        """
        ...


class PortrayType(Visitor):
    """Type-dispatching helper that maps a Castle AIGR type to its ``CC_B_*`` class name.

    Uses the ``'prefix'`` phase (``_prefixes = ('prefix',)``) to dispatch
    ``prefix_<ClassName>`` methods.  The default handler reads
    ``CC_type.represents`` and prepends ``'CC_B_'``.

    Usage
    -----
    ::

        pt = PortrayType()
        pt.prefix(aigr.types.int)               # -> 'CC_B_int'
        pt.prefix(a_component_implementation)   # -> 'CC_B_Component'
    """

    _prefixes: PTH.ClassVar[tuple[str, ...]]
    _CC_buildinType_prefix: PTH.ClassVar[str]

    def prefix(self, CC_type: PTH.Any) -> str:
        """Dispatch to ``prefix_<ClassName>`` for *CC_type*, or use the default."""
        ...

    def _default_prefix(self, CC_type: PTH.Any) -> str:
        """Default: return ``'CC_B_' + CC_type.represents``."""
        ...

    def prefix_ComponentImplementation(self, CC_type: PTH.Any) -> str:
        """Special case: ``ComponentImplementation`` maps to ``'CC_B_Component'``."""
        ...
