.. (C) Albert Mietus, 2026. CodeAI=GH.Claude.Opus-4.8

castle-RPy-writer
=================

The **RPy writer** is the Castle compiler back-end that walks an AIGR tree and
renders it as runnable Python (RPython-compatible) source code.  It sits at the
top of the CCastle dependency hierarchy, building on ``castle-aigr`` for the
data model and ``castle-monorail`` for the visitor machinery.  A single call to
:meth:`Renderer.render` turns a parsed Castle program into a ``.py`` file ready
for CPython or the RPython/PyPy2 toolchain.

.. contents:: On this page
   :local:
   :depth: 1

At a glance
-----------

==========================  ====================================================
Package                     ``castle-RPy-writer`` (version 0.0.1)
Depends on                  ``castle-aigr``, ``castle-monorail``
Import roots                ``castle.writers.RPy``, ``castle.writers.RPy_buildin``
Main entry point            :class:`Renderer` (``castle.writers.RPy.writer``)
Key classes                 :class:`Renderer`, :class:`Walker`, :class:`Portray`,
                            :class:`IDRef`, :class:`Machinery`
Transformer                 :func:`Source2RPy` (``castle.writers.RPy.transformers``)
Unit scaffolder             :class:`ScaffolderUnit` (``castle.writers.RPy.aigr.units``)
Translators                 :class:`Evaluate`, :class:`Compile`, :class:`Execute`
Built-in runtime            ``castle.writers.RPy_buildin``
==========================  ====================================================

The most common workflow::

    from castle.writers.RPy.transformers import Source2RPy
    from castle.writers.RPy.aigr.units import ScaffolderUnit

    unit = Source2RPy(source_ns)          # AIGR Source_NS -> RPy_unit
    ScaffolderUnit(unit).write_out(inDir="build/")   # render + save

----

``Renderer`` -- the main entry point
-------------------------------------

*Module:* ``castle.writers.RPy.writer`` (re-exports ``castle.writers.RPy.writer.renderer``)
(`renderer.py
<../../../core_packages/castle-RPy-writer/castle/writers/RPy/writer/renderer.py>`_ /
`renderer.pyi
<../../../core_packages/castle-RPy-writer/castle/writers/RPy/writer/renderer.pyi>`_)

``Renderer`` is the orchestrator: it owns four single-purpose helper objects
and dispatches rendering to them via the ``monorail`` visitor mechanism.  Every
``visit_<ClassName>`` method handles one AIGR node type.

How to use it
~~~~~~~~~~~~~

#. Build an AIGR tree (e.g. via the TatSu reader or programmatically).
#. Optionally wrap the ``Source_NS`` with :func:`Source2RPy` to get an
   ``RPy_unit`` (the node type the renderer understands as a *file*).
#. Call ``Renderer().render(unit)`` to get the Python source as a string.
#. Or use :class:`ScaffolderUnit` to render and write directly to disk.

All four helpers -- ``walker``, ``machinery``, ``portray``, ``idref`` -- have
sensible defaults so ``Renderer()`` with no arguments is the common case.
Inject custom instances to override specific behaviour (e.g. in tests).

.. code-block:: python

    from castle.writers.RPy.writer.renderer import Renderer
    from castle.writers.RPy.transformers import Source2RPy

    # Option 1: render to a string
    unit = Source2RPy(source_ns, filename="output.py")
    code = Renderer().render(unit)
    print(code)

    # Option 2: render + write to disk via ScaffolderUnit
    from castle.writers.RPy.aigr.units import ScaffolderUnit
    ScaffolderUnit(unit).write_out(inDir="build/")

    # Option 3: inject a custom Machinery backend
    from castle.writers.RPy.writer.machinery import Machinery
    renderer = Renderer(machinery=Machinery("flat-dict"))
    code = renderer.render(unit)

Public signatures
~~~~~~~~~~~~~~~~~~

