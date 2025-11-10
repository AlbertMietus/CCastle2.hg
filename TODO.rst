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

   It appears to work in the experiments in “HW-credible”. But is further away from te original C version. Maybe it as other benefits/disadvanteds to

   For now, it is seen as a (possible future) variant “Machinery”

