# (C) Albert Mietus, 2025. Part of Castle/CCastle project

"""The AIGR TestDouble for credible HelloWorld.Castle
    source: .../TestDoubles-HelloWorlds/CastleCode/credible/HelloWorld.Castle
    file:   .../TestDoubles-HelloWorlds/castle/TESTDOUBLES/aigr/HelloWorlds/credible/HelloWorld.py
"""

import logging; logger = logging.getLogger(__name__)

from castle import aigr
from castle.aigr import Source_NS, ID, RefID
from castle.aigr import EventProtocol, Event
from castle.aigr import ComponentInterface, ComponentImplementation
from castle.aigr import Method, Initializer, EventHandler

from castle.aigr_extra.blend import mangle_event_handler

from castle.aigr_extra.scaffolding import ScaffolderNameSpace, ScaffolderCallable, ScaffolderComponentImplementation

ALL = ["Hello_World"]

#Hello_World = Source_NS(ID('HelloWorld'), source="credible/HelloWorld.Castle") # XXX ToDo: use path -- change DIR STRUCT in Testdoubles_out() 
Hello_World = Source_NS(ID('HelloWorld'), source="HelloWorld.Castle")
wrapped_HW = ScaffolderNameSpace(Hello_World)

#protocol SetLabel : EventProtocol {
#         set(label:str);
#}
SetLabel = EventProtocol(ID('SetLabel', context=aigr.Def()),
                         events=[
                             Event(ID('set', context=aigr.Def()),
                                   typedParameters=(
                                       aigr.TypedParameter(name=ID('label'), type=aigr.types.string),))])
wrapped_HW.register(SetLabel)


#component Credible {
#  port SetLabel<in>: hello;
#}
component_Credible = ComponentInterface(ID("Credible"),
                                        ports=[
                                            RefID('event',
                                                      aigr.Port(ID('hello'), direction=aigr.PortDirection.In, type=SetLabel)), # XXX
                                            ])
wrapped_HW.register(component_Credible, asName="component_Credible")

#implement Credible {
#...
Credible = ComponentImplementation(ID("Credible"), outer_ns=Hello_World, interface=component_Credible)
wrapped_Credible = ScaffolderComponentImplementation(Credible)

#...
#HelloWorld(str:label) {
#   print("Hello {label} World");
#}
#...

#SAME as elemental/HelloWorld (but for ...)
HelloWorld = Method(ID('HelloWorld', context=aigr.Def()),
                    returns=None,
                    outer_ns=Credible,
                    parameters=(aigr.TypedParameter(name=ID('label'), type=aigr.types.string),),
                    body=aigr.Body(statements=[
                        aigr.VoidCall(
                            aigr.Call(callable=ID('print'),
                                      arguments=(
                                          aigr.fString(
                                              value="Hello {label} World",
                                              type=aigr.types.string,
                                              args=[ID('label',context=aigr.Ref(reference=Credible))]
                                                  ),)
                                          ))]))
ScaffolderCallable(HelloWorld).auto_register_parameters()
wrapped_Credible.register(HelloWorld)

#...
#SetLabel.set(label) on .hello {
#  HelloWorld(label);
#}
#...
set_label = EventHandler(mangle_event_handler(protocol='SetLabel', event='set', port='hello'),
                         protocol=ID('SetLabel', context=aigr.Ref(reference=SetLabel)),
                         event=ID('set', context=aigr.Ref(reference=SetLabel.events[0])),
                         port=ID('hello', context=aigr.Ref(reference=component_Credible.ports[0])),
                         outer_ns=Credible,
                         body=aigr.Body(statements=[
                             aigr.VoidCall(
                                 aigr.Call(callable=ID('HelloWorld', context=aigr.Ref(reference=HelloWorld)),
                                               arguments=(aigr.Constant(value="Elemental"),)))]))
wrapped_Credible.register(set_label)

#...
#} //@end Credible
wrapped_HW.register(Credible)



#@impliciet(Main)
#implement Credible_HelloWorld
#{
#...

__impliciet_Main_Credible_HelloWorld = ComponentInterface(ID('Credible_HelloWorld'), ports=[])
wrapped_HW.register(__impliciet_Main_Credible_HelloWorld, asName="__impliciet_Main_Credible_HelloWorld")

Credible_HelloWorld = ComponentImplementation(ID('Credible_HelloWorld'), outer_ns=Hello_World, interface=__impliciet_Main_Credible_HelloWorld)
wrapped_Credible_HW = ScaffolderComponentImplementation(Credible_HelloWorld)

#...
#  sub credible;
#...

sub_credible = aigr.VariableDefintion(name=ID('credible', context=aigr.Def()), type="aigr.types.XXX.Component") # type: ignore[arg-type] # XXX ToDo
wrapped_Credible_HW.register(sub_credible)

#...
#init() {
#  .credible := Credible();
#}
#...
init = Initializer(ID('init', context=aigr.Def()),
              #returns=None,
              outer_ns=Credible_HelloWorld,
              #parameters=(),
              body=aigr.Body(statements=[
                  aigr.Become(
                      targets=(ID('self.credible', context=aigr.Set()),),
                      values=(aigr.Call(callable=ID('Credible', context=aigr.Ref(reference=Credible)), arguments=()),))]))
wrapped_Credible_HW.register(init)

#...
#invoke() on self.std {
#   .credible.hello.set("credible")  // trigger internal port!
#}
#...
invoke = EventHandler(mangle_event_handler(protocol='std', event='invoke', port='std'),
                      protocol=ID('std', context=aigr.Ref()),
                      event=ID('invoke', context=aigr.Ref()),
                      port=ID('std',     context=aigr.Ref()),
                      outer_ns=Credible_HelloWorld,
                      body=aigr.Body(statements=[
                          aigr.machinery.sendEvent( # Or localSendEvent() XXX
                              outport=ID('self.credible.hello', context=aigr.Ref()), # It's the inport of a sub-component!
                              event=ID('set', context=aigr.Ref()),
                              arguments=(aigr.Argument(aigr.Constant(value="credible", type=aigr.types.string)),)

                              )
                          ]))
wrapped_Credible_HW.register(invoke)

#...
#} //@end Credible_HelloWorld

wrapped_HW.register(Credible_HelloWorld)


if __name__ == '__main__':                                       # pragma: no cover
    print("Debug: print credible_helloworld")                    # pragma: no cover
    print("Hello_World (NS) =\n", Hello_World)                   # pragma: no cover
    print("SetLabel (EventProtocol) =\n", SetLabel)              # pragma: no cover

