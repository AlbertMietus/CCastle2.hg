# (C) Albert Mietus, 2024. Part of Castle/CCastle project

import logging; logger = logging.getLogger(__name__)

from ..expressions import operators
from ..expressions.OpExpr import BinExpr


##
## Many builder are very similar can be written very compact with a lambda...
##
## It is possible to write then as normal function, as shown by two examples
## .. note:: the ``if False`` comments them out
if False:
    def Modulo(left, right):
        return BinExpr(left=left, op=operators.Modulo(), right=right)
    def Add(left, right):
        return BinExpr(left=left, op=operators.Add(), right=right)

# Or we can meta-build them, "calling" `_build` for each operator, wich returns
# a lambda function, filling in the "std" text (as above), and
# storing them in the current module...
def _build(op):
        return lambda left,right : BinExpr(left=left, op=op(), right=right)

for op in (operators.Modulo, operators.Add, operators.Sub):
        op_name = op.__name__
        logger.debug(f"Creating builder '{op_name}' around {op}")
        globals()[op_name] = _build(op)

