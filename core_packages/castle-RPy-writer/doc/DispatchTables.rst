=====================
DispatchTables in RPy
=====================
:status: outdated

Analyse
=======

.. tabs::

   .. tab:: HelloWorld (rpython)

      Define the index(es) into the (eventHandlers) DispatchTable -- generated

      .. code-block:: python
         :emphasize-lines: 1

         CC_P_Power_On = 1

      The DispatchTable itself (here for the `Power` port)

      .. code-block:: python
         :emphasize-lines: 3

         cc_S_Elemental_HelloWorld_power = [
             None,
             CC_Elemental_HelloWorld.Power_powerOn__power, # index: 1, CC_P_Power_On
             ]


      As a demo: The method :meth:`Power_powerOn__power` -- internally to class :class:`CC_Elemental_HelloWorld`-- is
      called when that event (number ``CC_P_Power_On`) is send to that class.

      With the `DirectCall` machinery, that result in code as shown below. The event-index is used to select the
      event-handler from the *(class+port)** DispatchTable -- resulting in a method. Which is called with the object as
      1ste parameter, and all other parameters also.
      This is basicly a one-liner.

      .. code-block:: python

         cc_S_Elemental_HelloWorld_power[CC_P_Power_On](main_elm, "__dummy__")

   .. tab:: C, (Sieve’s Main)

      In the old *“hand-compiled” C-code* --only for the Sieve-- we see the same.  Here we had to use preprocessor
      defines to be able to use names for numbers, array for the DispatchTable.
      |BR|
      Notice, the RPy-desing used this a a starting-point; maybe the PRy once can be optimized. But for now ...

      .. code-block:: C

         #define CC_P_PowerProto_powerOn    CC_P_Protocol_NoEvents      /*6*/

      .. code-block:: C
         :emphasize-lines: 1,8

         CC_B_eventHandler cc_S_Main_power[CC_P_PowerProto_NoEvents] = { /*[7]*/
           /*CC_P_Protocol_qazEventA 0 */  (CC_B_eventHandler)CC_Mi_error,
           /*CC_P_Protocol_qazEventB 1 */  (CC_B_eventHandler)CC_Mi_error,
           /*CC_P_Protocol_qazEventC 2 */  (CC_B_eventHandler)CC_Mi_error,
           /*CC_P_Protocol_qazEventD 3 */  (CC_B_eventHandler)CC_Mi_error,
           /*CC_P_Protocol_qazEventE 4 */  (CC_B_eventHandler)CC_Mi_error,
           /*CC_P_Protocol_qazEventF 5 */  (CC_B_eventHandler)CC_Mi_error,
           /*CC_P_PowerProto_powerOn 6 */  (CC_B_eventHandler)CC_E_Main__powerOn__power,
           };

      Calling ``CC_E_Main__powerOn__power`` -- here the function-name needs to include the component, as there is no
      “class namespace”-- has the same steps. Which depends on the Machinery. Again for DirectCall...
      |BR|
      Unlike above in RPy-code, the steps are written-out; in 4 lines -- but it equally.

      .. code-block:: C
         :emphasize-lines: 3,4

         { CC_ComponentType          	receiver  =  board;
           CC_B_eDispatchTable       	handlers  =  cc_S_Main_power; assert(handlers);
           CC_E_PowerProto_powerOn_FT  	signal    =  (CC_E_PowerProto_powerOn_FT)handlers[CC_P_PowerProto_powerOn]; assert(signal);
           signal(receiver, CC_B_Nil, max);
         }

Design
======


We need several kinds of DispatchTables; the most eminent ones are the event-DispatchTables.  There is one for each
(input) port, for each Component.

Each port can react to (all) events in a ``Protocol``; including the events of the base protocols. The (“name” of the)
event-handler within a component is hidden/private and not related to the name of the event; at least not
directly. Again, there is inheritance; also for Components.
|BR|
To trigger the correct eventhandler for a specific event (within a specific Component and a specific Port) the (event)
DispatchTable is used. Each component has some, one for every (input/event) port.
|BR|
Something simular is needed for other port-kinds (data & stream). Maybe we also need a DispatchTable for (component)
internal call; althogh we may depend on the OO semantics of RPy, for now.

The exact (RPy) python code depends also on the :ref:`Machinery` -- although the abtract conscepts are the same. So, we
need an abtract one in te AIGR, and specific one for RPY-writer, possible even depending on the Machinery.

It is tempting to see the DispatchTable as a (C-style) array, with an const-int (`#define` aka a file-global
constant-var) as index into a vector of function-pointer (as in the hand-compiled C version). That however is to
detailed.
|BR|
Also remember, only the most base-protocol has an event with “int index” zero (0). Most protocols inherit from another
protocol, and so the lowwest (allowed) index should be higher as inherited once.

More generic, the index of an event should be unique (in the set of related, inherited protocols), and the should be an
ordening that reflecs the ordening of the protocols.

As an example: Suppose protocol `B` inherits from protocol `A`, where `A` has 7 events, and `B` has 5 (extra); then a
port that can handle `A` needs a DispatchTable of 7 entries, whereas the DispatchTable for port that handle `B` has 12
entries. The first 7 once should “point to  the same *index*”
|BR|
This can be realized by 12 consecutive integers, 0 up to 6 for A, and 7 up to 11 for B. Here the ordening is trivial

There alternatives, like `a1 ... a7` and ` `b1 ... b5`; again the are unique and in a clear ordning.  But even `a01`,
`a02`, `a03`, `a05` , `a08`, `a12` , `a20`, `b2`, `b3`, `b5`, `b7`, `b9` is fine: unique and sortable.
|BR|
Notice, when the last B event has index ``b11``, typical sorting doesn’t work anymore! (a11 is sorted beforen a3).


AIGR
----
In AIGR, we use an abtract DispatchTable. It works as an (unsorted) dictonary, with key-value pairs, and a ``sort``
function to sort the keys. The keys should be unique, and sort function works on single key; like in the `sorted()`
function.  DispatchTable’s can be chained; which represent ‘inheritance”.
|BR|
The key (also know as `index`) should be unique within the DispatchTable, as well relative to all “chained (up)”
once. Simular, the sort function should sort correctly over a chain of DispatchTable.
Again, using integersa as key/index will work, when we sort them as numbers.

RPy
---
For PRy, we like to stay close to a C-alike implementation. And use consecutive ascending interger numbers as key. That
can simply generated from the AIGR abraction.