.. code-block:: python

    class Renderer(Visitor):
        walker:    Walker     # default: Walker()
        machinery: Machinery  # default: Machinery()  -> M_DC_chained_dict
        portray:   Portray    # default: Portray(self)
        idref:     IDRef      # default: IDRef(self)

        def __init__(self, walker=None, machinery=None,
                     portray=None, idref=None, **kw) -> None: ...
        def render(self, node: aigr.AIGR) -> str: ...          # THE main entry
        def render_subNodes(self, node) -> Block | None: ...   # descend helpers

        # visit_* handlers (one per AIGR node type; returning TextBlock):
        def visit_RPy_unit(self, node) -> TextBlock: ...
        def visit_ComponentInterface(self, node) -> TextBlock: ...
        def visit_ComponentImplementation(self, node) -> TextBlock: ...
        def depart_ComponentImplementation(self, node) -> TextBlock: ...
        def visit_EventProtocol(self, node) -> TextBlock: ...
        def visit_Method(self, node) -> TextBlock: ...
        def visit_Initializer(self, node) -> TextBlock: ...
        def visit_EventHandler(self, node) -> TextBlock: ...
        def visit_Body(self, node) -> TextBlock: ...
        def visit_VoidCall(self, node) -> TextBlock: ...
        def visit_Call(self, node) -> TextBlock: ...
        def visit__literal(self, node) -> TextBlock: ...
        def visit_fString(self, node) -> TextBlock: ...
        def visit_ID(self, node) -> TextBlock: ...
        def visit_Become(self, node) -> TextBlock: ...
        def visit_EventOverPort(self, node) -> TextBlock: ...
        def visit_EventToSub(self, node) -> TextBlock: ...

.. note::

   ``_render_args`` (called by ``visit_Call``) contains ``assert False`` and
   is currently WIP -- argument bundling for ``Call`` nodes is not yet complete.
   See ``doc/CodeAI-analysis/ToDo/intentional-dead-code.rst``.

----

Helper visitors -- Walker, Portray, IDRef
------------------------------------------

These three helpers are owned by the ``Renderer`` and each answer exactly one
question.  See ``doc/CodeAI-analysis/VisitorsInsight/index.rst`` for a full
discussion of the collaboration pattern.

``Walker`` -- tree traversal
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

*Module:* ``castle.writers.RPy.writer.walker``
(`walker.py
<../../../core_packages/castle-RPy-writer/castle/writers/RPy/writer/walker.py>`_ /
`walker.pyi
<../../../core_packages/castle-RPy-writer/castle/writers/RPy/writer/walker.pyi>`_)

*"What are the child nodes of this node?"*

``Walker`` is a ``Visitor`` subclass whose ``visit_*`` methods return tuples of
child AIGR nodes.  An unhandled node type returns an empty tuple (the
``_defaultType = tuple`` mechanism).

.. code-block:: python

    from castle.writers.RPy.writer.walker import Walker

    w = Walker()
    children = w.visit(a_component_implementation)  # -> tuple of nodes

.. code-block:: python

    class Walker(Visitor):
        def visit__NameSpace(self, node) -> Sequence[AIGR]: ...
        def visit__Named_callable(self, node) -> Sequence[AIGR]: ...
        def visit_ComponentImplementation(self, node) -> Sequence[AIGR]: ...
        def visit_Body(self, node) -> Sequence[AIGR]: ...
        def visit_VoidCall(self, node) -> Sequence[AIGR]: ...
        def visit_Call(self, node) -> Sequence[AIGR]: ...
        def visit_fString(self, node) -> Sequence[AIGR]: ...

``Portray`` -- name translation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

*Module:* ``castle.writers.RPy.writer.portray``
(`portray.py
<../../../core_packages/castle-RPy-writer/castle/writers/RPy/writer/portray.py>`_ /
`portray.pyi
<../../../core_packages/castle-RPy-writer/castle/writers/RPy/writer/portray.pyi>`_)

*"How is this AIGR name spelled in RPy?"*

``Portray`` is a plain (non-Visitor) class with pure string-manipulation
methods.  Every generated symbol has a well-defined prefix:

=============================== ==============================================
Method                          Example result
=============================== ==============================================
``CC_cls_prefix("Counter")``    ``'CC_Counter'``
``cc_CI_elm_prefix("Counter")`` ``'cc_CI_Counter'``
``cc_C_elm_prefix("Counter")``  ``'cc_C_Counter'``
``cc_S_dispatchTable("C","p")`` ``'cc_S_C_p'``
``CC_P_eventTrigger("P","e")``  ``'CC_P_P_e'``
``CC_ProtocolName_prefix("P")`` ``'cc_P_P'``
=============================== ==============================================

