# (C) Albert Mietus, 2024. Part of Castle/CCastle project

import logging; logger = logging.getLogger(__name__)

from ...aigr.expressions import operators
from ...aigr.expressions.operator_expressions import LRexpression, RLexpression

##
## Many builder are very similar can be written very compact with a lambda...,
## which can be meta-programmed. As doc: a few intermediate steps
##
## It is possible to write then as normal function, as shown by two examples
## .. note:: the ``if False`` comments them out
if False: # This code-block is passive; it's ref/doc only  						# pragma: no cover  # pragma: no mutate
    def Modulo(left, right, *more):  											# pragma: no cover  # pragma: no mutate
        return LRexpression(op=operators.Modulo(), values=(left,right)+more)  	# pragma: no cover  # pragma: no mutate
    def Add(left, right, *more):  												# pragma: no cover  # pragma: no mutate
        return LRexpression(op=operators.Add(), values=(left,right)+more) 		# pragma: no cover  # pragma: no mutate
    ...
# As they are short, we can replace the '2-line def' by a 1-line lambda
if False: # This code-block is passive; it's ref/doc only  												# pragma: no cover  # pragma: no mutate
    Modulo = lambda left,right, *more: LRexpression(op=operators.Modulo(), values=(left,right)+more)	# pragma: no cover  # pragma: no mutate
    Add    = lambda left,right, *more: LRexpression(op=operators.Add(),    values=(left,right)+more)	# pragma: no cover  # pragma: no mutate
    ... 																								# pragma: no cover  # pragma: no mutate
# Again, there is a lot of repetition... which can be automated
# * The name of the builder is the same as the name of the operators.<cls>
# * We can add names:functions to this module, by writing to `globals()`
#    ``globals()[op_name] = lambda .....


def _meta_build(super_op, expr):
    """Meta-build the builders for (the subclasses of super_op"

    See the ref/code (in the module-source) above, how each function looks like."""

    def _build(op, association):
        return lambda left,right, *more : association(op=op(), values=(left,right)+more)

    pubs    = [n for n in dir(operators) if n[0]!='_']                        # The 'public' names in 'operators'
    clsses  = [c for n in pubs   if isinstance(c:=getattr(operators,n),type)] # all classes
    ops     = [c for c in clsses if issubclass(c, super_op)] # all operator (classes) that are Left/Right-Associative
    for op in ops:
        op_name = op.__name__
        logger.debug(f"Creating builder '{op_name}' around {op}")
        globals()[op_name] = _build(op, expr)

#Call the meta-builder
_meta_build(super_op=operators._LeftAssociative,  expr=LRexpression)
_meta_build(super_op=operators._RightAssociative, expr=RLexpression)
