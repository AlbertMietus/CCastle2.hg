Quick Note: Machinery
=====================

**The Machinery** is the concept on HOW component's *talk* to each-other. This has effect on several place where code is generated.

When compiling, the machinery can set chosen/set (as compiler-flag). Conceptually, it act as a plug-in; such that more
variants can be add. The early compilers will/may have a limited set (without plug-ins).

To make sure, we have a generic interface, we should implement some! Some of them are actually sub-sub-machines

In RPY, we focus on 'DirectCall'; with 3 sub variants:

* Both, 'list' & 'tuple' resemble the (old) manual C-code: the (generated) dispatch-tables are an "indexed sequence"
  (either a RPython list ('[]') or a tuple ('()').

  And so, a full table must be generated; including the inherited indexes (events) and empty slots

*  In 'dict', those dispatch-tables are RPython dicts ('{}'); now we only need to generate the relevant entrypoints

   There are some sub-sub-sub options:

   - `flat-dict`    : each table has all entrypoints, including the inherited once (like in C).
   - 'chained-dict` : a table has only it's "own events" and refers to the inherited one
     |BR|
     This need a bit of extra code for lookup! (but less data)

Those variants are currently (informally) defined, to have "some" -- as requested above.
|BR|
Besides, we can use the to measure (execution) speed differences.

Note: eventually, we could have multiple machinery's actief. Where each *component* has one set, to be used by all
**sub-components** inside, but itself uses another to talk to other components within the **super-component**

.. see also:: http://docideas.mietus.nl/en/default/CCastle/3.Design/zz.todo.html#the-machinery-todo


DirectCall  = "Machinery.DirectCall"
LibDispatch = "Machinery.LibDispatch"
DDS         = "Machinery.DDS-Study"

DirectCall_tuple        = DirectCall + ".tuple"
DirectCall_list         = DirectCall + ".list"
DirectCall_flat_dict    = DirectCall + ".dict.flat"
DirectCall_chained_dict = DirectCall + ".dict.chained"
