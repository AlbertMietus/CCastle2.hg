.. (C) Albert Mietus, 2026. CodeAI=GH.Claude.Opus-4.8

CCastle API reference (usage-oriented)
======================================

This section documents **how to use** each CCastle package and its public
classes -- the *interface*, not the implementation. It is generated from the
code and comes in two parallel forms, one per audience:

==================  ====================  =================================================
Audience            Format                Where
==================  ====================  =================================================
Humans              ``.rst`` (this tree)  ``doc/CodeAI-analysis/API/<package>.rst``
Tools / CodeAI      ``.pyi`` stubs        *inline*, next to every ``.py`` module
==================  ====================  =================================================

The ``.rst`` pages are a *manual* form of ``autodoc``: hand-written, readable,
focused on usage examples and the public signatures, with a link to the backing
``.py`` (and its ``.pyi``).

The ``.pyi`` stubs carry the **signatures** plus a concise usage docstring for
each public class/function. They live beside the modules so that ``mypy`` and
``pyright`` consume them automatically (every package already ships a
``py.typed`` marker and declares ``*.pyi`` in ``package-data``), and so future
CodeAI actions get an accurate, low-noise view of each API.

.. note::

   **Trade-off of inline stubs.** When a ``module.pyi`` sits next to
   ``module.py``, type checkers use the *stub* as the authoritative interface
   and stop type-checking that module's *implementation*. That is intentional
   here (the API is the contract), but it means a stub must stay in sync with
   the code and must expose every name -- including the *protected extension
   points* that subclasses call (e.g. ``Visitor._visitor``).

Scope
-----

Documented: the active, installable packages only. The ``ARCHIVED/`` and
``ASIDE/`` trees are deliberately **excluded** -- they are archived/dead code,
so "how to use" docs for them would be misleading.

Packages
--------

.. toctree::
   :maxdepth: 2

   castle-monorail
   castle-aigr
   castle-aigr-trawlers
   castle-TatSu-reader
   castle-RPy-writer
   testdoubles