``PortrayType`` is a companion ``Visitor`` subclass (custom ``'prefix'``
phase) that maps a Castle AIGR type object to its ``CC_B_*`` class name
(e.g. ``aigr.types.int`` -> ``'CC_B_int'``).

.. code-block:: python

    from castle.writers.RPy.writer.portray import Portray, PortrayType

    p = Portray(renderer)
    p.CC_cls_prefix("Counter")     # -> 'CC_Counter'
    p.PortDirection(port)          # -> 'buildin.CC_PortDirection.In'

    pt = PortrayType()
    pt.prefix(aigr.types.int)      # -> 'CC_B_int'

``IDRef`` -- reference resolution
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

*Module:* ``castle.writers.RPy.writer.idref``
(`idref.py
<../../../core_packages/castle-RPy-writer/castle/writers/RPy/writer/idref.py>`_ /
`idref.pyi
<../../../core_packages/castle-RPy-writer/castle/writers/RPy/writer/idref.pyi>`_)

*"How do I render this ID, given what it points to?"*

``IDRef`` uses the ``dispatch_on`` feature of ``monorail``'s ``Visitor``: its
``portray(id_node)`` method calls ``visit(id_node, dispatch_on=reference)``
so the handler is chosen by the *target's* class, not the ID's class.

.. code-block:: python

    from castle.writers.RPy.writer.idref import IDRef

    class IDRef(Visitor):
        def portray(self, node: aigr.ID) -> str: ...  # main entry
        def visit_ComponentInterface(self, node) -> str: ...  # -> 'cc_CI_...'
        def visit_ComponentImplementation(self, node) -> str: ...  # -> 'CC_...'
        def visit__Named_callable(self, node) -> str: ...
        def visit_AIGR(self, node) -> str: ...          # catch-all fallback
        def visit_str(self, node) -> str: ...

----

``Machinery`` -- dispatch-table strategy
-----------------------------------------

*Module:* ``castle.writers.RPy.writer.machinery``
(`_machinery.py
<../../../core_packages/castle-RPy-writer/castle/writers/RPy/writer/machinery/_machinery.py>`_ /
`_machinery.pyi
<../../../core_packages/castle-RPy-writer/castle/writers/RPy/writer/machinery/_machinery.pyi>`_)

*"How do I emit the event dispatch-table and event-send plumbing?"*

``Machinery`` is an abstract strategy (ABC + factory).  ``Machinery.__new__``
consults an internal registry keyed by a *hint* string and returns the matching
concrete subclass.  The default (no hint) returns :class:`M_DC_chained_dict`.

Concrete backends registered out of the box
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

================================= ==========================================
Hint strings                      Class
================================= ==========================================
``"chained-dict"`` (and aliases)  :class:`M_DC_chained_dict` **(default)**
``"flat-dict"`` (and aliases)     :class:`M_DC_flat_dict`
``"tuple"``                       :class:`M_DC_tuple`
``"list"``                        :class:`M_DC_list`
================================= ==========================================

``M_DC_chained_dict`` is the only fully-implemented backend today.  The
others exist as registration stubs.

How to use it
~~~~~~~~~~~~~

.. code-block:: python

    from castle.writers.RPy.writer.machinery import Machinery

    m = Machinery()                     # -> M_DC_chained_dict (default)
    m = Machinery("chained-dict")       # explicit
    m = Machinery("flat-dict")          # selects M_DC_flat_dict

    # Use inside Renderer:
    renderer = Renderer(machinery=Machinery("chained-dict"))

Registering a custom backend
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    @Machinery.register("my-backend", default=False)
    class MyMachinery(Machinery):
        def render_EventDispatchTable(self, renderer, node) -> Block: ...
        def render_EventOverPort(self, renderer, node) -> Block: ...
        def render_EventToSub(self, renderer, node) -> Block: ...

Public signatures
~~~~~~~~~~~~~~~~~~

