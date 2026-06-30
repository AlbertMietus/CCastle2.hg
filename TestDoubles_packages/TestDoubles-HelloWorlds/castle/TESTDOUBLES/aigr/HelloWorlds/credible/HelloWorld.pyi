# (C) Albert Mietus, 2026. CodeAI=GH.Claude.Opus-4.8
#
# Type stub for ``castle.TESTDOUBLES.aigr.HelloWorlds.credible.HelloWorld``.
#
# Provides the AIGR fixture for the credible variant of HelloWorld: a more
# complete Castle program that adds a typed ``SetLabel`` protocol, a named
# ``Credible`` component with an input port, an internal sub-component, an
# initializer, and an event handler that routes through the sub-component.
#
# Typical test usage::
#
#   from castle.TESTDOUBLES.aigr.HelloWorlds.credible import HelloWorld as hw
#   from castle.aigr.tools.scaffolding import ScaffolderNameSpace
#   from castle import aigr
#
#   def test_credible_protocol():
#       assert isinstance(hw.SetLabel, aigr.EventProtocol)
#       assert str(hw.SetLabel.events[0].name) == "set"
#
#   def test_credible_component():
#       comp = ScaffolderNameSpace(hw.Hello_World).findNode('Credible')
#       assert isinstance(comp, aigr.ComponentImplementation)
#
# NOTE: mypy reports 3 pre-existing arg-type errors in this module
# (Ref type mismatch and EventToSub argument types); stubs reflect the
# interface as built.

import typing as PTH

from castle.aigr import (
    Source_NS,
    EventProtocol,
    Port,
    ComponentInterface,
    ComponentImplementation,
    Method,
    Initializer,
    EventHandler,
    VariableDefintion,
)
from castle.aigr.tools.scaffolding import ScaffolderNameSpace, ScaffolderComponentImplementation

ALL: list[str]
"""Module-level export list; contains ``'Hello_World'``."""

Hello_World: Source_NS
"""Top-level namespace fixture; represents ``credible/HelloWorld.Castle``.

Registered nodes: ``SetLabel``, ``component_Credible`` (interface),
``Credible`` (implementation), ``__impliciet_Main_Credible_HelloWorld``
(interface), ``Credible_HelloWorld`` (implementation)."""

wrapped_HW: ScaffolderNameSpace
"""``ScaffolderNameSpace`` wrapper around ``Hello_World``."""

SetLabel: EventProtocol
"""AIGR fixture for the ``SetLabel`` EventProtocol.

Represents::

    protocol SetLabel : EventProtocol {
        set(label:str);
    }

Events (by index):
  * ``events[0]`` -- ``set(label: str)``
"""

p_hello: Port
"""AIGR ``Port`` node for the ``hello`` input port of ``component_Credible``.

Direction: In; type: ``SetLabel``."""

component_Credible: ComponentInterface
"""AIGR fixture for the ``Credible`` component interface.

Represents::

    component Credible {
        port SetLabel<in>: hello;
    }

``ports[0]`` is a ``Ref`` wrapping ``p_hello``."""

Credible: ComponentImplementation
"""AIGR fixture for the ``Credible`` component implementation.

Contains: ``HelloWorld`` (Method) and ``set_label`` (EventHandler).
``outer_ns`` is ``Hello_World``."""

wrapped_Credible: ScaffolderComponentImplementation
"""``ScaffolderComponentImplementation`` wrapper around ``Credible``."""

HelloWorld: Method
"""AIGR fixture for the ``HelloWorld(str:label)`` method inside ``Credible``.

Body: ``print(fString("Hello {label} World"))``."""

set_label: EventHandler
"""AIGR fixture for the ``SetLabel.set`` event handler on port ``hello``.

Body: ``VoidCall(HelloWorld("Elemental"))``."""

__impliciet_Main_Credible_HelloWorld: ComponentInterface
"""Implicit ``@impliciet(Main)`` component interface for
``Credible_HelloWorld``.  Has no ports."""

Credible_HelloWorld: ComponentImplementation
"""AIGR fixture for the ``Credible_HelloWorld`` top-level implementation.

Contains: ``sub_credible`` (VariableDefintion), ``init`` (Initializer),
and ``invoke`` (EventHandler)."""

wrapped_Credible_HW: ScaffolderComponentImplementation
"""``ScaffolderComponentImplementation`` wrapper around ``Credible_HelloWorld``."""

sub_credible: VariableDefintion
"""AIGR node for the ``credible`` sub-component variable inside
``Credible_HelloWorld``.

Type annotation is ``"aigr.types.XXX.Component"`` (a placeholder string --
the correct component type is not yet resolved in the Castle type system).
Marked with ``# type: ignore[arg-type]`` in the source."""

init: Initializer
"""AIGR fixture for the ``init()`` initializer of ``Credible_HelloWorld``.

Body: ``.credible := Credible()`` -- a single ``Become`` statement."""

invoke: EventHandler
"""AIGR fixture for the ``invoke()`` event handler on port ``std`` inside
``Credible_HelloWorld``.

Body: a single ``EventToSub`` that fires ``SetLabel.set("credible")`` on
``self.hello``."""
