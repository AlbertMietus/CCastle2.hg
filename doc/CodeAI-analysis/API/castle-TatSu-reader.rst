.. (C) Albert Mietus, 2026. CodeAI=GH.Claude.Opus-4.8

castle-TatSu-reader
===================

The **Ladon** reader is the front-end of the CCastle compiler: it parses
``.Castle`` and ``.Moat`` source files using a `TatSu`_ PEG grammar and
produces an :doc:`castle-aigr` in-memory tree that writers (e.g. the RPy writer)
consume.  It depends on ``castle-aigr`` for the node types it constructs.
The name *Ladon* is the mythical Greek dragon guarding the golden apples; it
was chosen because TatSu means "dragon" in Japanese and the reader is the
gateway to the Castle compilation pipeline.

.. _TatSu: https://pypi.org/project/TatSu/

.. contents:: On this page
   :local:
   :depth: 1

At a glance
-----------

==========================  ====================================================
Package                     ``castle-TatSu-reader`` (version 0.0.1)
Depends on                  ``castle-aigr``
Import root                 ``castle.readers`` (subpackages ``castle.readers.ladon``, ``castle.readers.support``)
Main entry point            :class:`~castle.readers.ladon.loaders.SimpleFileLoader` (or :class:`~castle.readers.ladon.loaders.simple_loader.PyModuleLoader` for package-data files)
Parser                      :class:`~castle.readers.ladon.parser.castle_parser.CastleParser` (TatSu 5.17; see note on version)
Actions object              :class:`~castle.readers.ladon.parser.castle_actions.CastleActions` (created automatically)
AIGR bridge                 :class:`~castle.readers.ladon.aigr.inputs.FileNS` + :class:`~castle.readers.ladon.aigr.inputs.ScaffolderFileNS`
Support                     :class:`~castle.readers.support.stack.Stack` (LIFO utility; known import bug -- see `support`_)
==========================  ====================================================

Quickest import::

    from castle.readers.ladon.loaders import SimpleFileLoader

----

Loading Castle source
---------------------

*Modules:* ``castle.readers.ladon.loaders.simple_loader``,
``castle.readers.ladon.loaders._base_loader``
(`simple_loader.py <../../../core_packages/castle-TatSu-reader/castle/readers/ladon/loaders/simple_loader.py>`_,
`_base_loader.py <../../../core_packages/castle-TatSu-reader/castle/readers/ladon/loaders/_base_loader.py>`_)

The loaders are the **only public entry points** you need for normal use.
They own a :class:`~castle.readers.ladon.parser.CastleParser` instance, open
the source, call TatSu, and wrap the result in a
:class:`~castle.aigr.Source_NS`.

``_BaseLoader`` and ``_FileLoader`` are internal base classes; use the two
concrete subclasses:

* :class:`~.simple_loader.SimpleFileLoader` -- takes a
  :class:`~pathlib.Path` to a local file.
* :class:`~.simple_loader.PyModuleLoader` -- resolves a filename relative to
  the on-disk directory of an installed Python package (useful for Castle
  source shipped as package data).

The ``CastleKind`` enum (in ``_base_loader``) controls which TatSu start
symbol is used.  The default is ``CastleKind.auto``, which infers the symbol
from the file suffix (``.Castle`` -> ``castle_file``, ``.Moat`` ->
``moat_file``).

How to use it
~~~~~~~~~~~~~

.. code-block:: python

    from castle.readers.ladon.loaders import SimpleFileLoader
    from pathlib import Path

    # Parse a local .Castle file; start symbol inferred from suffix.
    loader    = SimpleFileLoader(Path("src/MyComponent.Castle"))
    source_ns = loader.parse()              # -> castle.aigr.Source_NS
    print(source_ns.name)                   # e.g. "MyComponent"

    # Override the AIGR name (useful for test fixtures with unusual paths):
    source_ns = loader.parse(name="MyComponent")

    # Parse a Castle file shipped inside an installed Python package:
    from castle.readers.ladon.loaders.simple_loader import PyModuleLoader

    loader2    = PyModuleLoader("my_castle_pkg", "protocols/Clocks.Castle")
    source_ns2 = loader2.parse()            # -> castle.aigr.Source_NS

