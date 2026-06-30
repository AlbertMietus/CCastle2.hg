.. (C) Albert Mietus, 2026. CodeAI=GH.Claude.Opus-4.8

TestDoubles (AIGR fixtures)
===========================

The **TestDoubles** packages supply hand-crafted, known-good
*Abstract Intermediate Graph Representation* (AIGR) structures.
They are stable fixtures: tests import them as ready-made inputs (for
writers, transformers, or visitors) or as expected outputs (for readers).
Every fixture is a pure collection of live AIGR dataclass instances built at
import time; no parser is involved.  All three packages depend on
``castle-aigr``.

.. contents::
   :local:
   :depth: 1

At a glance
-----------

============================================  =======  ==================================================  =========================================================
Package                                       Version  Depends on                                          Import root
============================================  =======  ==================================================  =========================================================
``castle-TestDoubles-aigr-base``              0.0.2    ``castle-aigr``                                     ``castle.TESTDOUBLES.aigr.base``
``castle-TestDoubles-aigr-sieve``             0.0.2    ``castle-aigr``, ``castle-TestDoubles-aigr-base``   ``castle.TESTDOUBLES.aigr.sieve``
``castle-TestDoubles-HelloWorlds``            0.0.2    ``castle-aigr``                                     ``castle.TESTDOUBLES.aigr.HelloWorlds``
============================================  =======  ==================================================  =========================================================

----

TestDoubles-aigr-base
---------------------

*Package:* ``castle-TestDoubles-aigr-base``
(`__init__.py <../../../TestDoubles_packages/TestDoubles-aigr-base/castle/TESTDOUBLES/aigr/base/__init__.py>`_)

This package is the **foundation** TestDouble.  It exists so downstream
TestDouble packages can share a single known import point for core AIGR types
(``ID``, ``NamedSpace``, ``ScaffolderNameSpace``).  In the current version all
concrete fixture building (``base`` namespace, ``baseProtocol``) is commented
out; the package is therefore a thin re-export shim.

Key public names
~~~~~~~~~~~~~~~~

================================  ============================================================
Name                              Origin / what it is
================================  ============================================================
``ID``                            Re-exported from ``castle.aigr.protocols``; the AIGR name class
``NamedSpace``                    Re-exported from ``castle.aigr``; base namespace class
``ScaffolderNameSpace``           Re-exported from ``castle.aigr.tools.scaffolding``; behaviour wrapper
================================  ============================================================

How to use it
~~~~~~~~~~~~~

Because the base package re-exports these types you can use it as a single
import in a test that needs only the building-blocks:

.. code-block:: python

    from castle.TESTDOUBLES.aigr.base import ID, NamedSpace
    from castle import aigr

    def test_id_round_trip():
        name = ID("Foo")
        assert str(name) == "Foo"
        assert isinstance(name, aigr.ID)

----

TestDoubles-aigr-sieve
----------------------

*Package:* ``castle-TestDoubles-aigr-sieve``
*Sub-package:* ``castle.TESTDOUBLES.aigr.sieve.basic1``
(`components.py <../../../TestDoubles_packages/TestDoubles-aigr-sieve/castle/TESTDOUBLES/aigr/sieve/basic1/components.py>`_,
`namespaces.py <../../../TestDoubles_packages/TestDoubles-aigr-sieve/castle/TESTDOUBLES/aigr/sieve/basic1/namespaces.py>`_,
`protocols.py <../../../TestDoubles_packages/TestDoubles-aigr-sieve/castle/TESTDOUBLES/aigr/sieve/basic1/protocols.py>`_,
`sieveCastle.py <../../../TestDoubles_packages/TestDoubles-aigr-sieve/castle/TESTDOUBLES/aigr/sieve/basic1/sieveCastle.py>`_)

A hand-crafted AIGR fixture that represents the **basic-1 variant of the
Sieve** -- a classic prime-number-sieve program expressed in Castle.  It
does *not* use SlowStart and does *not* address the Heisenbug.

The fixture is split across four modules that mirror the Sieve Castle source
tree:

================================  ============================================================
Module                            What it provides
================================  ============================================================
``protocols``                     ``StartSieve`` and ``SimpleSieve`` ``EventProtocol`` instances
``components``                    ``GeneratorMoat``, ``SieveMoat``, ``FinderMoat`` (``ComponentInterface``)
``namespaces``                    ``Source_NS`` nodes mirroring each Castle file + wired imports
``sieveCastle``                   Full ``ComponentImplementation`` for ``Sieve`` (method + event handler)
================================  ============================================================

How to use it
~~~~~~~~~~~~~

