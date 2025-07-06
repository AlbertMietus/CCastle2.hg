writers-mocks.rst
=================

.. tabs::

   .. code-tab:: ReasonML CastleCode

      protocol mockProtocol : EventProtocol {
         MockEvent_1();
         MockEvent_2();
      }

      component MockComp : Component {
         port MockProtocol<in>: MockPort
      }

      implement MockComp
         mockProtocol.MockEvent_1 on .MockPort {
            ....
         }

      }

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


