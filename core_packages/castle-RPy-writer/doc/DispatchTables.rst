DispatchTables in RPy
=====================



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

   .. tab:: Sieve.Main (C)

      .. code-block:: C

         #define CC_P_PowerProto_powerOn    CC_P_Protocol_NoEvents      /*6*/

      .. code-block:: C
         :emphasize-lines: 1,4

         CC_B_eventHandler cc_S_Main_power[CC_P_PowerProto_NoEvents] = { /*[7]*/
           /*CC_P_Protocol_qazEventA 0 */  (CC_B_eventHandler)CC_Mi_error,
           /*CC_P_Protocol_qazEventB 1 */  (CC_B_eventHandler)CC_Mi_error,
           /*CC_P_Protocol_qazEventC 2 */  (CC_B_eventHandler)CC_Mi_error,
           /*CC_P_Protocol_qazEventD 3 */  (CC_B_eventHandler)CC_Mi_error,
           /*CC_P_Protocol_qazEventE 4 */  (CC_B_eventHandler)CC_Mi_error,
           /*CC_P_Protocol_qazEventF 5 */  (CC_B_eventHandler)CC_Mi_error,
           /*CC_P_PowerProto_powerOn 6 */  (CC_B_eventHandler)CC_E_Main__powerOn__power};
