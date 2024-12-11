# (C) Albert Mietus, 2024. Part of Castle/CCastle project

"""The AIGR TestDouble for elemental HelloWorld.Castle

    This file is manually crafted  from: :file:`../../../../../CastleCode/elemental/HelloWorld.Castle`"""

from castle import aigr
from castle.aigr import Source_NS, ID
from castle.aigr import ComponentImplementation, Method, EventHandler
from castle.aigr_extra.blend import mangle_event_handler

ALL = ["elemental"]

elemental = Source_NS(ID('HelloWorld'), source="HelloWorld.Castle")

#implement Elemental_HelloWorld
#{
Elemental_HelloWorld = ComponentImplementation(ID('Elemental_HelloWorld'))


#HelloWorld(str:label)
#{
#   print("Hello {label} World")
#}
HelloWorld = Method(ID('HelloWorld'),
                    returns=None,
                    parameters=(aigr.TypedParameter(name=ID('label'), type=str),),
                    body=aigr.Body(statements=[
                        aigr.VoidCall(
                            aigr.Call(callable=ID(print), arguments=(
                                aigr.Constant(value="Hello {label} World"),
                                ID('label',context=aigr.Ref()))))]))
Elemental_HelloWorld.body.expand(HelloWorld)


#powerOn(max) on self.power  ///GAM: Here it starts ...
#{
#   HelloWorld("Elemental")
#}

powerOn = EventHandler(ID(mangle_event_handler(protocol='Power', event='powerOn', port='power'),context=aigr.Def()),
                       protocol=ID('Power', context=aigr.Ref()),
                       event=ID('powerOn', context=aigr.Ref()),
                       port=ID('power', context=aigr.Ref()),
                       parameters=(aigr.TypedParameter(name=ID('max'), type=int),),
                       body=aigr.Body(statements=[
                           aigr.VoidCall(
                               aigr.Call(
                                   callable=ID('HelloWorld', context=aigr.Ref(reference=HelloWorld)),
                                   arguments=(aigr.Constant(value="Elemental"),))) ]))
Elemental_HelloWorld.body.expand(HelloWorld, powerOn)


#} /* Elemental_HelloWorld */
elemental.register(Elemental_HelloWorld)

if __name__ == '__main__':
    print("Debug: print elemental_helloworld")
    print("elemental (NS) =\n", elemental)
    print("HelloWorld (Method) =\n", HelloWorld)
    print("powerOn (Event) =\n", powerOn)