Key public signatures
~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    from enum import Enum

    class CastleKind(Enum):
        auto    = None       # infer from file suffix (default)
        Moat    = ".Moat"    # force moat_file start symbol
        Castle  = ".Castle"  # force castle_file start symbol
        unknown = ...        # sentinel for unrecognised suffix

    class SimpleFileLoader(_FileLoader):
        def __init__(self, file: Path | None, **kw) -> None: ...
        def parse(self, *, name: str | None = ...,
                  _startsymbol: str | None = ..., **kw) -> Source_NS: ...

    class PyModuleLoader(_FileLoader):
        def __init__(self, module: str, file: str, **kw) -> None: ...
        # inherits parse() from _FileLoader

----

Parser -- grammar and semantic actions
---------------------------------------

*Modules:* ``castle.readers.ladon.parser.castle_parser``,
``castle.readers.ladon.parser.castle_actions``,
``castle.readers.ladon.parser.actions.*``
(`castle_parser.py <../../../core_packages/castle-TatSu-reader/castle/readers/ladon/parser/castle_parser.py>`_,
`castle_actions.py <../../../core_packages/castle-TatSu-reader/castle/readers/ladon/parser/castle_actions.py>`_,
`actions/ <../../../core_packages/castle-TatSu-reader/castle/readers/ladon/parser/actions/>`_)

These modules are **internal machinery**.  You do not need to touch them for
normal use; the loader creates a ``CastleParser`` (and therefore a
``CastleActions``) automatically.  The section below documents the structure
for developers extending or debugging the parser.

``CastleParser``
~~~~~~~~~~~~~~~~

Compiles ``castle_grammar.tatsu`` from its own directory via
``tatsu.parser.TatSuParserGenerator`` and attaches a
:class:`~.castle_actions.CastleActions` semantics object.  The compiled
grammar lives in ``.parser`` (a raw ``tatsu.grammars.Grammar``; TatSu has no
type stubs so this attribute is typed ``Any``).

