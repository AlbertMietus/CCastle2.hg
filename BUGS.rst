BUGS
====

.. need:: Replace Arpeggio, as it is not supporting **Left-Recursion**.
   :ID: WRONG_ARPEGGIO
   :status: todo
   :tag: improvement; CCastle-syntax

   .. seealso:: http://docideas.mietus.nl/en/latest/CCastle/2.Design/syntax/2.grammar_code.html#more-details, for why we
                need Left-Recursion.

   .. tip:: Possible we can life without left-recursion for a bit; but no code/test should depend on Arpeggio
            |BR|
            It does now, a bit

.. need:: Possible, we can updated the grammar, visitors and ATS of CCastle itself
   :status: open
   :tag: test;demo
   :links: WRONG_ARPEGGIO

   The grammar, and so AST as used is probably influed by not beeing able to handle reft-recursion.
   See :need:`WRONG_ARPEGGIO`

.. todo:: mutmut does not work with python3.11 yet

   Apparently, the is a new python-VM statement: RETURN_GENERATOR (correct) that need to be supported in ‘pony’ first

   .. seealso::

      * https://github.com/boxed/mutmut/issues/266
      * https://github.com/ponyorm/pony/issues/668
      * https://github.com/ponyorm/pony/pull/671
