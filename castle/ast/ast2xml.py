""" Support to translate an AST into XML.
This file should be used directly, instead use  :class:`castle.ast.serialization.Serialize` as in ``Serialize('XML')``
"""

import logging; logger = logging.getLogger(__name__)
from castle.ast import  serialization
from xml.etree import ElementTree as ET


class XML_Serialize(serialization.Serialize):
    def serialize(self, ast) -> str:
        logger.debug(f"serialize:: ast={ast._valType(ast)}")

        tree = self._ast2xml(ast)
        return ET.tostring(tree, encoding="unicode")


    def _ast2xml(self, ast, parent=None) -> ET.Element:
        if parent is None:
            parent = ET.Element('AST2XML', version="0.0")

        method_name = f'{type(ast).__name__}2xml'
        visitor = getattr(self, method_name, None)
        logger.debug(f'_ast2xml:: visitor={visitor}')

        if visitor:
            visitor(ast=ast, parent=parent) # Grow the tree
        else:
            logger.info(f'No visitor >>{method_name}<<, skipping ... (fingers crossed)')
        return parent


    def ID2xml(self, ast, parent) ->None:
        logger.debug(f"ID2xml:: ast={ast._valType(ast)} parent={parent} ast.name={ast.name}")
        ET.SubElement(parent, 'ID', name=ast.name)


#NO_VISITOR_NEEDED: PEG2xml 				## Pure Abstract
#NO_VISITOR_NEEDED: MixIn_value_attribute2xml		## MixIn
#NO_VISITOR_NEEDED: MixIn_expr_attribute2xml		## MixIn
#NO_VISITOR_NEEDED: MixIn_children_tuple2xml		## MixIn
#NO_VISITOR_NEEDED: Terminal2xml			## Pure Abstract
#NO_VISITOR_NEEDED: NonTerminal2xml			## Pure Abstract
#NO_VISITOR_NEEDED: Expression2xml			## Pure Abstract
#NO_VISITOR_NEEDED: Predicate2xml			## Pure Abstract
#NO_VISITOR_NEEDED: Group2xml				## Pure Abstract
#NO_VISITOR_NEEDED: Markers2xml				## Pure Abstract
#NO_VISITOR_NEEDED: Quantity2xml			## Pure Abstract
#NO_VISITOR_NEEDED: EOF2xml				## Not a real token


    def _MixIn_value_attribute2xml(self, ast, parent, cls_name):
        logger.debug(f"{cls_name}2xml:: ast={ast._valType(ast.value)}")
        ET.SubElement(parent, cls_name, value=ast.value)

    def StrTerm2xml(self, ast, parent):     self._MixIn_value_attribute2xml(ast, parent, 'StrTerm')
    def RegExpTerm2xml(self, ast, parent):  self._MixIn_value_attribute2xml(ast, parent, 'RegExpTerm')

    def Sequence2xml(self, ast, parent) ->None:
        logger.debug(f"Sequence2xml::ast={ast._valType(ast.value)}")
        seq = ET.SubElement(parent, 'Sequence')
        for elm in ast.value:
            self._ast2xml(elm, parent=seq)

    def Rule2xml(self, ast, parent) ->None:
        logger.debug(f"Rule2xml:: ast:Rule.name={ast.name.name}")
        rule = ET.SubElement(parent, 'Rule', name=ast.name.name)
        self._ast2xml(ast.expr, parent=rule)

    def Rules2xml(self, ast, parent) ->None:
        logger.debug(f"Rules2xml:: ast[{len(ast)}]")
        for child in ast:
            logger.debug(f'Rules2xml type(child)={type(child)}')
            self._ast2xml(child, parent=parent)

    def _quantity_op2xml(self, ast, parent, tagName) -> None:
        g = ET.SubElement(parent, tagName)
        self._ast2xml(ast.expr, g)

    def UnorderedGroup2xml(self, ast, parent): 	self._quantity_op2xml(ast, parent, 'UnorderedGroup')
    def Optional2xml(self, ast, parent): 	self._quantity_op2xml(ast, parent, 'Optional')
    def ZeroOrMore2xml(self, ast, parent): 	self._quantity_op2xml(ast, parent, 'ZeroOrMore')
    def OneOrMore2xml(self, ast, parent): 	self._quantity_op2xml(ast, parent, 'OneOrMore')


    def OrderedChoice2xml(self, ast, parent) ->None:
        oc = ET.SubElement(parent, 'OrderedChoice')
        for c in ast:
            self._ast2xml(c,oc)

    def _Predicate2xml(self, ast, parent, tagName) ->None:
        logger.debug(f"_Predicate2xml.{tagName}:: expr: {ast.expr}:{type(ast.expr).__name__}")
        predicate = ET.SubElement(parent, tagName)
        self._ast2xml(ast.expr, predicate)

    def AndPredicate2xml(self, ast, parent): self._Predicate2xml(ast, parent,'AndPredicate')
    def NotPredicate2xml(self, ast, parent): self._Predicate2xml(ast, parent,'NotPredicate')

#############

##    def Setting2xml(self, ast, parent) ->None:
##        logger.debug(f"Setting2xml:: ast[{len(ast)}]")
##        ET.SubElement(parent, 'Setting', name=ast.name, value=ast.value)

##    def Settings2xml(self, ast, parent) ->None: ...
#    def Grammar2xml(self, ast, parent) ->None: ...





#    def NotPredicate2xml(self, ast, parent) ->None: ...


