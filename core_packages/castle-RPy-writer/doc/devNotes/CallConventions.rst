====================
When to (un)pack/box
====================

.. warning:: **The big question is: should Methods also use the :class:`Bundler`?**

Handlers
========
* An CC-(Event)Handler is always called via a (Event)DispatchTable. And thus all callables should have the same
  signature.
* With the Bundler, all args become an ``List of CC_B_Value`` -- which is (for rpython) the same signature.

Methods
=======
* A CC-Method roughly corresponds with a python-Method. Although, the `self.` prefix is not needed in the CastleCode
* In all RPY examples, the are called as ``self.<Method>(..)`` in (r)python; using the build dispatch of python
* So, it looks like we can reuse the python-signature stuff (No `Bundler` needed.
* Still, some examples use the `[` list `]` convention, some not

Functions
=========

We can classic CC-Functions (like `print`) in CastleCode. Then no dispatching is needed. And we can use the normal
calling convention: no boxing, no packing -- So no Bundler

This is more or less a **must**, to be able to call existing (python) function, like `print`

====================
How to (un)pack/box
====================

Assuming we wil ``bundle``, the generated ‘def’ has a few lines to unpack/unbox

From `~/work/TryOut/PyPy+Rpython/CallBundler/Bundle_rpy.py`
.. code-block:: python

   def call_ifsbb(self, pos, named):
       p0 = CC_B_int.unbox(pos[0])
       p1 = CC_B_float.unbox(pos[1])
       p2 = CC_B_string.unbox(pos[2])
       p3 = CC_B_boolean.unbox(pos[3])
       p4 = CC_B_boolean.unbox(pos[4])
       print (p0,p1,p2,p3,p4)


I the OLD/wrong “.value” unboxing, generating the code was easy:

* `_render_unpack` (was part of `_render_def`

-----------

NOTES
======
.. warning:: PPY calling conventions

   In CastleCode (and the AIGR), there are several ways to call an _callable, or actuallu there are several kind of _callables.
   We have traditional functions (e.g. `print`), Method (like OO-methods, but then in an Component) and (event)Handlers.

   This has effect on how the generated RPY code should look like, and wheter we should use the `Bundler`

The Elemental_HelloWorld shows all 3 variations:

* `print`						is a function (typical in a lib; but local-functions exist too)
* `HelloWorld`					is a Method
* `std.invoke() on self.std`	is an (Event)Handler


Handlers
--------
Handlers are always called via ports, and so indeitectly via a :class:`_DispatchTable` (an RPY externtion to the AIGR).
Here the 'machinery` is used.

And, as 




.. code-block:: ReasonML

   implement Elemental_HelloWorld
   {

   HelloWorld(label :string) { 			///GAM: fixed `name :type` order
      print("Hello {label} World");
   }

   std.invoke() on self.std {              ///GAM: need proto (std) in name - lookup via port not yett supported
      HelloWorld("Elemental");
   }
`HelloWorld` is a Method, `print` a function -- and so the are called differtencly in RPython
RY:         self.HelloWorld(['Elemental'])



  
..  LocalWords:  Bundler callables args rpython
