.. (C) Albert Mietus, 2026. CodeAI=GH.Claude.Opus-4.8

castle-aigr-trawlers
====================

**castle-aigr-trawlers** extends the ``castle.aigr.tools`` namespace with a
lightweight *trawling* tool: a fluent, position-aware navigator that traverses
an AIGR tree and extracts nodes from it.  It depends exclusively on
:doc:`castle-aigr` (the AIGR data model) and adds zero overhead to the core
model -- the trawler is a read-only wrapper, never a visitor.

.. contents:: On this page
   :local:
   :depth: 1

At a glance
-----------

==========================  ====================================================
Package                     ``castle-aigr-trawlers`` (version 0.0.1)
Depends on                  ``castle-aigr``
Import root                 ``castle.aigr.tools.trawlers``
Key public class            :class:`Trawl` -- fluent AIGR tree navigator
==========================  ====================================================

The single public symbol is re-exported from the package root::

    from castle.aigr.tools.trawlers import Trawl

----

``Trawl`` -- the fluent navigator
----------------------------------

*Module:* ``castle.aigr.tools.trawlers.trawl``
(`trawl.py <../../../base_packages/castle-aigr-trawlers/castle/aigr/tools/trawlers/trawl.py>`_)

A :class:`Trawl` wraps a set of AIGR nodes and allows chain-safe upward
navigation through the parent-link axis.  Every navigation step returns a
**new** :class:`Trawl`; the original is never mutated.  Navigating past the
root of the tree yields an *empty* trawl rather than raising an exception,
so callers can navigate freely and check :meth:`exists` at the end.

How to use it
~~~~~~~~~~~~~

#. Wrap a starting node with ``Trawl(node)``.
#. Navigate with :meth:`up` (one step, or ``steps=N`` for multiple levels).
#. Terminate with :meth:`one` (first node or ``None``), :meth:`all` (all nodes
   as a tuple), or :meth:`exists` (boolean guard).

.. code-block:: python

    from castle.aigr import ID, NamedNode
    from castle.aigr.tools.trawlers import Trawl

    # Build a small three-level tree (parent links set via keyword arg):
    root  = NamedNode(name=ID.Def("root"))
    child = NamedNode(name=ID.Def("child"),       parent=root)
    grand = NamedNode(name=ID.Def("grandchild"),  parent=child)

    # Navigate upward:
    t_parent = Trawl(grand).up()           # one level -> wraps child
    t_root   = Trawl(grand).up(2)          # two levels -> wraps root

    assert t_parent.exists()
    assert t_parent.one() is child

    assert t_root.one() is root

    # Safe navigation past the root:
    t_gone = Trawl(root).up()
    assert not t_gone.exists()             # empty -- no exception
    assert t_gone.one() is None
    assert t_gone.all() == ()

    # Chaining:
    names = [n.name for n in Trawl(grand).up(2).all()]   # ["root"]

.. note::

   ``up()`` silently drops nodes that are plain :class:`~castle.aigr.AIGR`
   (rather than :class:`~castle.aigr.AIGRNode`) because plain ``AIGR`` nodes
   have no ``parent`` link.  In a normal tree all internal nodes are
   ``AIGRNode``; only top-level singletons (e.g. type singletons) are plain
   ``AIGR``.

Public signatures
~~~~~~~~~~~~~~~~~

.. code-block:: python

    class Trawl:
        def __init__(self, node: AIGR) -> None: ...

        # Terminator methods -- extract results
        def exists(self) -> bool: ...                      # True if non-empty
        def one(self) -> AIGR | None: ...                  # first node or None
        def all(self) -> tuple[AIGR, ...]: ...             # all nodes

        # Navigation methods -- return a new Trawl
        def up(self, steps: int = 1) -> Trawl: ...        # walk toward root

        # Protected extension point (for subclasses)
        @classmethod
        def _of(cls, nodes: tuple[AIGR, ...]) -> Trawl: ...   # private factory