.. code-block:: python

    class Machinery(ABC):
        _register: ClassVar[dict[str, type]]
        _default_hint: ClassVar[Any]
        arg_bundler: Bundler        # always NativeBundler

        def __new__(cls, hint: str = "", **kwargs) -> Machinery: ...
        @classmethod
        def register(cls, *hints, default=False) -> Callable[[type], type]: ...

        @abstractmethod
        def render_EventDispatchTable(self, renderer, node) -> Block: ...
        @abstractmethod
        def render_EventOverPort(self, renderer, node) -> Block: ...
        @abstractmethod
        def render_EventToSub(self, renderer, node) -> Block: ...

``Bundler`` / ``NativeBundler`` -- argument packing
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

*Module:* ``castle.writers.RPy.writer.machinery`` (``_bundler.py``,
``native_bundler.py``)
(`_bundler.py
<../../../core_packages/castle-RPy-writer/castle/writers/RPy/writer/machinery/_bundler.py>`_,
`native_bundler.py
<../../../core_packages/castle-RPy-writer/castle/writers/RPy/writer/machinery/native_bundler.py>`_)

``Bundler`` defines the four-step argument calling convention (box / pack /
unpack / unbox).  ``Bundler.__new__`` always returns a ``NativeBundler``.  The
native convention wraps each argument in a ``CC_B_<type>`` class and packs
them as ``[CC_B_int(v1), ...], {}``.

.. note::

   ``NativeBundler.unpack`` is WIP and raises ``AssertionError``.

----

``aid`` -- the Block text buffer
---------------------------------

*Module:* ``castle.writers.RPy.aid``
(`block.py
<../../../core_packages/castle-RPy-writer/castle/writers/RPy/aid/block.py>`_ /
`block.pyi
<../../../core_packages/castle-RPy-writer/castle/writers/RPy/aid/block.pyi>`_,
`convert.py
<../../../core_packages/castle-RPy-writer/castle/writers/RPy/aid/convert.py>`_ /
`convert.pyi
<../../../core_packages/castle-RPy-writer/castle/writers/RPy/aid/convert.pyi>`_)

``Block`` is the indented text buffer used throughout the renderer.  Every
``visit_*`` method returns a ``TextBlock`` (which is ``Optional[str | Block]``).

.. code-block:: python

    from castle.writers.RPy.aid import Block, TextBlock

    txt = Block("class Foo(Base):")
    body = Block("def method(self): pass")
    txt.sub(body)         # adds body as indented child
    txt += "extra_line"   # appends without extra indent
    print(str(txt))
    # class Foo(Base):
    #     def method(self): pass
    # extra_line

``fString_2_modulo`` (in ``convert.py``) converts Castle f-strings
(``"Hello {name}"``) to Python ``%``-style format strings
(``"Hello %s", ("name",)``).

----

``aigr`` -- RPy-writer-internal AIGR extensions
-------------------------------------------------

*Package:* ``castle.writers.RPy.aigr``
(`dispatch_tables.py
<../../../core_packages/castle-RPy-writer/castle/writers/RPy/aigr/dispatch_tables.py>`_ /
`dispatch_tables.pyi
<../../../core_packages/castle-RPy-writer/castle/writers/RPy/aigr/dispatch_tables.pyi>`_,
`units.py
<../../../core_packages/castle-RPy-writer/castle/writers/RPy/aigr/units.py>`_ /
`units.pyi
<../../../core_packages/castle-RPy-writer/castle/writers/RPy/aigr/units.pyi>`_)

These are writer-internal AIGR extensions, **not** part of the public
``castle-aigr`` package.

``RPy_unit`` / ``ScaffolderUnit``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``RPy_unit`` represents a single output ``.py`` file: it is a
``castle.aigr.NamedNode`` + ``_Target_NS`` (carries a ``target_file`` path
and all top-level AIGR nodes to render).  Created by :func:`Source2RPy`.

``ScaffolderUnit`` wraps an ``RPy_unit`` and adds file-write capability:

.. code-block:: python

    from castle.writers.RPy.aigr.units import ScaffolderUnit

    su = ScaffolderUnit(unit)
    su.write_out(inDir="build/")
    # or step by step:
    txt = Renderer().render(unit)
    su.save(txt, inDir="build/")

