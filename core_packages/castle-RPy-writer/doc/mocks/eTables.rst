Event Dispatch Tables
=====================
:date: 20 Jul 2025

Stub Protocols
---------------
The following two (Stub)Protocols are used in the code below. Both hold a few *dummyEvents* - in total 3.

.. tabs::

  .. tab:: StubProtocol

     .. literalinclude:: ./demo.Castle
        :language:  ReasonML
        :lines: 1-4

  .. tab:: SubStubProtocol

     .. literalinclude:: ./demo.Castle
        :language:  ReasonML
        :lines: 6-9


Simple
------
The ‘Simple’ `Component` has only 1 `Port` for an (event) protocol without inheritance. For both events in that
`(Stub)Protocol` an event-handler implemented (which is not specified).

The eTable is simple: 2 entries. And no “parent” (see below).

.. tabs::

  .. tab::  CastleCode

     .. literalinclude:: ./demo.Castle
        :language:  ReasonML
        :lines: 12-20

  .. tab::  eTable (notes)


     ==============================   =============================   =================================================
     Simple::MockPort.eTable                                          Notes
     ==============================   =============================   =================================================
     `.parent:`                       ``None``
     StubProtocol.dummyEvent_1        ...
     StubProtocol.dummyEvent_2        ...
     ==============================   =============================   =================================================

Child
-----
The ‘Child’ `Component` is a bit more complicated. It is based on ‘Simple’ and so inherits it ports and protocols -- in
the (shown) *CastleCode* the port is redefined; but that is not needed.
|BR|
Its implementation had (another) event-handler for one of the events.

That one is in the eTable -- overriding the one of Simple. But ‘Child’ will inherits the other one from ‘Simple’. That
one is not in the eTable. But the eTable refers to the eTable of ‘Simple’. (we use .parent here)

.. tabs::

  .. tab::  CastleCode

     .. literalinclude:: ./demo.Castle
        :language:  ReasonML
        :lines: 22-29

  .. tab::  eTable (notes)

     ==============================   =============================   =================================================
     Child::MockPort.eTable                                           Notes
     ==============================   =============================   =================================================
     `.parent:`                       ``Simple::MockPort.eTable``
     StubProtocol.dummyEvent_1        ...                             **Overriding** Simple::StubProtocol.dummyEvent_1
     ==============================   =============================   =================================================

Sub
---
The ‘SubStubProtocol’ --which inherits from `StubProtocol.`; see above-- is used by the (Mock)Port of the ‘Sub’
`Component`. So, the `Component` can handle a few more events as Simple; but no implementations are inherited.

Again, the eTable has (only) entries for the implemented event-handlers. But the table can be “longer” as it can
hold event-handlers for both the inherited and new events.
|BR|
There is no ‘parent’ in the eTable, as no event-handlers are inherited from another Component.

.. tabs::

   .. tab::  CastleCode

      .. literalinclude:: ./demo.Castle
         :language:  ReasonML
         :lines: 31-39

   .. tab::  eTable (notes)

      ==============================   =============================   =================================================
      Sub::MockPort.eTable                                             Notes
      ==============================   =============================   =================================================
      `.parent:`                       ``none``
      StubProtocol.dummyEvent_2        ...                             **Same As**  `SubStubProtocol.dummyEvent_2`
      SubStubProtocol.dummyEvent_3     ...
      ==============================   =============================   =================================================

      .. note::  There is no handler for ``StubProtocol.dummyEvent_1`` (at all)

.. hint::

   Some events (like ``dummyEvent_2``) are known by 2 (or more) names -- both the base-protocol-name and sub-protocol-name
   are allowed as prefix. The dispatch-table will refer to the name as specified in CastleCode. However, those names are
   aliases.

SubChild
--------
Like above, the ‘SubChild` `Component` has one (inherited) (Mock)Port -- now implicit. It can respond to the same
events as `Sub`: the ones of the `StubProtocol` and the “extension” of `SubStubProtocol`.
|BR|
Unlike `Sub`, but alike `Child`, ‘SubChild’ inherits also events-handlers; those of `Sub`.

The eTable will hold only the locally defined event-handler for ‘Event_2`. But refers to the “parent” eTable of `Sub`.,

.. tabs::

  .. tab::  CastleCode

     .. literalinclude:: ./demo.Castle
        :language:  ReasonML
        :lines: 40-47

  .. tab::  eTable (notes)

     ==============================   =============================   =================================================
     SubChild::MockPort.eTable                                        Notes
     ==============================   =============================   =================================================
     `.parent:`                       ``Sub::MockPort.eTable``
     StubSubProtocol.dummyEvent_2     ...
     ==============================   =============================   =================================================

Full
----
The complete code, and the UML-diagrams for the dispatch-tables are shown below

.. tabs::

   .. tab::  CastleCode

      .. literalinclude:: ./demo.Castle
         :language:  ReasonML
   
   .. tab:: UML

      .. uml:: eTables.puml


..  LocalWords:  eTable TestDouble TestDoubles
