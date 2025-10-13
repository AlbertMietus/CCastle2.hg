# (C) Albert Mietus, 2024. Part of Castle/CCastle project

"""The AIGR TestDouble for elemental HelloWorld.Castle
    source: .../TestDoubles-HelloWorlds/CastleCode/elemental/HelloWorld.Castle
    file:   .../TestDoubles-HelloWorlds/castle/TESTDOUBLES/aigr/HelloWorlds/elemental/HelloWorld.py
"""

import logging; logger = logging.getLogger(__name__)

from castle import aigr
from castle.aigr import Source_NS, ID
from castle.aigr import ComponentInterface, ComponentImplementation
from castle.aigr import  Method, EventHandler
from castle.aigr_extra.blend import mangle_event_handler

from castle.aigr_extra.scaffolding import ScaffolderNameSpace, ScaffolderCallable, ScaffolderComponentImplementation

ALL = ["Hello_World"]

#Hello_World = Source_NS(ID('HelloWorld'), source="elemental/HelloWorld.Castle") # XXX ToDo: use path -- change DIR STRUCT in Testdoubles_out() 
Hello_World = Source_NS(ID('HelloWorld'), source="HelloWorld.Castle")
wrapped_HW = ScaffolderNameSpace(Hello_World)

#@impliciet(Main) ..
#implement Elemental_HelloWorld ...
__impliciet_Main_Elemental_HelloWorld = ComponentInterface(ID('Elemental_HelloWorld'), ports=[]) #ToDo: 1based_on=lib/..

wrapped_HW.register(__impliciet_Main_Elemental_HelloWorld, asName="__impliciet_Main_Elemental_HelloWorld")


#implement Elemental_HelloWorld
#{
Elemental_HelloWorld = ComponentImplementation(ID('Elemental_HelloWorld'), outer_ns=Hello_World, interface=__impliciet_Main_Elemental_HelloWorld)
wrapped_E_HW = ScaffolderComponentImplementation(Elemental_HelloWorld)

#HelloWorld(str:label)
#{
#   print("Hello {label} World")
#}
HelloWorld = Method(ID('HelloWorld', context=aigr.Def()),
                    returns=None,
                    outer_ns=Elemental_HelloWorld,
                    parameters=(aigr.TypedParameter(name=ID('label'), type=aigr.types.string),),
                    body=aigr.Body(statements=[
                        aigr.VoidCall(
                            aigr.Call(callable=ID('print'),
                                      arguments=(
                                          aigr.fString(
                                              value="Hello {label} World",
                                              type=aigr.types.string,
                                              args=[ID('label',context=aigr.Ref())]),
                                          )))]))

ScaffolderCallable(HelloWorld).auto_register_parameters()
wrapped_E_HW.register(HelloWorld) # Register a NamedNode


#invoke() on self.std {
#   HelloWorld("Elemental")
#}
invoke = EventHandler(mangle_event_handler(protocol='std', event='invoke', port='std'),
                      protocol=ID('std', context=aigr.Ref()),
                      event=ID('invoke', context=aigr.Ref()),
                      port=ID('std',     context=aigr.Ref()),
                      outer_ns=Elemental_HelloWorld,
                      body=aigr.Body(statements=[
                          aigr.VoidCall(
                              aigr.Call(callable=ID('HelloWorld', context=aigr.Ref(reference=HelloWorld)),
                                            arguments=(aigr.Constant(value="Elemental"),)))]))
wrapped_E_HW.register(invoke) # XXX


#} /* Elemental_HelloWorld */
wrapped_HW.register(Elemental_HelloWorld) # Register a NamedNode

if __name__ == '__main__':
    print("Debug: print elemental_helloworld")
    print("Hello_World (NS) =\n", Hello_World)
    print("Elemental_HelloWorld (CompImp) =\n", Elemental_HelloWorld)
    print("HelloWorld (Method) =\n", HelloWorld)
    print("invoke (Event) =\n", invoke)
