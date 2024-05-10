# (C) Albert Mietus, 2024. Part of Castle/CCastle project

""" This is the manual crafted AIGR TestDouble represents the sieve component implementation.

   .. see also:: :file:`./__init__.py` for a general intro
"""


from castle.aigr import ComponentImplementation, Body


# implement Sieve {
#   int myPrime;
# ...

from . import components

Sieve = ComponentImplementation('Sieve',
                                interface=components.SieveMoat,
                                parameters=(),
                                body=Body()) # Body in filed below




# init(int:onPrime)  // `init` is (typically) part of the construction of a element.
# {
#   super.init();    // `super` acts as port to the base-class
#   .myPrime := onPrime;
# }
#
# SimpleSieve.input(try) on .try
# {
#   if ( (try % .myPrime) !=0 ) {
#     .coprime.input(try);
#   }
# }
#
# } //@end Sieve
