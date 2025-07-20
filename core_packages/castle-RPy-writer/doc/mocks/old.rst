OLD: mocks doc
==============
stats: OLD

.. tabs::

   .. tab:: UML

      .. uml::

         @startuml
         skinparam  classBackgroundColor lightBlue


         entity mockProtocol <<EventProtocol>> {
            ID = MockProtocol
            events = [
                \tMockEvent_1,
                \tMockEvent_2,
            ]
         }

         entity mockPort <<Port>> {
            ID        \t= MockPort
            direction \t= In
            type      \t= mockProtocol
         }
         mockProtocol <- mockPort::type

         entity "mockComp" as visible <<ComponentInterface >> {
            ID     \t= MockComp
            ports \t= [ mockPort ]
         }
         mockPort <- visible::ports

         entity "mockComp" as intern <<ComponentImplementation >> #lightgray {
            ID        \t= MockComp
            interface \t= mockComp
         }
         visible <- intern::interface
       @enduml

   .. tab:: Mocks

      .. literalinclude:: _2code/mocks.py
         :language: Python
         :lines: 10-
         :emphasize-lines: 9, 13, 17


