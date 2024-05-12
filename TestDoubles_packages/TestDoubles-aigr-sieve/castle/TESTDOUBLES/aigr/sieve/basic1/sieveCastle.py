# (C) Albert Mietus, 2024. Part of Castle/CCastle project

""" This is the manual crafted AIGR TestDouble represents the sieve component implementation.

   .. see also:: :file:`./__init__.py` for a general intro
"""

__all__ = ['Sieve']


from castle import aigr
from castle.aigr import ComponentImplementation, ID, Method



# implement Sieve {
#   int myPrime;
# ...

from . import components

Sieve = ComponentImplementation('Sieve',
                                interface=components.SieveMoat,
                                parameters=(),
                                body=aigr.Body()) # Body in filed below

# init(int:onPrime)  // `init` is (typically) part of the construction of a element.
# {
#   super.init();    // `super` acts as port to the base-class
#   .myPrime := onPrime;
# }

init_method = Method(ID('init'),
                         returns=None,
                         parameters=(aigr.TypedParameter(name=ID('onPrime'), type=int),),
                         body=aigr.Body(statements=[
                             aigr.Call(
                                 callable=aigr.Part(
                                     base=aigr.Call(callable=ID('super')), attribute=ID('init')),
                                 arguments=()),
                             aigr.Become(
                                        targets=(aigr.Part(base=ID('self'), attribute=ID('myPrime', context=aigr.Set())),),
                                        values=(ID('onPrime', context=aigr.Ref()),))]))

assert isinstance(Sieve.body, aigr.Body) # This make mypy happy for the next line :-)
Sieve.body.expand(init_method)





# SimpleSieve.input(try) on .try
# {
#   if ( (try % .myPrime) !=0 ) {
#     .coprime.input(try);
#   }
# }
#
# } //@end Sieve
