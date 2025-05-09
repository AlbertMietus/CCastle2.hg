==============
DispatchTables
==============

.. seealso:: DispatchTables in RPy -- that is old and wrong
	     

Event-DispatchTables
====================

Conceptually, an EventDispatchTable is the mapping between an ``Event``, on a specific ``Port``, and the
``EventHandler`` that should be called when that event occurs. As the event-handler (including the name for the
callable in the generated lower-code) is an implementation detail, the DispatchTables itself are also an
implementation detail.

Externally (outside the component-implementation) the DispatchTables are not visable; although a Castle
programmer might be aware that such a mechanism exists.  This is a bit simulair to *vtables* in f.e. C++ -- many
developers "know" it is there, but are not aware of the details. And don't need to know it.

Protocols & inheritance
-----------------------

Both Components and Protocols have (there) own inheritance-graph; and even event-handlers of base components
can be used in sub-components. This implies the DispatchTables will incorprate those graphs; where later/lower
variants overide inherited variants -- like typical in OO.

AIGR & writers
--------------

In the AIGR, every component will have its own mapping, with a "reference" (pointer) to the mappings that are
inherited.

Howevever, that concept will probally be "to slow" for generated ("lower") code. That design is upto the
specific writter, but in general it will be flattended; possible in to a indexed-array (with direct access,
like in C) -- again comparable to the C++ vtable.
|BR|
Although that design in not relevant to de AIGR, it is mentioned to make explicerly clear that aspects isn't
relevant for the AIGR.



