import logging; logger = logging.getLogger(__name__)

class Serialize ():
    def __new__(cls, strategy=None):
        if strategy is None:
            return object.__new__(cls)
        if str(strategy).upper() == "XML":
            return XML_Serialize()
        else:
            raise NotImplementedError(f"No Serializer of {strategy} available")

        def serialize(self, ast):
            raise NotImplementedError(f"Implement in subclass")

from xml.etree import ElementTree as ET


class XML_Serialize(Serialize):
    def serialize(self, ast) -> str:
        logger.debug(f"ast={ast._valType(ast)}")

        tree = self._ast2xml(ast)
        return ET.tostring(tree, encoding="unicode")


    def _ast2xml(self, ast, parent=None) -> ET.Element:
        if parent is None:
            parent = ET.Element('AST2XML', version="0.0")

        method_name = f'{type(ast).__name__}2xml'
        visitor = getattr(self, method_name, None)
        logger.debug(f'visitor={visitor}')

        if visitor:
            visitor(ast=ast, parent=parent) # Grow the tree
        else:
            logger.info(f'No visitor >>{method_name}<<, skipping ... (fingers crossed)')
        return parent


    def ID2xml(self, ast, parent) ->None:
        logger.debug(f"ast={ast._valType(ast)} parent={parent} ast.name={ast.name}")
        ET.SubElement(parent, 'ID', name=ast.name)


#NO_VISITOR_NEEDED: PEG2xml 				## Pure Abstract
#NO_VISITOR_NEEDED: MixIn_value_attribute2xml		## MixIn
#NO_VISITOR_NEEDED: MixIn_expr_attribute2xml		## MixIn
#NO_VISITOR_NEEDED: MixIn_children_as_tuple2xml		## MixIn
#NO_VISITOR_NEEDED: Terminal2xml			## Pure Abstract
#NO_VISITOR_NEEDED: NonTerminal2xml			## Pure Abstract
#NO_VISITOR_NEEDED: Expression2xml			## Pure Abstract
#NO_VISITOR_NEEDED: Predicate2xml			## Pure Abstract
#NO_VISITOR_NEEDED: Group2xml				## Pure Abstract
#NO_VISITOR_NEEDED: Markers2xml				## Pure Abstract


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

#############

    def Setting2xml(self, ast, parent) ->None: ...
    def Settings2xml(self, ast, parent) ->None: ...
    def Grammar2xml(self, ast, parent) ->None: ...
    def UnorderedGroup2xml(self, ast, parent) ->None: ...
    def Quantity2xml(self, ast, parent) ->None: ...

    def OrderedChoice2xml(self, ast, parent) ->None: ...
    def Optional2xml(self, ast, parent) ->None: ...
    def ZeroOrMore2xml(self, ast, parent) ->None: ...
    def OneOrMore2xml(self, ast, parent) ->None: ...
    def AndPredicate2xml(self, ast, parent) ->None: ...
    def NotPredicate2xml(self, ast, parent) ->None: ...

    def EOF2xml(self, ast, parent) ->None: pass # Needed
