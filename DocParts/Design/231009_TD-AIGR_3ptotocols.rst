.. -*- plantuml -*-

TestDoubles/AIGR: The protocols of the Sieve
============================================

.. uml::

   @startuml

   object StartSieve <<EventProtocol>>
   object runTo <<Event>>{
    max: int
   }
   object newMax <<Event>> {
     max: int
   }
   StartSieve *-- runTo
   StartSieve *-- newMax

   '---

   object SlowStart << EventProtocol>>
   object queue_max <<TypedParameter>> {
       :int
    }
   object setMax <<Event>> {
     setMax :int
   }
   SlowStart *-- setMax
   SlowStart *- queue_max

   '---

   object SimpleSieve <<EventProtocol>>
   SlowStart <-- SimpleSieve: based_on

   object input <<Event>> {
     try :int
   }
   SimpleSieve *--input

   @enduml
