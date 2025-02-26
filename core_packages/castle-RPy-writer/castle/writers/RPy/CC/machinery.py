"""**The Machinery** is the concept & implementation detail on component's *talk* to each-other

When compiling, the machinery can set chosen/set (as compiler-flag). Conceptually, it act as a plug-in; such that more
variants can be add. The early compilers will/may have a limited set (without plug-ins).
|BR|
To make sure, we have a generic interface, we should implementat some ...


Note: eventually, we could have multiple machinery's actief. Where each *component* has one set, to be used by all
**sub-components** inside, but itself uses another to talk to other components within the **super-component**

.. see also:: http://docideas.mietus.nl/en/default/CCastle/3.Design/zz.todo.html#the-machinery-todo
"""

DirectCall  = "Machinery.DirectCall"
LibDispatch = "Machinery.LibDispatch"
DDS         = "Machinery.DDS-Study"

Machinery = DirectCall
