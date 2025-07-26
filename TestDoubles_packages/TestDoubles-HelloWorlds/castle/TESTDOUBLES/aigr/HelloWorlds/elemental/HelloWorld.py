# (C) Albert Mietus, 2024. Part of Castle/CCastle project

"""The AIGR TestDouble for elemental HelloWorld.Castle
    source: .../TestDoubles-HelloWorlds/CastleCode/elemental/HelloWorld.Castle
    file:   .../TestDoubles-HelloWorlds/castle/TESTDOUBLES/aigr/HelloWorlds/elemental/HelloWorld.py
"""

import logging; logger = logging.getLogger(__name__)

from castle import aigr
from castle.aigr import Source_NS
from castle.aigr import ID
from castle.aigr import ComponentImplementation, Method, EventHandler
from castle.aigr_extra.blend import mangle_event_handler
from castle.aigr import ComponentInterface
from castle.aigr.components import EventDispatchTable

ALL = ["Hello_World"]

Hello_World = Source_NS(ID('HelloWorld'), source="HelloWorld.Castle")


#@impliciet(Main) ..
#implement Elemental_HelloWorld ...
__impliciet_Main_Elemental_HelloWorld = ComponentInterface(ID('Elemental_HelloWorld'), ports=[]) #ToDo: 1based_on=lib/..

Hello_World.register(__impliciet_Main_Elemental_HelloWorld, asName="__impliciet_Main_Elemental_HelloWorld")


#implement Elemental_HelloWorld
#{
Elemental_HelloWorld    = ComponentImplementation(ID('Elemental_HelloWorld'), outer_ns=Hello_World, interface=__impliciet_Main_Elemental_HelloWorld)

#HelloWorld(str:label)
#{
#   print("Hello {label} World")
#}
HelloWorld = Method(ID('HelloWorld', context=aigr.Def()),
                    returns=None,
                    outer_ns=Elemental_HelloWorld,
                    parameters=(aigr.TypedParameter(name=ID('label'), type=str),),
                    body=aigr.Body(statements=[
                        aigr.VoidCall(
                            aigr.Call(callable=ID('print'), # GAM/BUG: was print (the build-in function); now with quotes
                                      arguments=(
                                          aigr.fString(
                                              value="Hello {label} World",
                                              type=aigr.types.string,
                                              args=(
                                                  ID('label',context=aigr.Ref()),
                                                  )),)
                                          ))]))
Elemental_HelloWorld.register(HelloWorld)  # XXX
""" .. todo::

       1) `.register` on an AIGR is not allowed; use a builder-(alike) pattern
"""


#invoke() on self.std {
#   HelloWorld("Elemental")
#}
invoke = EventHandler(ID(mangle_event_handler(protocol='std', event='invoke', port='std'),context=aigr.Def()),
                       protocol=ID('std', context=aigr.Ref()),
                       event=ID('invoke', context=aigr.Ref()),
                       port=ID('std',     context=aigr.Ref()),
                       outer_ns=Elemental_HelloWorld,
                       body=aigr.Body(statements=[
                           aigr.VoidCall(
                               aigr.Call(callable=ID('HelloWorld', context=aigr.Ref(reference=HelloWorld)),
                                         arguments=(aigr.Constant(value="Elemental"),)))]))
Elemental_HelloWorld.register(invoke) # XXX
""" .. todo::

       1) `.register` on an AIGR is not allowed; use a builder-(alike) pattern
       2) EventHandlers shouldn't be in the name-space -- as:
            *) their mangle_names are useless
            *) they should be called (directly) anyhow
       3) Put them in a (event) DispatchTable!
"""

etable_std = EventDispatchTable(
    map={invoke.event: invoke.name},
    _comp=Elemental_HelloWorld.name, _port=invoke.port, _parentTable=ID('Fake_Main'))   # XXX
""" .. todo::

       1) How to put this table/entry in the AIGR?
          Probally:
           *) As datafield of ComponentImplementation
           * Use a builder-pattern
"""


#} /* Elemental_HelloWorld */
Hello_World.register(Elemental_HelloWorld)

if __name__ == '__main__':
    print("Debug: print elemental_helloworld")
    print("Hello_World (NS) =\n", Hello_World)
    print("HelloWorld (Method) =\n", HelloWorld)
    print("powerOn (Event) =\n", powerOn)
