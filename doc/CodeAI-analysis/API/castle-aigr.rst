.. (C) Albert Mietus, 2026. CodeAI=GH.Claude.Opus-4.8

castle-aigr
===========

The **AIGR** -- *Abstract Intermediate Graph Representation* -- is the in-memory
data model of a parsed Castle program. It is a tree-shaped graph of small
dataclasses (one class per language concept: events, protocols, ports,
components, statements, expressions, ...). *Readers* (e.g. the TatSu reader)
**produce** an AIGR; *writers* (e.g. the RPy writer) **consume** it. AIGR sits
one level above :doc:`castle-monorail` in the hierarchy: every AIGR node is
walkable by a ``monorail`` ``Visitor``.

.. contents:: On this page
   :local:
   :depth: 1

At a glance
-----------

==========================  ====================================================
Package                     ``castle-aigr`` (version 0.0.5)
Depends on                  ``castle-monorail``
Import roots                ``castle.aigr`` and ``castle.aigr_extra``
Root node                   :class:`AIGR` / :class:`AIGRNode` (every node is one)
Names                       ``ID`` (with ``Def``/``Ref`` context), ``Label``, ``QualID``
Types                       ``types.int``, ``types.float``, ``types.string``, ``types.boolean``
Structural nodes            ``Event``, ``Protocol``/``EventProtocol``, ``Port``, ``ComponentInterface``
Statements                  ``Body``, ``If``, ``Become``, ``VoidCall``, ``Method``, ``EventHandler``, ``ComponentImplementation``, ``VariableDefintion``
Expressions                 ``Call``, ``Part``, ``Constant``, ``fString``, ``Compare``, ``LRexpression``/``RLexpression``/``Unaryexpression``
Namespaces                  ``Source_NS``, ``Scope`` (data) + ``ScaffolderNameSpace`` (behaviour)
Tooling                     ``castle.aigr.tools.scaffolding`` (wrap, register, traverse)
Extras                      ``castle.aigr_extra`` (``mangle_event_handler``, expression builders)
==========================  ====================================================

Almost everything public is re-exported from the package root, so a single
import is usually enough::

    from castle.aigr import (
        ID, Event, EventProtocol, Port, PortDirection, ComponentInterface,
        types,
    )

The namespace **behaviour** (register/find names) and node traversal live in the
scaffolding tools::

    from castle.aigr.tools.scaffolding import ScaffolderNameSpace, AutoScaffolder

----

Base -- the root node, names, types and errors
----------------------------------------------

*Modules:* ``castle.aigr.base.AIGR``, ``.names``, ``.types``, ``.errors``
(`AIGR.py <../../../base_packages/castle-aigr/castle/aigr/base/AIGR.py>`_,
`names.py <../../../base_packages/castle-aigr/castle/aigr/base/names.py>`_,
`types.py <../../../base_packages/castle-aigr/castle/aigr/base/types.py>`_,
`errors.py <../../../base_packages/castle-aigr/castle/aigr/base/errors.py>`_)

Every node derives from :class:`AIGR`; nodes that live in the tree derive from
:class:`AIGRNode`, which adds the generic ``parent`` link. ``AIGR`` is abstract
-- instantiating it raises ``NotImplementedError``; always build a concrete
subclass.

Names are :class:`ID` objects. An ``ID`` *is* a ``str`` but also carries an
optional **context**: is this occurrence a *definition* (``Def``) or a
*reference* (``Ref``)? References can later be resolved to the real node.

Types are *unique objects* (not Python types): use the ready-made singletons in
``types`` instead of constructing your own for built-ins.

How to use it
~~~~~~~~~~~~~

.. code-block:: python

    from castle.aigr import ID, types
    from castle.aigr.base.names import Label, QualID

    a   = ID("amount")                 # a plain name
    defn = ID.Def("amount")            # a defining occurrence
    ref  = ID.Ref("amount", defn)      # a reference (optionally resolved)

    t = types.int                      # the built-in int type singleton
    assert t.represents == "int"

Errors are ``Warning`` subclasses (recoverable by default) and are *not* AIGR
nodes. Catch ``errors.NameError`` from name look-ups and ``errors.PartError``
from illegal attribute/index access.