``EventDispatchTable`` / ``Build_EventDispatchTable``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``EventDispatchTable`` (a temporary AIGR node) collects the
``(protocol, event) -> handler_name`` mapping for one port of one component.
It is built by ``Build_EventDispatchTable(comp, port_name)`` during rendering
and consumed by ``Machinery.render_EventDispatchTable``.

.. code-block:: python

    from castle.writers.RPy.aigr.dispatch_tables import Build_EventDispatchTable

    table = Build_EventDispatchTable(comp=comp_node, port_name=port_id)
    # -> EventDispatchTable_Scaffolder

----

``transformers`` -- AIGR-to-AIGR transformation
-------------------------------------------------

*Package:* ``castle.writers.RPy.transformers``
(`namespace.py
<../../../core_packages/castle-RPy-writer/castle/writers/RPy/transformers/namespace.py>`_ /
`namespace.pyi
<../../../core_packages/castle-RPy-writer/castle/writers/RPy/transformers/namespace.pyi>`_)

``Source2RPy`` is the transformer that prepares an AIGR for rendering.  It
takes an ``aigr.Source_NS`` (produced by the Castle reader) and returns an
``RPy_unit`` with the correct output file name.

.. code-block:: python

    from castle.writers.RPy.transformers import Source2RPy

    unit = Source2RPy(source_ns)
    # with explicit output file name:
    unit = Source2RPy(source_ns, filename="my_component.py")

.. code-block:: python

    def Source2RPy(
        src: aigr.Source_NS,
        filename: str | None = None,
        ext: str | None = None,       # default: 'py'
    ) -> RPy_unit: ...

----

``translators`` -- running the generated code
----------------------------------------------

*Package:* ``castle.writers.RPy.translators``
(`base.py
<../../../core_packages/castle-RPy-writer/castle/writers/RPy/translators/base.py>`_ /
`base.pyi
<../../../core_packages/castle-RPy-writer/castle/writers/RPy/translators/base.pyi>`_,
`eval.py
<../../../core_packages/castle-RPy-writer/castle/writers/RPy/translators/eval.py>`_ /
`eval.pyi
<../../../core_packages/castle-RPy-writer/castle/writers/RPy/translators/eval.pyi>`_,
`real.py
<../../../core_packages/castle-RPy-writer/castle/writers/RPy/translators/real.py>`_ /
`real.pyi
<../../../core_packages/castle-RPy-writer/castle/writers/RPy/translators/real.pyi>`_)

The translators drive external tools on the generated ``.py`` files.  Each is a
``TranslatorCommand`` subclass; calling ``.execute()`` runs setup -> runner ->
teardown.

===================  =======================================================
Class                What it does
===================  =======================================================
``Evaluate``         Runs the file with CPython (``python <driver>.py``)
``Compile``          Compiles with RPython (``rpython --batch ...``)
``Execute``          Runs a previously compiled RPython binary
===================  =======================================================

.. code-block:: python

    from castle.writers.RPy.translators import Evaluate, Compile, Execute

    # Run with CPython:
    out = Evaluate(inDir="build/", driver="output").execute()

    # Compile to native binary:
    Compile(inDir="build/", driver="output", into="my_app").execute()

    # Run the native binary:
    out = Execute(inDir="build/", into="my_app").execute()

.. warning::

   ``PYPY2_BINd`` and ``RPYTHON`` paths in ``base.py`` are hard-coded
   platform-specific strings.  They must be updated for other environments.

----

``RPy_buildin`` -- the Castle runtime library
----------------------------------------------

*Package:* ``castle.writers.RPy_buildin``
(import root: ``castle.writers.RPy_buildin``)

The ``RPy_buildin`` package is the **runtime support library** that generated
Castle code imports.  It is written in RPython-compatible Python (no ``typing``
module, old-style type comments for documentation only).

Every generated ``.py`` file starts with::

    from castle.writers.RPy_buildin import buildin
    from castle.writers.RPy_buildin import base

``buildin`` sub-package
~~~~~~~~~~~~~~~~~~~~~~~~

*Package:* ``castle.writers.RPy_buildin.buildin``
(`buildin/__init__.py
<../../../core_packages/castle-RPy-writer/castle/writers/RPy_buildin/buildin/__init__.py>`_)

