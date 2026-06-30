.. (C) Albert Mietus, 2026. CodeAI=GH.Claude.Opus-4.8

castle-monorail
===============

The dependency-free **foundation** of CCastle. It provides the generic
*visitor* machinery that every reader and writer builds on: type-based method
dispatch over an object's MRO, organised in phases.

.. contents:: On this page
   :local:
   :depth: 1

At a glance
-----------

==========================  ====================================================
Package                     ``castle-monorail`` (version 0.0.2)
Depends on                  *nothing* (this is the base of the hierarchy)
Import root                 ``castle.monorail``
Public API                  :class:`MRO_Dispatch_Mixin`, :class:`Visitor`
==========================  ====================================================

::

    from castle.monorail.base.visitors import Visitor

----

``Visitor`` -- the class you subclass
-------------------------------------

*Module:* ``castle.monorail.base.visitors``
(`visitors.py
<../../../base_packages/castle-monorail/castle/monorail/base/visitors.py>`_ /
`visitors.pyi
<../../../base_packages/castle-monorail/castle/monorail/base/visitors.pyi>`_)

``Visitor`` turns a class full of ``visit_<ClassName>`` methods into a tree
walker. You do not register anything: a handler is found by **name**, by walking
the node's MRO.

How to use it
~~~~~~~~~~~~~

#. Subclass ``Visitor``.
#. Add a ``visit_<ClassName>`` method for each node type you care about.
   Because lookup walks the MRO, a handler on a *base* class is a catch-all for
   all its subclasses (e.g. ``visit_AIGR`` catches every AIGR node).
#. Optionally add ``depart_<ClassName>`` to run *after* a node's children.
#. Drive it by calling ``visit(node)``.

.. code-block:: python

    from castle.monorail.base.visitors import Visitor

    class Printer(Visitor):
        def visit_AIGR(self, node):        # catch-all: AIGR is the common base
            print('enter', node)
        def depart_Component(self, node):  # runs after the Component's children
            print('leave', node.name)

    Printer().visit(some_tree)

Two phases
~~~~~~~~~~

The method *prefix* selects the phase:

``visit``
    Runs *before* the children. The main phase.
``depart``
    Runs *after* the children. Optional -- the default is a no-op, so you only
    add ``depart_*`` methods where you need post-order work.

Dispatching on another object
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``visit(node, dispatch_on=other)`` chooses the handler by ``type(other)`` but
still passes ``node`` to it. This indirection is the key that makes
reference-resolution possible (see the RPy-writer's ``IDRef``): you can render a
*reference to* a node differently from the node itself.

Custom phases (advanced)
~~~~~~~~~~~~~~~~~~~~~~~~~~

The phases are just the entries of the class attribute ``_prefixes`` (default
``('visit', 'depart')``). Set your own and call the low-level
``_visitor(node, prefix=...)`` to build a non visit/depart dispatcher:

.. code-block:: python

    class PortrayType(Visitor):
        _prefixes = ('prefix',)
        def prefix(self, t):
            return self._visitor(t, prefix='prefix')   # dispatches prefix_<ClassName>
        def prefix_ComponentImplementation(self, t):
            return 'CC_B_Component'

Public signatures
~~~~~~~~~~~~~~~~~~

.. code-block:: python

    class Visitor(MRO_Dispatch_Mixin):
        _prefixes: tuple[str, ...]          # default ('visit', 'depart')
        def visit(self, node, dispatch_on=None) -> Any: ...
        def depart(self, node, dispatch_on=None) -> Any: ...
        # protected extension points:
        def _visitor(self, node, dispatch_on=None, prefix='visit') -> Any: ...
        def _default_visit(self, node) -> Any: ...    # warns; override for a real catch-all
        def _default_depart(self, node) -> None: ...  # no-op by design

----

``MRO_Dispatch_Mixin`` -- the dispatch engine
---------------------------------------------

*Module:* ``castle.monorail.base.dispatch``
(`dispatch.py
<../../../base_packages/castle-monorail/castle/monorail/base/dispatch.py>`_ /
`dispatch.pyi
<../../../base_packages/castle-monorail/castle/monorail/base/dispatch.pyi>`_)

The mechanism underneath ``Visitor``. You rarely use it directly, but it is the
right base when you want type-dispatch **without** the visit/depart vocabulary.

For a ``node`` and a ``prefix`` it resolves ``<prefix>_<ClassName>`` by walking
``type(node).mro()`` (most-derived first), then falls back to
``_default_<prefix>``.

.. code-block:: python

    from castle.monorail.base.dispatch import MRO_Dispatch_Mixin

    class Sizer(MRO_Dispatch_Mixin):
        _prefixes = ('size',)
        def size_int(self, n): return 4

    m = Sizer()
    handler = m.dispatch_find_method_by_mro(42, 'size')   # -> size_int (int is in bool's MRO too)

Public signatures
~~~~~~~~~~~~~~~~~~

.. code-block:: python

    class MRO_Dispatch_Mixin:
        _prefixes: tuple[str, ...]          # declare the prefixes you use
        def dispatch_check_prefix(self, prefix) -> bool: ...
        def dispatch_find_method_by_mro(self, node, prefix) -> Callable | None: ...

.. tip::

   Always set ``_prefixes`` in your subclass. An unknown prefix does not fail,
   but it is logged as a warning -- a cheap guard against typos in phase names.
