""" Serialization of PEG- AST classes into into XML.
    This file should NOT be used directly, instead use  :class:`castle.ast.serialization.Serialize` as in ``Serialize('XML')``
"""

import logging; logger = logging.getLogger(__name__)
from xml.etree import ElementTree as ET

from . import XML_Serialize


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
#NO_VISITOR_NEEDED: ParseRules2xml			## Handle in Rules2xml
#NO_VISITOR_NEEDED: Settings2xml			## Handle in Rules2xml


class XML_Serialize_PEG(XML_Serialize):

    def _MixIn_value_attribute2xml(self, ast, parent, cls_name):
        logger.debug(f"{cls_name}2xml:: ast={ast._valType(ast.value)}")
        ET.SubElement(parent, cls_name, value=ast.value)

    def StrTerm2xml(self, ast, parent):     self._MixIn_value_attribute2xml(ast, parent, 'StrTerm')
    def RegExpTerm2xml(self, ast, parent):  self._MixIn_value_attribute2xml(ast, parent, 'RegExpTerm')

    def Sequence2xml(self, ast, parent) ->None:
        logger.debug(f"Sequence2xml::ast={ast._valType(ast._children)}")
        seq = ET.SubElement(parent, 'Sequence')
        for elm in ast:
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


    def Number2xml(self, ast, parent) ->None:
        logger.debug(f"Number2xml:: ast: {ast}:{type(ast).__name__}")
        n = ET.SubElement(parent, 'Number')
        n.text=ast.value


    def Setting2xml(self, ast, parent) ->None:
        logger.debug(f"Setting2xml:: ast: {ast}:{type(ast).__name__}")
        setting = ET.SubElement(parent, 'Setting')
        self._ast2xml(ast.name, setting)
        self._ast2xml(ast.value, setting)

    def Grammar2xml(self, ast, parent) ->None:
        g = ET.SubElement(parent, 'Grammar', no_parse_rules=str(len(ast.parse_rules)), no_settings=str(len(ast.settings)))
        self._ast2xml(ast._all_rules, g)

XML_Serialize.register(XML_Serialize_PEG)