.. warning::

   TatSu 5.17 is required.  TatSu 5.18 is **broken** for the Castle grammar
   (https://github.com/neogeny/TatSu/issues/423).  A version mismatch logs an
   ``ERROR`` but continues; results may be incorrect.

.. code-block:: python

    from castle.readers.ladon.parser.castle_parser import CastleParser

    # Normally done by a loader -- only do this directly for advanced use:
    parser = CastleParser()
    ast    = parser.parse(castle_source_string, start="castle_file")
    # ast is the FileNS produced by CastleActions.castle_file(...)

``CastleActions`` and the action mixins
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:class:`~.castle_actions.CastleActions` is a single composite class that
inherits from eight action-mixin classes, one per grammar rule group:

====================  ========================================================
Mixin                 Grammar rules handled
====================  ========================================================
``Names``             ``nameID``, ``nameRef``, ``typeID``, ``auto_self``, ``qualRef``
``ParmsArgs``         ``typedParameter(Tuple)``, ``argument(Tuple)``, ``literal_ID``, ``modifiers``
``Protocols``         ``event_definition``, ``event_protocol``
``Components``        ``component_definition``, ``implement_component``, ``port_line``, ``port_direction``, ``event_handler``, ``method``
``Meta``              rewriter/meta rules (placeholder; no active actions)
``Literals``          ``lit_string``
``Files``             ``castle_file`` (and ``_old`` legacy path)
``Body``              ``body``, ``stat_voidcall``
====================  ========================================================

Each mixin is decorated with ``@add_debug_logging`` (from
``actions._debug``), which wraps every method to emit ``DEBUG`` log lines of
the form ``ClassName.method::  ast=... ==> retval=...``.  Enable debug
logging on the ``castle.readers.ladon.parser.actions`` logger to see every
TatSu reduction.

.. code-block:: python

    import logging
    logging.getLogger("castle.readers.ladon.parser.actions").setLevel(logging.DEBUG)

----

AIGR bridge -- ``ladon.aigr.inputs``
--------------------------------------

*Module:* ``castle.readers.ladon.aigr.inputs``
(`inputs.py <../../../core_packages/castle-TatSu-reader/castle/readers/ladon/aigr/inputs.py>`_)

This small bridge module introduces two AIGR extensions that are only needed
inside the reader:

* :class:`~.aigr.inputs.FileNS` -- a temporary, nameless
  :class:`~castle.aigr.namespaces._NameSpace` that the ``Files`` grammar
  action fills with every top-level node found in one source file.  Its
  ``name`` class attribute is the sentinel ``"TEMP"`` because the real name
  (the file stem) is not known until ``_BaseLoader._make_Source_NS`` wraps it
  in a :class:`~castle.aigr.Source_NS`.

* :class:`~.aigr.inputs.ScaffolderFileNS` -- a
  :class:`~castle.aigr.tools.scaffolding.ScaffolderNameSpace` specialisation
  whose ``__iter__`` yields each value stored in the ``_ns`` dict of a
  ``FileNS``.  Used internally by ``_BaseLoader._make_Source_NS`` to transfer
  nodes from the temporary namespace into the final ``Source_NS``.

Callers never instantiate these directly.  They are created inside the
grammar actions (``Files.castle_file``) and consumed immediately by the
loader.

.. code-block:: python

    # Internal flow (shown for documentation purposes only):
    from castle.readers.ladon.aigr.inputs import FileNS, ScaffolderFileNS

    file_ns = FileNS()                      # created by Files.castle_file(ast)
    scaffolder = ScaffolderFileNS(file_ns)
    for node in scaffolder:                  # yields each registered AIGR node
        source_ns_wrapper.register(node)    # transfers to Source_NS

Key public signatures
~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    from dataclasses import dataclass
    from castle.aigr.namespaces import _NameSpace
    from castle.aigr.tools.scaffolding import ScaffolderNameSpace

    @dataclass
    class FileNS(_NameSpace):
        name: ClassVar[str]        # == "TEMP"

    class ScaffolderFileNS(ScaffolderNameSpace):
        _nodeCls: type             # == FileNS
        def __iter__(self) -> Iterator[Any]: ...

----

support -- ``castle.readers.support``
--------------------------------------

*Module:* ``castle.readers.support.stack``
(`stack.py <../../../core_packages/castle-TatSu-reader/castle/readers/support/stack.py>`_)

The ``support`` subpackage currently contains one utility:
:class:`~castle.readers.support.stack.Stack`, a generic LIFO stack.

.. error::

   **Known bug in** ``castle/readers/support/__init__.py``

   The ``__init__.py`` does::

       from .support import Stack   # WRONG -- module is named stack.py

   This causes a ``ModuleNotFoundError`` at import time whenever
   ``castle.readers.support`` is imported.  The bug is currently harmless
   because ``Stack`` is not yet used anywhere in production code, but it means
   you **must** import ``Stack`` directly from the implementation module::

       from castle.readers.support.stack import Stack   # correct

   The bug is tracked and documented in
   ``doc/CodeAI-analysis/ToDo/readers-support-Stack.rst``.  mypy reports it as
   a ``[import-not-found]`` error on that ``__init__.py``.

How to use it
~~~~~~~~~~~~~

.. code-block:: python

    from castle.readers.support.stack import Stack   # direct import (see bug note)

    stack: Stack[str] = Stack()
    stack.push("alpha")
    stack.push("beta")
    top = stack.peek()            # "beta" -- does not remove
    val = stack.pop()             # "beta" -- removes it
    assert stack.size() == 1      # or: len(stack) == 1
    assert not stack.is_empty()

Key public signatures
~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    class Stack(Generic[T]):
        def push(self, item: T) -> None: ...
        def pop(self) -> T: ...            # raises IndexError if empty
        def peek(self) -> T: ...           # raises IndexError if empty
        def is_empty(self) -> bool: ...
        def size(self) -> int: ...
        def __len__(self) -> int: ...      # alias for size()
