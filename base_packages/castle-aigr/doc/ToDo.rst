.. _todo_castle-aigr:

==================
ToDo (castle-aigr)
==================

event_dispatch_tables.EventDispatchTable
========================================

.. todo:: EventDispatchTable isn’t a dataclass.

   * Rewrite/split, and
   * Make a builder

.. todo:: Design EventDispatchTable -- Rethink

   * Now, There is one big one, for all ports of the comp. Alternatively: use one (smaller) one pro port
   * The relations are unclear

     - from dispatchtable to comp/port
     - from dispatchtable to the dispatchtable(s) of the inherited one(s)

   .. seealso:: :ref:`todo_castle-RPy-writer`

      By not having a clear design, rendering the tables (in the various Machinery’s) is hard too

      With the chained-dict (directcall) Machinery, each RPython ``ChainedDict`` has to be linked to it parent, by a
      name! That name is now “gambled” - constructed, without knowing whether it is there.  
