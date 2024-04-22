# (C) Albert Mietus, 2023-2024. Part of Castle/CCastle project

from __future__ import annotations # Postponed evaluation of annotations
import logging; logger = logging.getLogger(__name__)

import typing as PTH                                                                                 # Python TypeHints
from dataclasses import dataclass, KW_ONLY
from dataclasses import field as dc_field

from .. import AIGR

class _operator(AIGR): pass

class _bin_op(_operator):    "Operate on two values"                      # Why not cascaded?
class Power(_bin_op)   		:'**'
class Times(_bin_op)        : '*'
class Div(_bin_op)          : '/'
class Modulo(_bin_op)       : '%'
class Add(_bin_op)          : '+'
class Sub(_bin_op)          : '-'
#class MatrixMult(_bin_op)	: '@'    	# Probably NOT needed

class _compare_op(_operator): "Compare 2 or more values --The expression can be cascaded `1<2<3`"
class Equal(_compare_op):         '=='
class Notequal(_compare_op):      '!='
#class Uequal(_compare_op):        '<>'   	# Probably NOT needed
class Less(_compare_op):          '<'
class LessEqual(_compare_op):     '<='
class Greater(_compare_op):       '>'
class GreaterEqual(_compare_op):  '>='
class Is(_compare_op):            'is'
class IsNot(_compare_op):         'is not'
class In(_compare_op):            'in'
class NotIn(_compare_op):         'not in'


class _boolean_op(_operator): "Operate on boolean values"
class And(_boolean_op):  	'and'
class Nand(_boolean_op):  	'nand'
class Or(_boolean_op):  	'or'
class Nor(_boolean_op):  	'nor'
class Xor(_boolean_op):  	'xor'
class Xnor(_boolean_op):  	'xnor'


class _unart_op(_operator): "Operates on only one value"
class Not(_unart_op):  			'not'            #Unary not
class Negative(_unart_op): 		'- (unary)'
class Positive(_unart_op): 		'+ (unary)'


