.. -*- plantuml -*-

TestDoubles/AIGR: The interfaces of the SIEVE (BUSY)
====================================================

.. uml::

   @startuml

    object "**Sieve**" as Sieve  <<ComponentInterface>> {
    + {static} new(onPrime:int)
    }
    note right of Sieve: alt-name: **SieveMoat**
    object try  <<Port>>{
      In: PortDirection
      SimpleSieve: type
    }
    object corprime <<Port>> {
      Out: PortDirection
      SimpleSieve: type
    }

    Sieve *-- try
    Sieve *-- corprime

    @enduml
