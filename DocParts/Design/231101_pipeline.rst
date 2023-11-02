.. -*- plantuml -*-

AIGR pipeline
=============

.. uml::

   @startuml
   skin rose

    () "files" as txt1

    file "*.Castle" as f1
    f1 --> txt1
    file "*.Moat"   as f2
    f2 --> txt1

   package CC{
   txt1 -> CC 

    () "AIGR"	as a1
    () "AIGR"	as a2

     [Readers]
     CC #-> Readers
     [Transformers]
     Folder Backend {
       [Writers]
       [Translators]

       Backend #->Writers

       () "files" as txt2
       Writers  -(  txt2
       txt2        )-> Translators
    }



     Readers       -(  a1
     a1             )->  Transformers
     Transformers  -(   a2
     a2             )->  Backend
   }

   Translators 0)-> bin

   @enduml