Public signatures
~~~~~~~~~~~~~~~~~~

.. code-block:: python

    @dataclass
    class AIGR: ...
    @dataclass
    class AIGRNode(AIGR):
        parent: AIGR | None = None        # keyword-only

    class ID(str, AIGR):
        context: _Context | None
        @staticmethod
        def Def(name: str) -> ID: ...
        class Ref(Generic[RefType]):      # ID.Ref(name, target); ID.Ref[T] as hint
            ...

    # types: int, float (numbers), string, boolean -- singletons of _types
    # errors: AIGR_ERROR (base), NameError, PartError

----

Structural nodes
----------------

*Modules:* ``castle.aigr.nodes``, ``.events``, ``.protocols``, ``.interfaces``,
``.namespaces``
(`nodes.py <../../../base_packages/castle-aigr/castle/aigr/nodes.py>`_,
`events.py <../../../base_packages/castle-aigr/castle/aigr/events.py>`_,
`protocols.py <../../../base_packages/castle-aigr/castle/aigr/protocols.py>`_,
`interfaces.py <../../../base_packages/castle-aigr/castle/aigr/interfaces.py>`_,
`namespaces.py <../../../base_packages/castle-aigr/castle/aigr/namespaces.py>`_)

These are the building blocks of a component-based Castle program. Most derive
from :class:`NamedNode` (an ``AIGRNode`` with a ``name``; a plain ``str`` name
is auto-wrapped into a defining ``ID``).

* :class:`Event` -- a (remote) call: a name, an optional return type and typed
  parameters.
* :class:`Protocol` / :class:`EventProtocol` -- a protocol is a set of events;
  ``based_on`` lets one protocol extend another (only *new* events are stored).
* :class:`Port` -- a named, directed connection point typed by a protocol; its
  ``ID`` lives in the owning component's namespace.
* :class:`ComponentInterface` -- the interface of a component: the protocol it
  is ``based_on`` and its ``ports``.

How to use it
~~~~~~~~~~~~~

.. code-block:: python

    from castle.aigr import (
        ID, Event, EventProtocol, ProtocolKind,
        Port, PortDirection, ComponentInterface, types,
    )
    from castle.aigr.aid import TypedParameter

    tick = Event("tick", typedParameters=(TypedParameter("n", types.int),))
    clock = EventProtocol(ID("Clock"), events=(tick,))

    clk_in = Port("clk", direction=PortDirection.In, type=clock)
    comp   = ComponentInterface(ID("Counter"),
                                based_on=None,
                                ports=(ID.Ref("clk", clk_in),))

Namespaces (``_NameSpace``, :class:`NamedSpace`, :class:`Source_NS`,
:class:`Scope`) are the *data* side of scoping -- they store ``outer_ns`` and a
local name map. The look-up/registration *behaviour* is added by
``ScaffolderNameSpace`` (see `Tooling`_), so build the node here and drive it
through the scaffolder.

Public signatures
~~~~~~~~~~~~~~~~~~

.. code-block:: python

    @dataclass
    class NamedNode(AIGRNode):
        name: ID | str

    @dataclass
    class Event(NamedNode):
        return_type: type | None = None
        typedParameters: Sequence[TypedParameter] = ()

    @dataclass
    class EventProtocol(Protocol):
        kind: ProtocolKind = ProtocolKind.Event
        events: Sequence[Event]

    @dataclass
    class Port(NamedNode):
        direction: PortDirection
        type: Protocol | type

    @dataclass
    class ComponentInterface(NamedNode):
        based_on: ID.Ref[Protocol | Specialise] | None = None
        ports: Sequence[ID.Ref[Port]] = ()

----

Statements
----------

*Modules:* ``castle.aigr.statements`` package -- ``.compounds``, ``.flow``,
``.simple``, ``.defs``, ``.callables``
(`compounds.py <../../../base_packages/castle-aigr/castle/aigr/statements/compounds.py>`_,
`flow.py <../../../base_packages/castle-aigr/castle/aigr/statements/flow.py>`_,
`simple.py <../../../base_packages/castle-aigr/castle/aigr/statements/simple.py>`_,
`defs.py <../../../base_packages/castle-aigr/castle/aigr/statements/defs.py>`_,
`callables.py <../../../base_packages/castle-aigr/castle/aigr/statements/callables.py>`_)

