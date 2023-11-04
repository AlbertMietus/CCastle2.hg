.. -*- plantuml -*-

=============
AIGR pipeline
=============

Overview
========

.. uml::

   @startuml
   skin rose
   !include ../../DocParts/skins.inc

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

The Reader(s)
=============

.. uml::

   @startuml
   skin rose
   !include ../../DocParts/skins.inc

   frame "CC” #c0c0c0 {
    package Readers #white {
     'portout AIGR
     'portin TXT

     node Reader {
        [parser]
        [analyse\n(ast)] as ast_ana
        [AST 2 AIGR] as AST2AIGR
        () "AIGR"	as aigr1
        [analyse\n(aigr)] as aigr_ana
        () "AIGR"	as aigr2

        parser    -> ast_ana  : AST
        ast_ana   -> AST2AIGR : AST
        AST2AIGR  -> aigr1
        aigr1     -> aigr_ana
        aigr_ana  -( aigr2
     }

     TXT -> Reader
     node mock {
        [py_data]
        () "AIGR" as aigr3

        py_data   -(  aigr3
     }
     Reader -[hidden]down-> mock
    }
   }

   @enduml

