PortNumbers: not needed in the AIGR nor RPy
*******************************************

Summary
=======

After a successful try with (optional) *AutoNumbering*, I decided that the **port_number** *(a low int)* is an unneeded
leftover of the once “handCompiled-C” version. It isn't needed in general. And so, -as we don’t store/use *portNo*-- the
auto-numbering option is removed (but documented, as it might be convenient later).

Background
----------

In the (handCompiled) C version, everything is stored in an C-array; and we have to use (array) indexes to find the
element. Therefore, those port numbers (as index) have to be  unique, contiguous “low” numbers. In general, this is
inconvenient. When a base-component(interface) changes the number of ports, all other have to be renumbered.
|BR|
That is fine for (generated) C-code, but unwanted in e.g the AIGR-model.

Also the *Sieve_in_rPython* variant has those index ``portNo``’s -- although with a question-mark. And thy are never
used.
|BR|
Arrays in (r)Python are list and can be indexed with (e.g.) a name. Such a ``nameID`` is more convenient, and the Castle
semantics already secures uniqueness.

Thus,the  RPy backend doesn't need to render ‘PortNo’ (see
file:`castle/writers/RPy/templates/parts/interface_DataStructures.jinja2`) and hence doesn't need in the AIGR either.


AutoNumbering
==============

I have made a variant of :file:`castle/aigr/interfaces.py` to support automatically numbering of port. It quite simple.

* We need to store the `port_no` in ``Port`` and with a default marker: `_AUTO_NUMBER`.
* In ``ComponentInterface``, in the post_init a  call to ``_number_auto_ports()`` is make
* That method add portNo’s to the ports of that instance. After some basic checks.
  |BR|
  Note, the routine isn't perfect - there are complex edge cases that are ignored.

.. code-block:: ReasonML
   :emphasize-lines: 3,8

   @dataclass
   class Port(AIGR):
       _AUTO_NUMBER=-1
       name: str
       _: KW_ONLY
       direction: PortDirection
       type: PortType
       port_no: int=_AUTO_NUMBER # automatically set in ComponentInterface


.. code-block:: ReasonML
   :emphasize-lines: 4,7

   @dataclass
   class ComponentInterface(AIGR):
   ...
       def __post_init__(self):
           self._number_auto_ports()

       def _number_auto_ports(self):
           all_auto  = all(p.port_no == Port._AUTO_NUMBER for p in self.ports)
           if all_auto:
               start = self.based_on._noPorts() if isinstance(self.based_on, ComponentInterface) else 0
               for n, p in enumerate(self.ports, start=start):
                   p.port_no = n
           else:
               any_auto =any(p.port_no == Port._AUTO_NUMBER for p in self.ports)
               assert not any_auto, "Do not mix automatic port-numbering with pre-set ones. Typically, use set all!!"

.. error:: AutoNumbering is tricky

   During the development, all kind of complex edge cases are found. As the feature is removed, those checks are
   (mostly) ignored. And covert by statements as “do not mix”, “use with care”, and “only during development”.

   Conceptually, all (the inherited and own/defined) ports should be numbered: 0, 1, 2 ...
   |BR|
   Whenever a portNo can be preset, that isn’t possible. Some corner cases:

   * The pre-set numbers of two ports can be te same.

     - Ignore in auto-numbering, as it can’t be fixed (here)
     - Idea (not realised): write a checker (plugin) for the AIGR-model
     - As a variant: those non unique numbers can be set in anywhere in inherit tree of `Components`.

   * Some portNo’s are set, others not

     - We kind of need to find the available numbers first
     - Is there a reason that some numbers are skipped? Than do no use them --  complex
     - Or, just continue at the highest port-no -- more holes

   * We need all kind of auxiliary methods for ComponentInterface, to handle port-numbering

     - Not *SOLID*: code becomes hard to maintain and misleading
     - But, putting the in ``Port`` doesn't solve it


At the end, instead of “solving” those issues, I reconsidered the portNo attribute. By abandoning that left-over, all
those issues are solved too.