A statement is anything that appears in a body. The common base is
``_statement``; you use the concrete leaves:

* :class:`Body` -- the list of statements between ``{`` and ``}``.
* :class:`If` -- a ``test`` plus a ``body`` and an optional ``orelse`` (another
  ``Body`` for ``else``, or another ``If`` for ``elif``).
* :class:`Become` -- assignment ``targets := values`` (currently single).
* :class:`VoidCall` -- wraps a ``Call`` expression so it can stand as a statement.
* :class:`Method` / :class:`Initializer` / :class:`EventHandler` -- named
  callables with ``parameters``, a ``body`` and a ``returns`` type.
* :class:`ComponentImplementation` -- the ``implement`` of a component; its
  ``{ ... }`` is a *namespace*, not a ``Body``.
* :class:`VariableDefintion` -- declare a variable with a ``type`` and optional
  ``value``. (Name keeps the source spelling.)

How to use it
~~~~~~~~~~~~~

.. code-block:: python

    from castle.aigr import Body, If, Become, Method, ID
    from castle.aigr.expressions import Constant

    assign = Become(targets=(ID("a"),), values=(Constant(value=1),))
    body   = Body(statements=[assign])
    branch = If(test=Constant(value=True), body=body)

    m = Method(ID("reset"), body=Body())

An :class:`EventHandler` fires when a protocol-event arrives on a port. Each of
``protocol``/``event``/``port`` is an ``ID`` with a ``Ref`` context (or
``'default'``); its blended ``name`` is best computed with
``mangle_event_handler`` (see `Extras`_).

Public signatures
~~~~~~~~~~~~~~~~~~

.. code-block:: python

    @dataclass
    class Body(_statement):
        statements: list[_statement] = []

    @dataclass
    class If(_statement):
        test: AIGR; body: AIGR; orelse: AIGR | None = None

    @dataclass
    class Become(_statement):
        targets: tuple[AIGR]; values: tuple[AIGR]

    @dataclass
    class EventHandler(_handlers):
        protocol: ID; event: ID; port: ID         # + parameters, body, returns

    @dataclass
    class ComponentImplementation(_hasScope, _statement, NamedNode):
        interface: ComponentInterface | None = None
        parameters: tuple[TypedParameter, ...] = ()
        handlers: list[_handlers] = []

----

Expressions
-----------

*Modules:* ``castle.aigr.expressions`` package -- ``.calls``, ``.literals``,
``.operators``, ``.operator_expressions``
(`calls.py <../../../base_packages/castle-aigr/castle/aigr/expressions/calls.py>`_,
`literals.py <../../../base_packages/castle-aigr/castle/aigr/expressions/literals.py>`_,
`operators.py <../../../base_packages/castle-aigr/castle/aigr/expressions/operators.py>`_,
`operator_expressions.py <../../../base_packages/castle-aigr/castle/aigr/expressions/operator_expressions.py>`_)

An expression yields a value (base class ``_expression``):

* :class:`Call` -- ``callable(arguments)``; ``callable`` is usually an ``ID``.
* :class:`Part` -- ``a.b`` (attribute) **or** ``a[i]`` (index) -- exactly one,
  else ``errors.PartError``.
* :class:`Constant` / :class:`fString` -- literals; ``fString`` is f-string-like.
* :class:`Compare` -- two-or-more value comparison, cascadable (``1 < 2 < 3``).
* :class:`LRexpression` / :class:`RLexpression` / :class:`Unaryexpression` --
  operator applications. The ``operators`` module holds value-less marker
  classes (``Add``, ``Sub``, ``Times``, ``Power``, ``Less``, ``And`` ...).

Prefer the high-level **builders** in ``castle.aigr_extra`` over assembling
operator nodes by hand (see `Extras`_).

How to use it
~~~~~~~~~~~~~

