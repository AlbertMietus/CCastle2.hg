# (C) Albert Mietus, 2024. Part of Castle/CCastle project

""" This is the manual crafted AIGR TestDouble represents the sieve component implementation.

   .. see also:: :file:`./__init__.py` for a general intro
"""

__all__ = ['Sieve']


from castle import aigr
from castle.aigr import ComponentImplementation, ID
from castle.aigr import Method, EventHandler

from castle.aigr_extra.blend import mangle_event_handler
from castle.aigr_extra  import builders

from . import components, protocols

# implement Sieve {
#   int myPrime;
# ...
Sieve = ComponentImplementation(ID('Sieve'),
                                interface=components.SieveMoat,
                                parameters=(),
                                body=aigr.Body()) # Body filled-in below

assert isinstance(Sieve.body, aigr.Body) # This make mypy happy to fill-in the Body



# init(int:onPrime)  // `init` is (typically) part of the construction of a element.
# {
#   super.init();    // `super` acts as port to the base-class
#   .myPrime := onPrime;
# }
init_method = Method(ID('init'),
                         returns=None,
                         parameters=(aigr.TypedParameter(name=ID('onPrime'), type=int),), # XXX Really: int?
                         body=aigr.Body(statements=[
                             aigr.VoidCall(
                                 aigr.Call(
                                    callable=aigr.Part(
                                        base=aigr.Call(callable=ID('super')), attribute=ID('init', context=aigr.Ref())),
                                    arguments=())),
                             aigr.Become(
                                        targets=(aigr.Part(base=ID('self'), attribute=ID('myPrime', context=aigr.Set())),),
                                        values=(ID('onPrime', context=aigr.Ref()),))]))
Sieve.body.expand(init_method)



# SimpleSieve.input(try) on .try
# {
#   if ( (try % .myPrime) !=0 ) {
#     .coprime.input(try);
#   }
# }
#
# } //@end Sieve
event_handler_1 = EventHandler(ID(mangle_event_handler(protocol="SimpleSieve", event="input", port="try"), context=aigr.Def()),
                               protocol=ID('SimpleSieve', context=aigr.Ref()),
                               event=ID('input', context=aigr.Ref()),
                               port=ID('try', context=aigr.Ref()),
                               body=aigr.Body(statements=[
                                   aigr.If(
                                       test=aigr.Compare(
                                           ops=aigr.operators.NotEqual(),
                                           values=(
                                               builders.Modulo(
                                                   ID("try", context=aigr.Ref()),
                                                   ID("myPrime",context=aigr.Ref())),
                                               aigr.Constant(value=0),)),
                                       body=aigr.Body(
                                           statements=[
                                               aigr.machinery.sendEvent(
                                                   outport=aigr.Part(base=ID('self'), attribute=ID('coprime', context=aigr.Ref())),
                                                   event=ID('input',context=aigr.Ref()),
                                                   arguments=[aigr.Argument(ID('try', context=aigr.Ref()))])
                                               ]))]))
Sieve.body.expand(event_handler_1)
