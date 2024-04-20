# (C) Albert Mietus, 2024. Part of Castle/CCastle project

from ..expressions.OpExpr import BinExpr
from ..expressions import operators


def Modulo(left, right):
    return BinExpr(left=left, op=operators.Modulo(), right=right)

def Add(left, right):
    return BinExpr(left=left, op=operators.Add(), right=right)
