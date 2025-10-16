Visitors (in RPy)
===================

Renderer (castle.writers.RPy.writer.renderer)
----------------------------------------------

:returns: -> TextBlock:= PTH.Optional[str|Block]

* visit_Body
* visit_Call
* visit_ComponentImplementation
* depart_ComponentImplementation
* visit_ComponentInterface
* visit_EventHandler
* visit_ID				 # GAM: Nog niet overal gebruikt (bijna niet)
* visit_Method
* visit_RPy_unit
* visit_VoidCall
* visit__literal
* visit_fString

Busy:
*  visit_Initializer
*  visit_Become

  Walker (castle.writers.RPy.writer.walker)
-----------------------------------------

:returns: -> PTH.Sequence[aigr.AIGR]

* visit_Body
* visit_Call
* visit_ComponentImplementation
* visit_VoidCall
* visit__NameSpace
* visit__Named_callable
* visit_fString
