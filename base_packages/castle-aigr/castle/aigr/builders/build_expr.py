# (C) Albert Mietus, 2024. Part of Castle/CCastle project

import logging; logger = logging.getLogger(__name__)

from ..expressions import operators
from ..expressions.operator_expressions import LRexpression, RLexpression

##
## Many builder are very similar can be written very compact with a lambda...,
## which can be meta-programmed. As doc: a few intermediate steps
##
## It is possible to write then as normal function, as shown by two examples
## .. note:: the ``if False`` comments them out
if False: # This code-block is passive; it's ref/doc only
    def Modulo(left, right, *more):
        return LRexpression(op=operators.Modulo(), values=(left,right)+more)
    def Add(left, right, *more):
        return LRexpression(op=operators.Add(), values=(left,right)+more)
    ...
# As they are short, we can replace the '2-line def' by a 1-line lambda
if False: # This code-block is passive; it's ref/doc only
    Modulo = lambda left,right, *more: LRexpression(op=operators.Modulo(), values=(left,right)+more)
    Add    = lambda left,right, *more: LRexpression(op=operators.Add(),    values=(left,right)+more)
    ...
# Again, there is a lot of repetition... which can be automated
# * The name of the builder is the same as the name of the operators.<cls>
# * We can add names:functions to this module, by writing to `globals()`
#    ``globals()[op_name] = lambda .....
def _meta_LR():
    """Meta-build all builders for all LRexpression; which all use the _LeftAssociative operator

    See the ref/code (in the module-source) above, how each function looks like.

    This function is called directly below, in this file -- having the details in function-scope 
    makes it a bit more readable, without cluttering the module-scope."""

    def _build(op):
        return lambda left,right, *more : LRexpression(op=op(), values=(left,right)+more)

    pubs    = [n for n in dir(operators) if n[0]!='_']                        # The 'public' names in 'operators'
    clsses  = [c for n in pubs   if isinstance(c:=getattr(operators,n),type)] # all classes
    ops     = [c for c in clsses if issubclass(c, operators._LeftAssociative)] # all operator (classes) that are LeftAssociative
    for op in ops:
        op_name = op.__name__
        logger.debug(f"Creating builder '{op_name}' around {op}")
        globals()[op_name] = _build(op)

def _meta_RL():
    """Meta-build the RLexpression builders, like Power"""

    def _build(op):
        return lambda left,right, *more : RLexpression(op=op(), values=(left,right)+more)

    pubs    = [n for n in dir(operators) if n[0]!='_']                        # The 'public' names in 'operators'
    clsses  = [c for n in pubs   if isinstance(c:=getattr(operators,n),type)] # all classes
    ops     = [c for c in clsses if issubclass(c, operators._RightAssociative)] # all operator (classes) that are LeftAssociative
    for op in ops:
        op_name = op.__name__
        logger.debug(f"Creating builder '{op_name}' around {op}")
        globals()[op_name] = _build(op)

#Call the meta-builders
_meta_LR()
_meta_RL()
