analyse_imports (220122)
========================

.. UML::

  @startuml
  skinparam  ArrowColor green

  skinparam component {
    BackgroundColor #0077ff
    BorderColor black
  }
  skinparam folder {
    BackgroundColor lightblue
    BorderColor black
  }

  cloud "AsIS 2022/Jan/22" #pink {

  folder AST {
    folder castle {
     [peg] --> [_base]
     [_base]
     [~__init __]
     }
    }

  folder Arpeggio {
    [grammar]
    [vistor] --> [peg]
    }

  }
  @enduml
