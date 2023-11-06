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

   object "SlowStart(1)" as SlowStart_1 <<ProtocolWrapper>> {
   queue_max=1
   }
   SlowStart <-- SlowStart_1: based on


   '---

   object SimpleSieve <<EventProtocol>>
   SlowStart_1 <-- SimpleSieve: based_on

   object input <<Event>> {
     try :int
   }
   SimpleSieve *--input

   @enduml
