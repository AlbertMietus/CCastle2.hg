=======================
TestDoubles-HelloWorlds
=======================

.. note:: Only on my local laptop, for now

The TestDoubles-package contain some variant of HelloWord as TestDoubles ...

HelloWord variants
==================

elemental
  This is the most elemental CastleCode that prints “HelloWord”. It does not even contain a protocol, and so it does not
  have connected components.

  It should be easy to compile (parse) and only needs an elemental implementaion of the Backend-writer(s)

credible
  This variant has a (one) simple Protocol, and two components. But there is no implementaion ...

  It can be used to verify compiling and code-generation for components, ports etc.

primitive
  The primitive HelloWord is primitive, sic. It has a protocol, connected components (with ports) and an
  implementaion. So it can print HelloWord using components...

  Again, a bit more complex handle.

All variants (will) have a implementaion in Castle (the ‘CastleCode’) and a AIGR respresentation. Other mocks can be
added, like a reference rpython (manual compiled code). And/Or similar for other Backends.

Overview
========

By layer
--------
.. toctree::

   ./CastleCode
   ./aigr

By Variant
-----------

The same code & diagrams can also be variant by variant

.. toctree::
   
   ./xcross-elemental
