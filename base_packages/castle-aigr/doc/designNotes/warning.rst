Dispatch Tables by port
=======================
:date: 6 Jul 2025


.. warning:: An early version of :class:`aigr.EventDispatchTable` has some flaws

   1) Not a dataclass.

      The AIGR is a data-structure; but this EventDispatchTable is a typical class with (many) methods that hides the data.
      As already mention in the file, that is wrong.

      It should be split in a data-structure/class and a buider

   2) The base :class:`aigt._DispatchTable` has/needs a ref for ‘component’, which looks wrong (an not needed).

      Aside of that  it’s unclear/unspecified whether ‘comp’ is a :class:ComponentInterface`, or a
      :class:ComponentImplementation` it hardly used, and probably not need.

   3) The implementation of :class:`aigr.EventDispatchTable` has a field:
      ``_registration_byPort:  Dict[ID, Dict[ID, ID]]``

      That is WRONG.
      |BR|
      A single component can have multiple ports, but not all ports must be event-ports.


My current view, it that a (event) `DispatchTable` (in the AIGR) should be a data-class, that is associated with
a port and hold the mapping between the event-name and the handler-name.

It’s not 100% clear of the :class:`DispatchTable` needs a ref to the :class:`Port`, or :class:`Port`, refers to the
:class:`DispatchTable` (only), or both (or none).
|BR|
An alternatief is that the :class:`ComponentImplementation` maintains that information, e.g with a mapping between `Port`
and `DispatchTable`

     
