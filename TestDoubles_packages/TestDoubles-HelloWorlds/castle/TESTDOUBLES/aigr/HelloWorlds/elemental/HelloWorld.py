# (C) Albert Mietus, 2024. Part of Castle/CCastle project

"""The AIGR TestDouble for elemental HelloWorld.Castle

    This file is manually crafted  from: :file:`../../../../../CastleCode/elemental/HelloWorld.Castle`"""

import logging; logger = logging.getLogger(__name__)

from castle import aigr
from castle.aigr import Source_NS
from castle.aigr import ID
from castle.aigr import ComponentImplementation, Method, EventHandler
from castle.aigr_extra.blend import mangle_event_handler

ALL = ["Hello_World"]

Hello_World = Source_NS(ID('HelloWorld'), source="HelloWorld.Castle")

#implement Elemental_HelloWorld
#{
Elemental_HelloWorld    = ComponentImplementation(ID('Elemental_HelloWorld'), outer_ns=Hello_World)

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
                            aigr.Call(callable=ID('print'), # GAM/BUG: was print without quote -- build-in function
                                      arguments=(
                                          aigr.Constant(value="Hello {label} World", type=aigr.types.string),
                                          #ID('label',context=aigr.Ref()) # GAM deze lijkt fout
                                          )))]))
#HelloWorld._register_parameters() -- now automaticly
Elemental_HelloWorld.register(HelloWorld)



#powerOn(max) on self.power
#{
#   HelloWorld("Elemental")
#}
powerOn = EventHandler(ID(mangle_event_handler(protocol='Power', event='powerOn', port='power'),context=aigr.Def()),
                       protocol=ID('Power', context=aigr.Ref()),
                       event=ID('powerOn', context=aigr.Ref()),
                       port=ID('power', context=aigr.Ref()),
                       parameters=(aigr.TypedParameter(name=ID('max'), type=int),),
                       outer_ns=Elemental_HelloWorld,
                       body=aigr.Body(statements=[
                           aigr.VoidCall(
                               aigr.Call(callable=ID('HelloWorld', context=aigr.Ref(reference=HelloWorld)),
                                         arguments=(aigr.Constant(value="Elemental"),)))]))
#powerOn._register_parameters() -- now automaticly
Elemental_HelloWorld.register(powerOn)


#} /* Elemental_HelloWorld */
Hello_World.register(Elemental_HelloWorld)

if __name__ == '__main__':
    print("Debug: print elemental_helloworld")
    print("Hello_World (NS) =\n", Hello_World)
    print("HelloWorld (Method) =\n", HelloWorld)
    print("powerOn (Event) =\n", powerOn)
