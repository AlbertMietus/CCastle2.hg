AIGR:: ComponentInterface and Protocols (231005)
================================================

.. uml::

   @startuml

   abstract AIGR
   class CompomnentInterface
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

   AIGR <-- Protocol
   AIGR <-- Event
   AIGR <-- CompomnentInterface

   CompomnentInterface <--- CompomnentInterface: based_on
   CompomnentInterface *-- "*" Port


   Protocol <--- Protocol: based_on
   Protocol <--  EventProtocol
   Protocol <--  ProtocolWrapper


   ProtocolWrapper *- "+"Argument

   EventProtocol *--  "*"  Event: events
   Event         *-- "*"   TypedParameters : typedParameters
   Event         o- "?"    Type: returns

   Port o--- Protocol: type


   package ToDesign  <<Rectangle>> #gray {
   class Compomnent
   class CompomnentImplementation
   Compomnent *- CompomnentInterface
   Compomnent *- CompomnentImplementation

   }

   package ToDo/Later  <<Rectangle>> #gray {
     Protocol <-  DataProtocol
     Protocol <--  StreamProtocol

   }
   @enduml
            
