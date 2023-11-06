.. -*- plantuml -*-
.. filename: date of start
.. date in title: last version

AIGR:: ComponentInterface and Protocols (231009)
================================================

.. uml::

   @startuml

   abstract AIGR
   class ComponentInterface
   class Protocol
   class EventProtocol
   class Port {
    - direction :PortDirection
    - type :PortType
   }
   abstract ProtocolWrapper {
    -based_on\n(the Generic Protocol)
   }
   class Argument <<(S,lightgreen)>> {
    +value  :Any
    +name  :Optional[Str]
   }
   class TypedParameters <<(S,lightgreen)>> {
    +name :str
    +type :Type
   }
   class Type <<(T,lightblue)>>
   '--------------------

   ComponentInterface   <---  ComponentInterface: based_on
   Port "*"             -*    ComponentInterface

   Protocol <--- Protocol: based_on
   Protocol <--  EventProtocol
   Protocol <--  ProtocolWrapper

   ProtocolWrapper *- "+"Argument

   EventProtocol *-  "*"  Event: events
   Event         *-- "*"   TypedParameters : typedParameters
   Event         o- "?"    Type: returns

   Port o. Protocol: type

   @enduml

