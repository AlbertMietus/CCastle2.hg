# (C) Albert Mietus, 2024. Part of Castle/CCastle project

import logging; logger = logging.getLogger(__name__)

from ..expressions import operators
from ..expressions.expr_with_op import BinExpr


##
## Many builder are very similar can be written very compact with a lambda...,
## which can be meta-programmed. As doc: a few intermediate steps
##
## It is possible to write then as normal function, as shown by two examples
## .. note:: the ``if False`` comments them out
if False: # This code-block is passive; it's ref/doc only
    def Modulo(left, right):
        return BinExpr(left=left, op=operators.Modulo(), right=right)
    def Add(left, right):
        return BinExpr(left=left, op=operators.Add(), right=right)
    ...
# As they are short, we can replace the '2-line def' by a 1-line lambda
if False: # This code-block is passive; it's ref/doc only
    Modulo = lambda left,right: BinExpr(left=left, op=operators.Modulo(), right=right)
    Add    = lambda left,right: BinExpr(left=left, op=operators.Add(),    right=right)
    ...
# Again, there is a lot of repetition... which can be automated
# * The name of the builder is the same as the name of the operators.<cls>
# * All BinExpr-operators are a subclass of `operators._bin_op`
# * We can add names:functions to this module, by writing to `globals()`
#    ``globals()[op_name] = lambda this_op: BinExpr(left=left, op=this_op, right=right)``
# Remember: we have to call the lambda and fill in an **instance** op the op-class
def _meta_BinExpr():
    """Meta-build all builders of all defined `_bin_op` classes, and put the in this module

    See the ref/code (in the module-source) above, how each function looks like.

    This function is called directly below, in this file -- having the details in function-scope 
    makes it a bit more readable, without cluttering the module-scope."""

    def _build(op):
        return lambda left,right : BinExpr(left=left, op=op(), right=right)

    pubs    = [n for n in dir(operators) if n[0]!='_']                        # The 'public' names in 'operators'
    clsses  = [c for n in pubs   if isinstance(c:=getattr(operators,n),type)] # all classes
    bin_ops = [c for c in clsses if issubclass(c, operators._bin_op)]         # all operators, for BinExpr
    for op in bin_ops:
        op_name = op.__name__
        logger.debug(f"Creating builder '{op_name}' around {op}")
        globals()[op_name] = _build(op)

_meta_BinExpr()