.. code-block:: python

    import pytest
    from castle import aigr
    from castle.aigr.tools.scaffolding import ScaffolderNameSpace
    from castle.aigr_extra.blend import mangle_event_handler
    from castle.TESTDOUBLES.aigr.sieve.basic1 import protocols, components, sieveCastle

    # --- protocol fixtures ---

    def test_protocols_are_event_protocols():
        for p in (protocols.StartSieve, protocols.SimpleSieve):
            assert isinstance(p, aigr.EventProtocol)

    def test_start_sieve_has_two_events():
        p = protocols.StartSieve
        assert len(p.events) == 2
        assert str(p.events[0].name) == "runTo"
        assert str(p.events[1].name) == "newMax"

    # --- component-interface fixtures ---

    def test_sieve_moat_ports():
        g = components.SieveMoat
        assert isinstance(g, aigr.ComponentInterface)
        assert str(g.ports[0].name) == "try"
        assert str(g.ports[1].name) == "coprime"

    # --- component implementation ---

    @pytest.fixture
    def wrapped_sieve():
        return ScaffolderNameSpace(sieveCastle.Sieve)

    def test_sieve_has_init(wrapped_sieve):
        init = wrapped_sieve.findNode('init')
        assert isinstance(init, aigr.Method)

    def test_sieve_has_event_handler(wrapped_sieve):
        eh_name = mangle_event_handler(protocol="SimpleSieve",
                                       event="input", port="try")
        eh = wrapped_sieve.findNode(eh_name)
        assert isinstance(eh, aigr.EventHandler)

----

TestDoubles-HelloWorlds
-----------------------

*Package:* ``castle-TestDoubles-HelloWorlds``
(`elemental/HelloWorld.py <../../../TestDoubles_packages/TestDoubles-HelloWorlds/castle/TESTDOUBLES/aigr/HelloWorlds/elemental/HelloWorld.py>`_,
`credible/HelloWorld.py <../../../TestDoubles_packages/TestDoubles-HelloWorlds/castle/TESTDOUBLES/aigr/HelloWorlds/credible/HelloWorld.py>`_)

Two increasingly rich AIGR fixtures for Hello-World Castle programs.  They
are intended as **canonical smoke-test inputs** for any writer (e.g. the RPy
writer) or AIGR-consuming pass: if your code cannot handle
``elemental.HelloWorld``, it certainly cannot handle more complex programs.

========================  ================================================================
Sub-module                What it provides
========================  ================================================================
``elemental.HelloWorld``  Minimal program: one implicit component, one method, one event handler
``credible.HelloWorld``   Richer program: explicit protocol, named component with port, sub-component, initializer
========================  ================================================================

elemental variant
~~~~~~~~~~~~~~~~~

The elemental HelloWorld is the simplest self-contained AIGR.  It has:

* ``Hello_World`` -- top-level ``Source_NS`` (represents ``HelloWorld.Castle``)
* ``Elemental_HelloWorld`` -- ``ComponentImplementation`` (no ports)
* ``HelloWorld`` -- a ``Method(label:str)`` that calls ``print``
* ``invoke`` -- an ``EventHandler`` on ``std.invoke`` that calls ``HelloWorld``

credible variant
~~~~~~~~~~~~~~~~

The credible HelloWorld adds:

* ``SetLabel`` -- an ``EventProtocol`` with a ``set(label:str)`` event
* ``component_Credible`` / ``Credible`` -- a component with an input port ``hello:SetLabel``
* ``Credible_HelloWorld`` -- outer ``@impliciet(Main)`` implementation that holds a ``sub_credible`` field, an ``init`` initializer, and an ``invoke`` event handler routing through ``EventToSub``

How to use it
~~~~~~~~~~~~~

.. code-block:: python

    import pytest
    from castle import aigr
    from castle.aigr.tools.scaffolding import ScaffolderNameSpace

    # --- elemental ---
    from castle.TESTDOUBLES.aigr.HelloWorlds.elemental import HelloWorld as ehw

    def test_elemental_ns_is_source_ns():
        assert isinstance(ehw.Hello_World, aigr.Source_NS)

    def test_elemental_component_registered():
        comp = ScaffolderNameSpace(ehw.Hello_World).findNode('Elemental_HelloWorld')
        assert isinstance(comp, aigr.ComponentImplementation)

    def test_elemental_method_has_label_param():
        method = ScaffolderNameSpace(ehw.Elemental_HelloWorld).findNode('HelloWorld')
        assert isinstance(method, aigr.Method)
        param = ScaffolderNameSpace(method).findNode('label')
        assert param is not None

    # --- credible ---
    from castle.TESTDOUBLES.aigr.HelloWorlds.credible import HelloWorld as chw

    def test_credible_protocol():
        assert isinstance(chw.SetLabel, aigr.EventProtocol)
        assert str(chw.SetLabel.events[0].name) == "set"

    def test_credible_component_has_hello_port():
        iface = chw.component_Credible
        assert isinstance(iface, aigr.ComponentInterface)
        # port[0] is a Ref wrapping p_hello (SetLabel<in>:hello)
        assert str(iface.ports[0]) == "hello"

    def test_credible_init_becomes_sub():
        init = ScaffolderNameSpace(chw.Credible_HelloWorld).findNode('init')
        assert isinstance(init, aigr.Initializer)
        from castle.aigr.tools.scaffolding import ScaffolderBody
        stmt = ScaffolderBody(init.body)[0]
        assert isinstance(stmt, aigr.Become)
