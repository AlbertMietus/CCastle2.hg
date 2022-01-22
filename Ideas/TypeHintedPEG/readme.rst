.. (C) ALbert Mietus, 2022, Part of CCastel(2).

Type-Hinted PEGs (or other grammar)
===================================

The transitional (PEG-)syntax is like:

.. code-block:: peg

   single_expr	<-  ( rule_crossref
                    | term
                    | group
                    | predicate
                    ) ( '?' | '*' | '+' | '#' )? ;

The question is: *“Can we use *TypeHits* (similar as in python)”*?

Surely, that is possible. Then we get something like below, where (only) the result//lhs has a type hint

.. code-block:: peg

   single_expr:SingleExpr <-  ( rule_crossref
                              | term
                              | group
                              | predicate
                              ) ( '?' | '*' | '+' | '#' )? ;

Or even
.. code-block:: peg

   single_expr	<-  ( rule_crossref : ID
                    | term:Term
                    | group: Sequence
                    | predicate:Predicate
                    ) ( '?' | '*' | '+' | '#' )? ;

The idea is to make it more readable, but also *TypeHints* may be useful for
* ?*Vistors*?
* Type Checking
* to be discovered
