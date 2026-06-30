# (C) Albert Mietus, 2026. CodeAI=GH.Claude.Opus-4.8
#
# Type stub for ``castle.TESTDOUBLES.aigr.sieve.basic1.sieveCastle``.
#
# Provides the full ``ComponentImplementation`` AIGR fixture for the Sieve
# component: its ``myPrime`` variable, the ``init`` method, and the
# ``SimpleSieve.input`` event handler.
#
# Typical test usage::
#
#   from castle.TESTDOUBLES.aigr.sieve.basic1 import sieveCastle
#   from castle.aigr.tools.scaffolding import ScaffolderNameSpace
#   from castle import aigr
#
#   def test_sieve_component():
#       assert isinstance(sieveCastle.Sieve, aigr.ComponentImplementation)
#       wrapped = ScaffolderNameSpace(sieveCastle.Sieve)
#       init = wrapped.findNode('init')
#       assert isinstance(init, aigr.Method)
#
# NOTE: mypy reports 3 pre-existing arg-type errors in this module (Ref type
# mismatch and arguments tuple); the stubs reflect the interface as built.

import typing as PTH

from castle.aigr import ComponentImplementation, Method, EventHandler, VariableDefintion
from castle.aigr.tools.scaffolding import ScaffolderNameSpace

__all__: list[str]

Sieve: ComponentImplementation
"""AIGR fixture for the ``Sieve`` component implementation.

Represents::

    implement Sieve {
        int myPrime;
        init(int:onPrime) { super.init(); .myPrime := onPrime; }
        SimpleSieve.input(try) on .try {
            if ( (try % .myPrime) != 0 ) { .coprime.input(try); }
        }
    }

Use ``ScaffolderNameSpace(sieveCastle.Sieve).findNode(name)`` to look up
``'init'`` (a ``Method``) or the mangled event-handler name (an
``EventHandler``).  The interface is ``components.SieveMoat``."""

wrapped_Sieve: ScaffolderNameSpace
"""``ScaffolderNameSpace`` wrapper around ``Sieve``; used internally to
register ``myPrime``, ``init_method``, and ``event_handler_1``."""

myPrime: VariableDefintion
"""AIGR node for ``int myPrime`` -- the per-instance prime-number field."""

init_method: Method
"""AIGR fixture for the ``init(int:onPrime)`` constructor method.

Body has exactly two statements:
  1. ``super.init()``       -- ``VoidCall(Call(Part(Call('super'), 'init')))``
  2. ``.myPrime := onPrime`` -- ``Become``"""

event_handler_1: EventHandler
"""AIGR fixture for the ``SimpleSieve.input`` event handler on port ``try``.

Body: a single ``If`` whose test is ``(try % myPrime) != 0`` and whose
then-branch fires ``EventOverPort`` on the ``coprime`` output port."""