.. code-block:: python

    from castle.aigr import ID
    from castle.aigr.expressions import Call, Part, Constant, Compare
    from castle.aigr.expressions import operators

    call = Call(callable=ID.Ref("reset", None), arguments=(Constant(value=0),))
    attr = Part(ID("self"), attribute=ID("count"))
    cmp  = Compare(ops=operators.Less(), values=(Constant(value=1), Constant(value=2)))

Public signatures
~~~~~~~~~~~~~~~~~~

.. code-block:: python

    @dataclass
    class Call(_call):
        callable: ID | AIGR
        arguments: tuple[AIGR, ...] | None = ()

    @dataclass
    class Part(_call):
        base: AIGR | None
        attribute: AIGR | None = None     # XOR with index
        index: AIGR | None = None

    @dataclass
    class Compare(_expression):
        ops: _compare_op | tuple[_compare_op]
        values: tuple[AIGR, ...]

----

machinery -- the abstract inter-component machinery
---------------------------------------------------

*Module:* ``castle.aigr.machinery``
(`machinery/__init__.py <../../../base_packages/castle-aigr/castle/aigr/machinery/__init__.py>`_)

Models *what* the runtime does between components (sending an event), as an
interface -- not how it works. Compare it with the intra-component ``Call``
expression and ``VoidCall`` statement. The two ready nodes are
:class:`EventToSub` (send to a named sub-component) and :class:`EventOverPort`
(send out through a port). Stream/data variants are placeholders.

.. code-block:: python

    from castle.aigr import ID
    from castle.aigr.machinery import EventOverPort

    send = EventOverPort(comp=ID.Ref("Counter", None),
                         outport=ID.Ref("clk", None),
                         event=ID.Ref("tick", None),
                         arguments=())

----

aid -- arguments, parameters and return types
---------------------------------------------

*Module:* ``castle.aigr.aid``
(`aid.py <../../../base_packages/castle-aigr/castle/aigr/aid.py>`_)

The small "glue" nodes shared by callables and calls:

* :class:`TypedParameter` -- a named, typed formal parameter (definition side).
* :class:`Argument` -- an actual argument (call side); positional or named.
* :class:`ReturnType` -- a callable's return type, wrapped as a node.

.. code-block:: python

    from castle.aigr import types
    from castle.aigr.aid import TypedParameter, Argument

    p = TypedParameter("n", types.int)          # def: name + type
    a = Argument(42)                             # call: positional value
    kw = Argument(42, name="n")                  # call: named value

----

Tooling -- ``tools.scaffolding``
--------------------------------

*Package:* ``castle.aigr.tools.scaffolding``
(`_scaffolder.py <../../../base_packages/castle-aigr/castle/aigr/tools/scaffolding/_scaffolder.py>`_,
`node.py <../../../base_packages/castle-aigr/castle/aigr/tools/scaffolding/node.py>`_,
`namespaces.py <../../../base_packages/castle-aigr/castle/aigr/tools/scaffolding/namespaces.py>`_,
`_auto_scaffolder.py <../../../base_packages/castle-aigr/castle/aigr/tools/scaffolding/_auto_scaffolder.py>`_)

The AIGR dataclasses are intentionally *thin* (data only). The scaffolding
tools add behaviour by **wrapping** a node: a ``_Scaffolder`` holds the real
node in ``.node`` and transparently delegates any unknown attribute to it, so a
wrapped node behaves almost like the node itself but gains extra methods.

* :class:`ScaffolderNode` adds **tree traversal**. A subclass declares which of
  the node's fields are children/attributes/links (``_kids_fields`` /
  ``_attr_fields`` / ``_link_fields``); then :meth:`kids`, :meth:`attrs` and
  :meth:`links` yield the related nodes. ``set_parent`` links nodes (chainable).
* :class:`ScaffolderNameSpace` adds the **namespace API**: ``register`` (chosen
  by node type, MRO-dispatched ``register_<Type>`` handlers), ``findNode`` /
  ``getID`` / ``search`` look-ups, ``list_names`` / ``search_dottedNames``.