============================ ==================================================
Class                        Role
============================ ==================================================
``CC_B_ComponentInterface``  Static descriptor for a component's interface
``CC_B_ComponentClass``      Static descriptor for a component's implementation
``CC_B_Component``           Base class for all generated component classes
``CC_B_C_PortID``            Describes one port on a component interface
``CC_B_OutPort``             Runtime connected output port
``CC_B_Protocol``            Descriptor for a Castle protocol
``CC_B_P_EventID``           Describes one event in a protocol
``CC_B_Value`` / subtypes    Argument wrappers (``CC_B_int``, ``CC_B_string``, ...)
``CC_ProtocolKind``          RPython-compatible enum (Unknown/Event/Data/Stream)
``CC_PortDirection``         RPython-compatible enum (In/Out/BiDir/Master/Slave)
``ChainedDict``              Chained dispatch table (``buildin.machinery``)
============================ ==================================================

.. code-block:: python

    from castle.writers.RPy_buildin import buildin, base

    # Create a protocol:
    cc_P_Clock = buildin.CC_B_Protocol(
        name="Clock", kind=buildin.CC_ProtocolKind.Event,
        inherit_from=None, events=[],
    )
    cc_P_Clock.events.append(buildin.CC_B_P_EventID(
        name="tick", seqNo=0, part_of=cc_P_Clock,
    ))

    # Create a component interface:
    cc_CI_Counter = buildin.CC_B_ComponentInterface(
        name="Counter", inherit_from=base.cc_CI_Component, ports=[],
    )
    cc_CI_Counter.ports.append(buildin.CC_B_C_PortID(
        name="clk", portNo=-1, protocol=cc_P_Clock,
        direction=buildin.CC_PortDirection.In, part_of=cc_CI_Counter,
    ))

    # Create a component class (metadata):
    cc_C_Counter = buildin.CC_B_ComponentClass(interface=cc_CI_Counter)

    # A generated component class looks like:
    class CC_Counter(buildin.CC_B_Component):
        def __init__(self, *args):
            buildin.CC_B_Component.__init__(self, isa=cc_C_Counter)
            self._castle_init(*args)

``base`` module
~~~~~~~~~~~~~~~~

*Module:* ``castle.writers.RPy_buildin.base``
(`base.py
<../../../core_packages/castle-RPy-writer/castle/writers/RPy_buildin/base.py>`_ /
`base.pyi
<../../../core_packages/castle-RPy-writer/castle/writers/RPy_buildin/base.pyi>`_)

Provides ``cc_CI_Component``, the root component interface (no ports, no
parent) that every generated interface ultimately derives from.

``HACK`` sub-package
~~~~~~~~~~~~~~~~~~~~

*Package:* ``castle.writers.RPy_buildin.HACK``
(`std.py
<../../../core_packages/castle-RPy-writer/castle/writers/RPy_buildin/HACK/std.py>`_ /
`std.pyi
<../../../core_packages/castle-RPy-writer/castle/writers/RPy_buildin/HACK/std.pyi>`_)

A temporary hard-coded ``std`` protocol (invoke/stdin/stdout/stderr) and a
``Main`` component interface.  The ``HACK`` name signals this is scaffolding
that should eventually be generated from Castle source.

----

Complete usage example
-----------------------

The following sketch shows the full compile-and-run flow from an AIGR to
executed RPy output.

.. code-block:: python

    import logging
    from castle.aigr import Source_NS, ID
    # ... (populate source_ns with AIGR nodes via the TatSu reader or by hand)

    from castle.writers.RPy.transformers import Source2RPy
    from castle.writers.RPy.aigr.units import ScaffolderUnit
    from castle.writers.RPy.translators import Evaluate

    # Step 1: transform AIGR -> RPy_unit
    unit = Source2RPy(source_ns, filename="my_component.py")

    # Step 2: render + write to disk
    su = ScaffolderUnit(unit)
    su.write_out(inDir="build/")

    # Step 3: evaluate with CPython
    out = Evaluate(inDir="build/", driver="my_component").execute()
    print(out)

    # Or to compile with RPython:
    from castle.writers.RPy.translators import Compile, Execute
    Compile(inDir="build/", driver="my_component", into="cc_app").execute()
    out = Execute(inDir="build/", into="cc_app").execute()
