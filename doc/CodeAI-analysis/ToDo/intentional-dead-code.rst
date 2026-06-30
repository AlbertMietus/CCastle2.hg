.. (C) Albert Mietus, 2026. CodeAI=GH.Claude.Sonnet-4.6

Intentional Dead Code
=====================

This document lists code that static analysis tools (e.g. vulture) flag as dead or unreachable,
but that is **intentionally present** — either as inline documentation, as reference code during
active development, or as a placeholder for work still in progress.

These are **not bugs**. Do not remove without understanding the intent.

.. contents:: Contents
   :local:
   :depth: 2

``if False`` blocks — Inline documentation
-------------------------------------------

**File:** ``base_packages/castle-aigr/castle/aigr_extra/builders/build_expr.py``

Two ``if False:`` blocks appear near the top of the module. These are **intentional documentation**:
they show the step-by-step derivation of the lambda-based meta-builder pattern used in the module,
written as syntactically valid (and syntax-highlighted) Python rather than prose or comments.

The ``# pragma: no cover`` and ``# pragma: no mutate`` markers confirm this is deliberate.
Static analysis tools correctly identify these as unsatisfiable conditions — that is the point.

**Status:** Correct as-is. Do not remove or refactor.

Unreachable code after ``raise NotImplementedError`` — Work in progress
------------------------------------------------------------------------

**File:** ``core_packages/castle-RPy-writer/castle/writers/RPy/writer/machinery/chained_dict_DCM.py``
**Location:** method ``render_EventToSub`` (around line 40)

The method raises ``NotImplementedError`` immediately, leaving the remainder of the method body
unreachable. The dead code below the ``raise`` is **reference/scaffolding material**: it contains
the AIGR node signature and notes about what the implementation should produce, kept inline
for easy reference during future implementation work.

.. code-block:: python

   def render_EventToSub(self, renderer, node) -> Block:
       raise NotImplementedError          # ← not yet implemented
       node = PTH.cast(...)               # ← reference code; kept for context
       logger.info(f"XXX ...")
       # ... AIGR node signature as reminder ...

**Status:** Work in progress. To be implemented. The dead code below the ``raise`` serves as
an implementation note and should be removed once the method is written.

``if True`` guard — Partial implementation marker
--------------------------------------------------

**File:** ``core_packages/castle-RPy-writer/castle/writers/RPy/writer/renderer.py``
**Location:** method ``_DispatchTables`` (around line 132)

An ``if True:`` block wraps an assertion that checks only ``EventHandler`` nodes are present.
The comment reads *"partial implementation: check that we have ONLY event-handlers"*.
This guard is a **deliberate placeholder**: the ``if True:`` makes the partial-implementation
scope visually explicit and easy to locate, while keeping the assertion active during development.

.. code-block:: python

   def _DispatchTables(self, node) -> TextBlock:
       txt = Block()
       txt += self._EventDispatchTables(node)
       if True:  # partial implementation: check that we have ONLY event-handlers
           for h in node.handlers:
               assert isinstance(h, aigr.EventHandler), ...
       return txt

**Status:** Work in progress. The ``if True:`` scope should be replaced by a full implementation
that handles other handler types as well.

.. note::

   See also ``readers-support-Stack.rst`` for a case of dead code that is **not** intentional.
