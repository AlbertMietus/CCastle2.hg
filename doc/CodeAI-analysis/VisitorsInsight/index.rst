.. (C) Albert Mietus, 2026. CodeAI=GH.Claude.Opus-4.8

Visitors Insight — the RPy-writer
=================================

How the visitor pattern is used in ``castle-RPy-writer``, why the "sub visitors"
help, and where they could help more.

.. contents:: Contents
   :local:
   :depth: 2


The base mechanism (monorail)
-----------------------------

All visitors inherit from ``castle.monorail.base.visitors.Visitor``, which adds
**dispatch-by-type** on top of ``MRO_Dispatch_Mixin``:

* ``visit(node)`` looks for a method ``visit_<ClassName>`` — walking the full
  **MRO** of the node, so a ``visit_AIGR`` acts as a catch-all base.
* There are **phases**, selected by a *prefix*: ``visit`` and ``depart``
  (``depart`` runs *after* the children, default no-op).
* ``visit(node, dispatch_on=...)`` can dispatch on a **different** object than
  the one passed in. This single feature is what makes ``IDRef`` possible.

.. note::

   ``PortrayType`` shows the mechanism is not limited to visit/depart: it sets
   ``_prefixes = ('prefix',)`` and dispatches ``prefix_<ClassName>``. The same
   engine, a different verb.


The collaboration today
-----------------------

The ``Renderer`` is the orchestrator (the only large file, ~304 lines). It owns
**four helpers**, each with a single, nameable job:

.. uml:: visitor-collaboration.puml

.. list-table:: The four helpers and their roles
   :header-rows: 1
   :widths: 18 22 60

   * - Helper
     - Role / pattern
     - Responsibility (the one question it answers)
   * - ``Walker``
     - Tree traversal
     - *"What are the child nodes of this node?"* — decouples *what to descend
       into* from *how to render*. Returns tuples of sub-nodes.
   * - ``Portray``
     - Naming (plain class)
     - *"How is this AIGR name spelled in RPy?"* — prefixing and name mangling.
       Mostly pure string functions; easy to read and test in isolation.
   * - ``IDRef``
     - Reference resolution
     - *"How do I render this ID, given what it points to?"* — dispatches on the
       **referenced** node's class via ``dispatch_on``.
   * - ``Machinery``
     - Strategy (pluggable)
     - *"How do I emit the dispatch-table / event plumbing?"* — an ABC whose
       ``__new__`` selects a concrete backend (``M_DC_chained_dict`` ...).

A single ``render()`` call flows through them like this:

.. uml:: render-sequence.puml


A) Do the sub-visitors help the overview?
-----------------------------------------

**Yes — clearly, and especially for humans.** The evidence is in the line-counts:
the orchestrator is 304 lines, every helper is **59–82 lines**. Each helper can
be read on its own, and its class-docstring states its single job.

The deeper win is *separation of concerns*. Without the helpers, the Renderer
would have to interleave four unrelated questions (descend? spell-the-name?
resolve-the-reference? emit-the-plumbing?) inside every ``visit_*`` method.

**One caveat.** Calling all four "sub visitors" hides that they are *four
different patterns*: a traversal visitor, a plain naming utility, a
reference-resolving visitor, and a strategy object. Naming them by **role**
(Traversal / Naming / Reference / Strategy) is itself part of keeping the
overview — see the table above.


B) Where else could they be used?
---------------------------------

The *rendering* concern inside ``Renderer`` is the next candidate to split. The
AIGR is already organised into sub-packages; the writer can mirror that:

.. uml:: renderer-split.puml

Concretely, these cohesive chunks could each become a sub-renderer:

* **ExprRenderer** — operator expressions (``Add``, ``Sub``, ``And``, ``Or``,
  ``Compare`` ... ~25 classes, none implemented yet). This is the biggest future
  growth area; keeping it out of the main Renderer prevents it ballooning.
* **LiteralRenderer** — ``visit__literal``, ``visit_fString``, ``Constant``.
* **StatementRenderer** — ``Body``, ``VoidCall``, ``If`` (missing), ``Become``.
* **StructureRenderer** — the heaviest part *today* (lines ~67–150):
  ``ComponentInterface``, ``EventProtocol``, ``_render_ComponentClass`` and the
  ``_DispatchTables`` helpers.

The pattern to copy is exactly ``IDRef``/``Walker``: a small ``Visitor`` subclass
that holds a back-reference to the ``Renderer`` and is called for its slice.


C) Other / better options to keep the overview
----------------------------------------------

Sub-visitors are good, but combine them with:

#. **Mirror the AIGR package layout** in the writer (one renderer-module per
   AIGR sub-package). Then *"where does ``visit_X`` live?"* never needs thought.
#. **An explicit registry** (node-type → renderer), the way ``Machinery``
   already registers backends. A registry is *listable* — you can print the full
   dispatch map, which a scatter of ``visit_*`` methods cannot give you.
#. **A coverage map** (doc or test) listing every AIGR node and which renderer
   handles it, plus what is still ``BUSY`` / ``NotImplementedError``. This is the
   human "you-are-here" map for an evolving code-generator.
#. **Remove noise first.** Dead scaffolding hurts the overview more than file
   size: e.g. ``XXX_OLD_visit_Call`` and the commented separators in
   ``renderer.py`` (see ``../intentional-dead-code.rst`` for the *intentional*
   cases — these old blocks are not among them).
#. **Use ``depart`` consistently** where there is genuine after-children work
   (only ``ComponentImplementation`` uses it today). A predictable visit/depart
   rhythm is easier to scan than ad-hoc ``_render_*`` helpers.


Summary
-------

* The visitor base gives you typed dispatch, phases, and ``dispatch_on`` — a
  small but powerful engine.
* The four helpers already isolate **traversal, naming, reference-resolution and
  strategy**; they keep every file small and single-purpose.
* The remaining large surface is the **rendering** itself. Splitting it along the
  AIGR sub-packages (Expr / Literal / Statement / Structure) is the natural next
  step, ideally backed by a **registry** and a **coverage map**.
