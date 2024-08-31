BUGS
====

.. bug:: Replace Arpeggio, as it is not supporting **Left-Recursion**.
   :ID: B_ReplaceArpeggio
   :status: todo
   :tags: improvement; CCastle-syntax

   Arpeggio does not support **Left-Recursion**, wheres other, modern PEG-parser do. Being able to use left-recursion,
   make the grammar mutch easier and closer to the AIGT.

   .. seealso:: http://docideas.mietus.nl/en/latest/CCastle/2.Design/syntax/2.grammar_code.html#more-details, for why we
                need Left-Recursion.

   .. tip:: Possible we can life without left-recursion for a bit; but no code/test should depend on Arpeggio
            |BR|
            It does now, a bit

.. bug:: Possible, we can updated the grammar, visitors and ATS of CCastle itself
   :ID: B_UpdateGrammar
   :status: open
   :tags: test; demo
   :links: B_ReplaceArpeggio

   The grammar, and so AST as used is probably influed by not beeing able to handle reft-recursion.
   See :need:`B_ReplaceArpeggio`

