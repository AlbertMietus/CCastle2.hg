TODO
=====

.. note:: py-file & pytest-files

   Moved ....

.. todo:: Makefiles

   * There are still some Makefiles (and *.mk) that contain usefull stuff -- BUT OLD
   * They are now moved/saves into the .../Mk/-dir


.. todo:: RPy `arglist:List`

   rpython can’t handle calling a method via the dispatch_tables when the number of parameters is not always the same. It complains that the
   length of a tuple(s) isn’t fixed.
   Several option are tries, in HW-credible. The only option that I have found is called `arglist:List` ...

   Basically, all arguments (when calling) should be packed in an “argList”, --which is passed as single arg-- and unpacked inside the callable.
   Then the length of the tuple is constant ... But we need to generate a bit code extra.

   See `OO_Machinery` for an alternative

.. todo:: RPy: `OO_Machinery`

   As an alternative for the issue above (`arglist:List`), is calling the EventHandler method’s via (r)Pythons own dispatcher in stead of the “dict” dispatcher.

   It appears to work in the experiments in “HW-credible”. But is further away from te original C version. Maybe it as other benefits/disadvanteds too

   For now, it is seen as a (possible future) variant “Machinery”

typedParameters
================

De “juiste volgorde is ``naam  type``.

.. seealso::  https://share.google/aimode/2yzYg4Kn95rLljly9

   * Kort: https://share.google/aimode/EFYkQPeyv9riTn81q
   * Met voorbeelden:  https://share.google/aimode/2yzYg4Kn95rLljly9


Let op, dat is de volgorde; niet de syntax. Zo gebruik python dat voor de functie `def NAAM(...) -> TYPE :`.

Rewriters
=========

.. todo:: AIGR.rewriter (oid)

   Rewriters, zoals ``@impliciet(Main)`` en ``@FSM``, moeten in de AIGR opgenomen worden, zodat de parser ze parsen (en
   koppelen aan de structuur eronder).
   Later in de toolchain zal een “plug-in” de aigr herschrijven (en ze verwijderen/archiveren ). Dat is echter niet de rol van de parser!


Vragen
------
1) Hoe koppelen?
   Let op 1 component kan meerdere @rewriters hebben (en de volgorde is relevant; van binnen naar buiten)
2) Zijn er meer van dit soort “modificer”?
   Een beetje zoals ‘OPTIONAL’ een modifier is voor parameters

.. note:: In CCP2 heet dit  *Metafunctions* (https://hsutter.github.io/cppfront/cpp2/metafunctions)
