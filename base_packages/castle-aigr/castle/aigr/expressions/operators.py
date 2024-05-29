# (C) Albert Mietus, 2023-2024. Part of Castle/CCastle project

from __future__ import annotations # Postponed evaluation of annotations

from .. import AIGR

class _operator(AIGR): pass

class _LeftAssociative(_operator)    : """Left associative operators"""
class Times(_LeftAssociative)        : '''*'''
class Div(_LeftAssociative)          : '''/'''
class Modulo(_LeftAssociative)       : '''%'''
class Add(_LeftAssociative)          : '''+'''
class Sub(_LeftAssociative)          : '''-'''
#class MatrixMult(_LeftAssociative)	 : '''@'''    	# Probably NOT needed

class _RightAssociative(_operator)   : """Right associative operators"""
class Power(_RightAssociative)       : '''**'''

class _compare_op(_operator)         : """Compare 2 or more values --The expression can be cascaded `1<2<3`, always resulting in True/False"""
class Equal(_compare_op)             : '''=='''
class NotEqual(_compare_op)          : '''!='''
#class Unequal(_compare_op)           : '''<>'''   	# Probably NOT needed
class Less(_compare_op)              : '''<'''
class LessEqual(_compare_op)         : '''<='''
class Greater(_compare_op)           : '''>'''
class GreaterEqual(_compare_op)      : '''>='''
class Is(_compare_op)                : '''is'''
class IsNot(_compare_op)             : '''is not'''
class In(_compare_op)                : '''in'''
class NotIn(_compare_op)             : '''not in'''

class _boolean_op(_operator)         : """Operate on boolean values"""
class _ShortCircuit(_operator)       : """Operators, that stop when the result is fixed -- resulting in the 'last' value"""
class _bool_SC_op(_boolean_op, _ShortCircuit): pass
class And(_bool_SC_op)  	         : '''and'''
class Nand(_bool_SC_op)  	         : '''nand'''
class Or(_bool_SC_op)  	             : '''or'''
class Nor(_bool_SC_op)  	         : '''nor'''
#XOR/XNOR can not Short Circuit
class Xor(_boolean_op)  	         : '''xor'''
class Xnor(_boolean_op)  	         : '''xnor'''


class _unart_op(_operator)           : """Operates on only one value"""
class Not(_unart_op, _boolean_op)    : '''not'''            #Unary not -- always True/False
class Negative(_unart_op) 		     : '''- (unary)'''
class Positive(_unart_op) 		     : '''+ (unary)'''


