""" Serialization of base-AST classes into into XML.
"""

import logging; logger = logging.getLogger(__name__)
from xml.etree import ElementTree as ET


from . import XML_Serialize

class XML_Serialize_BASE(XML_Serialize):
    def ID2xml(self, ast, parent) ->None:
        logger.debug(f"ID2xml:: ast={ast._valType(ast)} parent={parent} ast.name={ast.name}")
        ET.SubElement(parent, 'ID', name=ast.name)

XML_Serialize.register(XML_Serialize_BASE)
