# (C) Albert Mietus, 2026. CodeAI=GH.Claude.Opus-4.8
#
# Type stub for ``castle.TESTDOUBLES.aigr.HelloWorlds.elemental.HelloWorld``.
#
# Provides the AIGR fixture for the elemental variant of HelloWorld: a minimal
# Castle program with one component implementation, one method, and one event
# handler -- the simplest valid AIGR structure a writer or reader test can
# consume.
#
# Typical test usage::
#
#   from castle.TESTDOUBLES.aigr.HelloWorlds.elemental import HelloWorld as hw
#   from castle.aigr.tools.scaffolding import ScaffolderNameSpace
#   from castle import aigr
#
#   def test_elemental_component_exists():
#       comp = ScaffolderNameSpace(hw.Hello_World).findNode('Elemental_HelloWorld')
#       assert isinstance(comp, aigr.ComponentImplementation)
#
#   def test_method_label_param():
#       method = ScaffolderNameSpace(hw.Elemental_HelloWorld).findNode('HelloWorld')
#       param = ScaffolderNameSpace(method).findNode('label')
#       assert param is not None

import typing as PTH

from castle.aigr import Source_NS, ComponentInterface, ComponentImplementation, Method, EventHandler
from castle.aigr.tools.scaffolding import ScaffolderNameSpace, ScaffolderComponentImplementation

ALL: list[str]
"""Module-level export list; contains ``'Hello_World'``."""

Hello_World: Source_NS
"""Top-level namespace fixture; represents ``elemental/HelloWorld.Castle``.

Contains ``__impliciet_Main_Elemental_HelloWorld`` (ComponentInterface) and
``Elemental_HelloWorld`` (ComponentImplementation) as registered nodes."""

wrapped_HW: ScaffolderNameSpace
"""``ScaffolderNameSpace`` wrapper around ``Hello_World``; used to register
component nodes."""

__impliciet_Main_Elemental_HelloWorld: ComponentInterface
"""Implicit ``@impliciet(Main)`` component interface for ``Elemental_HelloWorld``.

Has no ports (empty interface).  Registered in ``Hello_World`` under its
double-underscore name."""

Elemental_HelloWorld: ComponentImplementation
"""AIGR fixture for the ``Elemental_HelloWorld`` component implementation.

Represents::

    @impliciet(Main)
    implement Elemental_HelloWorld {
        HelloWorld(str:label) { print("Hello {label} World") }
        invoke() on self.std { HelloWorld("Elemental") }
    }

``outer_ns`` is ``Hello_World``.  Use
``ScaffolderNameSpace(Elemental_HelloWorld).findNode(name)`` to retrieve
``'HelloWorld'`` (Method) or the mangled invoke handler (EventHandler)."""

wrapped_E_HW: ScaffolderComponentImplementation
"""``ScaffolderComponentImplementation`` wrapper around ``Elemental_HelloWorld``;
used to register ``HelloWorld`` and ``invoke``."""

HelloWorld: Method
"""AIGR fixture for the ``HelloWorld(str:label)`` method.

Body: a single ``VoidCall`` of ``print`` with an ``fString`` argument
``"Hello {label} World"``."""

invoke: EventHandler
"""AIGR fixture for the ``invoke()`` event handler on port ``std``.

Body: a single ``VoidCall`` of ``HelloWorld("Elemental")``."""
