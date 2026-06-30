# (C) Albert Mietus, 2026. CodeAI=GH.Claude.Opus-4.8
#
# Type stub for ``castle.TESTDOUBLES.aigr.sieve.basic1.protocols``.
#
# This module is a hand-crafted AIGR fixture that represents the two Castle
# protocols used by the Sieve example: ``StartSieve`` (control protocol with
# two events) and ``SimpleSieve`` (data protocol with one event).
#
# Typical test usage::
#
#   from castle.TESTDOUBLES.aigr.sieve.basic1 import protocols as sieve_protocols
#   from castle import aigr
#
#   def test_protocols_exist():
#       assert isinstance(sieve_protocols.StartSieve, aigr.EventProtocol)
#       assert isinstance(sieve_protocols.SimpleSieve, aigr.EventProtocol)
#
#   def test_input_event():
#       e = sieve_protocols.SimpleSieve.events[0]
#       assert str(e.name) == "input"

import typing as PTH

from castle.aigr import EventProtocol, Event

StartSieve: EventProtocol
"""AIGR fixture for the ``StartSieve`` EventProtocol.

Represents::

    protocol StartSieve : EventProtocol {
        runTo(int:max);
        newMax(int:max);
    }

Events (by index):
  * ``events[0]`` -- ``runTo(max: int)``
  * ``events[1]`` -- ``newMax(max: int)``
"""

input_event: Event
"""The single ``input(try: int)`` event of ``SimpleSieve``.

Exposed at module level so tests can reference it directly without indexing
into ``SimpleSieve.events``."""

SimpleSieve: EventProtocol
"""AIGR fixture for the ``SimpleSieve`` EventProtocol.

Represents::

    protocol SimpleSieve : EventProtocol {
        input(int:try);
    }

Events (by index):
  * ``events[0]`` -- ``input(try: int)``  (same object as ``input_event``)
"""
