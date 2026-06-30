# (C) Albert Mietus, 2026. CodeAI=GH.Claude.Opus-4.8
#
# Type stub for ``castle.TESTDOUBLES.aigr.sieve.basic1.components``.
#
# Provides three ``ComponentInterface`` AIGR fixtures that match the Sieve
# Castle source (``interfaces.Moat``): Generator, Sieve, and Finder.
#
# Typical test usage::
#
#   from castle.TESTDOUBLES.aigr.sieve.basic1 import components
#   from castle import aigr
#
#   def test_generator_ports():
#       g = components.GeneratorMoat
#       assert isinstance(g, aigr.ComponentInterface)
#       assert str(g.name) == "Generator"
#       assert len(g.ports) == 2
#
# NOTE: mypy reports pre-existing arg-type errors in this module (ports tuple
# vs Sequence[Ref[Port]]); the stubs reflect the interface as built.

import typing as PTH

from castle.aigr import ComponentInterface

__all__: list[str]

GeneratorMoat: ComponentInterface
"""AIGR fixture for the ``Generator`` component interface.

Represents::

    component Generator : Component {
        port StartSieve<in>:controll;
        port SimpleSieve<out>:outlet;
    }

Ports (by index):
  * ``ports[0]`` -- ``controll`` (In,  type=StartSieve)
  * ``ports[1]`` -- ``outlet``   (Out, type=SimpleSieve)
"""

SieveMoat: ComponentInterface
"""AIGR fixture for the ``Sieve`` component interface.

Represents::

    component Sieve(onPrime:int) : Component {
        port SimpleSieve<in>:try;
        port SimpleSieve<out>:coprime;
    }

Ports (by index):
  * ``ports[0]`` -- ``try``     (In,  type=SimpleSieve)
  * ``ports[1]`` -- ``coprime`` (Out, type=SimpleSieve)
"""

FinderMoat: ComponentInterface
"""AIGR fixture for the ``Finder`` component interface.

Represents::

    component Finder : Component {
        port SimpleSieve<in>:newPrime;
        port SimpleSieve<out>:found;
    }

Ports (by index):
  * ``ports[0]`` -- ``newPrime`` (In,  type=SimpleSieve)
  * ``ports[1]`` -- ``found``    (Out, type=SimpleSieve)
"""