* :class:`AutoScaffolder` picks the **most specific** scaffolder for a given
  node automatically (``AutoScaffolder(node)`` never returns an
  ``AutoScaffolder``; it returns, e.g., a ``ScaffolderEventProtocol``).

How to use it
~~~~~~~~~~~~~

.. code-block:: python

    from castle.aigr import Source_NS, ID, Method, Body
    from castle.aigr.tools.scaffolding import ScaffolderNameSpace, AutoScaffolder

    ns = ScaffolderNameSpace(Source_NS(ID("main.castle")))
    ns.register(Method(ID("reset"), body=Body()))   # register by type
    reset = ns.getID("reset")                        # -> the Method (or NameError)
    maybe = ns.findNode("missing")                   # -> None
    names = ns.search_dottedNames()                  # recursive dotted names

    wrapped = AutoScaffolder(some_node)              # most specific scaffolder
    for kid in wrapped.kids():
        ...

.. tip::

   Register *unwrapped* nodes. ``register`` will unwrap an accidentally-wrapped
   node (with a warning), but passing the real node is the intended use.

Public signatures
~~~~~~~~~~~~~~~~~~

.. code-block:: python

    class ScaffolderNode(_Scaffolder):
        _nodeCls: type
        _kids_fields: frozenset[str]; _attr_fields: frozenset[str]; _link_fields: frozenset[str]
        def kids(self) -> Iterator[AIGRNode]: ...
        def attrs(self) -> Iterator[AIGRNode]: ...
        def links(self) -> Iterator[AIGRNode]: ...
        def set_parent(self, parent) -> Self: ...

    class ScaffolderNameSpace(ScaffolderNode, MRO_Dispatch_Mixin):
        def register(self, named_node, asName=None) -> None: ...
        def findNode(self, name) -> NamedNode | None: ...
        def getID(self, name) -> NamedNode: ...            # raises NameError
        def search(self, dottedName) -> NamedNode | None: ...

    class AutoScaffolder(_Scaffolder):
        def __new__(cls, node) -> _Scaffolder: ...         # returns the best match

----

Extras -- ``castle.aigr_extra``
-------------------------------

*Modules:* ``castle.aigr_extra.blend.mangle``,
``castle.aigr_extra.builders.build_expr``
(`mangle.py <../../../base_packages/castle-aigr/castle/aigr_extra/blend/mangle.py>`_,
`build_expr.py <../../../base_packages/castle-aigr/castle/aigr_extra/builders/build_expr.py>`_)

Helpers that sit *beside* the core model.

* ``mangle_event_handler`` -- blend a protocol/event/port triple into the single
  ``ID`` used as an :class:`EventHandler` name. Any part omitted becomes
  ``'default'``; the result is ``ID(f'{protocol}_{event}__{port}')``. This is
  the canonical specification for that name.
* The **expression builders** (``build_expr``) generate one function per
  operator (``Add``, ``Sub``, ``Times``, ``Div``, ``Modulo``, ``Power``, ...) at
  import time, so you build operator expressions readably instead of wiring
  ``LRexpression``/``RLexpression`` by hand.

.. code-block:: python

    from castle.aigr_extra.blend.mangle import mangle_event_handler
    from castle.aigr_extra.builders import build_expr
    from castle.aigr.expressions import Constant

    name = mangle_event_handler(protocol="Clock", event="tick", port="p")
    # -> ID('Clock_tick__p')

    expr = build_expr.Add(Constant(value=1), Constant(value=2))   # -> LRexpression

.. note::

   ``build_expr.py`` contains two ``if False:`` blocks. These are **deliberate
   documentation** (kept for syntax highlighting), showing the long-hand and
   lambda forms of a builder before the meta-programmed version. They are not
   dead code.

Public signatures
~~~~~~~~~~~~~~~~~~

.. code-block:: python

    def mangle_event_handler(*, protocol=None, event=None, port=None) -> ID: ...
    def qualID_2_str(quid: QualID | ID | str) -> str: ...

    # build_expr (generated at import):
    def Add(left, right, *more) -> LRexpression: ...     # also Sub, Times, Div, Modulo
    def Power(left, right, *more) -> RLexpression: ...
