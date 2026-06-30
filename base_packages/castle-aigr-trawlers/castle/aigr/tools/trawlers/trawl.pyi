# (C) Albert Mietus, 2026. CodeAI=GH.Claude.Opus-4.8
#
# Type stub (signatures + usage docs) for ``castle.aigr.tools.trawlers.trawl``.
# Hand-maintained "manual autodoc" companion to trawl.py.

import typing as PTH
from castle.aigr import AIGR as AIGR, AIGRNode as AIGRNode

class Trawl:
    """Fluent, position-based navigator for an AIGR tree.

    A ``Trawl`` wraps a *set* of :class:`~castle.aigr.AIGR` nodes and lets you
    move through the tree with a chainable, filter-safe API.  The result of
    every navigation step is itself a :class:`Trawl`, so steps compose without
    intermediate ``None``-checks.

    Construction
    ------------
    Pass a **single** AIGR node to the constructor::

        from castle.aigr.tools.trawlers import Trawl

        trawl = Trawl(some_node)            # wrap one node

    Navigation
    ----------
    ::

        parent = Trawl(child_node).up()          # one step up
        grandparent = Trawl(node).up(2)          # two steps up

    Termination
    -----------
    Extract results with the *terminator* methods::

        if trawl.exists():
            node = trawl.one()           # first node or None
        nodes = trawl.all()              # all nodes as a tuple (may be empty)

    Empty trawls
    ------------
    Navigating past the root of the tree (e.g. ``up()`` on a root node) yields
    an *empty* trawl.  Calling :meth:`exists` on it returns ``False``; :meth:`one`
    returns ``None``; :meth:`all` returns ``()``.  All navigation methods are
    safe on an empty trawl -- they stay empty.
    """

    def __init__(self, node: AIGR) -> None:
        """Wrap a single AIGR node in a new trawl."""
        ...

    @classmethod
    def _of(cls, nodes: tuple[AIGR, ...]) -> Trawl:
        """Private factory used internally to create a multi-node trawl.

        Do not call from application code; it bypasses the single-node
        constructor contract.  Extension points in subclasses may override
        this to return a different subclass instance.
        """
        ...

    # ------------------------------------------------------------------
    # Terminator methods (extract results from the trawl)
    # ------------------------------------------------------------------

    def exists(self) -> bool:
        """Return ``True`` if this trawl holds at least one node.

        Use as a guard before calling :meth:`one`::

            t = Trawl(node).up()
            if t.exists():
                print(t.one())
        """
        ...

    def one(self) -> PTH.Optional[AIGR]:
        """Return the first node, or ``None`` if the trawl is empty.

        Useful when exactly one result is expected::

            parent: AIGR | None = Trawl(child).up().one()
        """
        ...

    def all(self) -> tuple[AIGR, ...]:
        """Return all held nodes as an immutable tuple (may be empty).

        Use when the trawl may hold more than one node (e.g. after a future
        fan-out step)::

            nodes: tuple[AIGR, ...] = trawl.all()
        """
        ...

    # ------------------------------------------------------------------
    # Navigation methods (move through the tree; return a new Trawl)
    # ------------------------------------------------------------------

    def up(self, steps: int = 1) -> Trawl:
        """Navigate *steps* levels toward the root of the AIGR tree.

        Each step follows the ``parent`` link of every held node; nodes that
        are plain :class:`~castle.aigr.AIGR` (not :class:`~castle.aigr.AIGRNode`,
        i.e. they have no ``parent``) are silently dropped.

        Returns a new :class:`Trawl`; the original is unchanged.  Navigating
        past the root yields an empty trawl.

        ``steps`` defaults to 1.  Passing ``steps=0`` is a no-op (returns the
        same nodes wrapped in a new :class:`Trawl`).

        Example::

            grandparent = Trawl(grandchild_node).up(2).one()
        """
        ...


# ------------------------------------------------------------------
# Module-level private helper
# ------------------------------------------------------------------

def _step_up(nodes: tuple[AIGR, ...]) -> tuple[AIGR, ...]:
    """Walk one level up for every node in *nodes*.

    Private helper called by :meth:`Trawl.up`.  Drops nodes that are not
    :class:`~castle.aigr.AIGRNode` instances or whose ``parent`` is ``None``.
    """
    ...
