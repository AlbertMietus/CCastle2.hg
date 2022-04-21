""" Support to translate an AST into XML.
This file should NOT be used directly, instead use  :class:`castle.ast.serialization.Serialize` as in ``Serialize('XML')``
"""

import logging; logger = logging.getLogger(__name__)
from xml.etree import ElementTree as ET

from .. import Serialize

class XML_Serialize(Serialize):
    SubClassHandlers = []

    @classmethod
    def register(cls, SubHandler: type):
        logger.debug(f'{cls.__name__}.register:: SubHandler={SubHandler}')
        if  SubHandler in cls.SubClassHandlers:
            logger.warning(f"{SubHandler} already registered; ignoring")
            return False
        cls.SubClassHandlers.append(SubHandler)
        return True

    def __init__(self, *, base=None, **kwargs):
        logger.debug(f'{type(self).__name__}.__init__: base={base} kwargs={kwargs} -- SubClassHandlers=={self.SubClassHandlers}')
        self._base = base
        self._handlers = []
        # Initialise all SubClassHandlers into objects -- only for this class!!
        if type(self) is XML_Serialize:
            self._handlers = [cls(base=self) for cls in self.SubClassHandlers]
        super().__init__(**kwargs)


    def _find_visitor(self, ast):
        visitor_name = f'{type(ast).__name__}2xml'
        logger.debug(f'{type(self).__name__}._find_visitor:: {visitor_name}; for {ast}')

        # Search local (typical: nop)
        for h in self._handlers:
            visitor = getattr(h, visitor_name, None)
            if visitor:
                logger.debug(f'{type(self).__name__}._find_visitor:: found {visitor}')
                return visitor

        # Search in base
        logger.debug(f'{type(self).__name__}._find_visitor:: Going to search in {self._base}')
        if self._base:
            return self._base._find_visitor(ast)

        #None found
        logger.debug(f'{type(self).__name__}._find_visitor:: No visitor for {ast}')



    def serialize(self, ast) -> str:
        logger.debug(f"serialize:: ast={ast._valType(ast)}")
        tree = self._ast2xml(ast)
        return ET.tostring(tree, encoding="unicode")


    def _ast2xml(self, ast, parent=None) -> ET.Element:
        if parent is None:
            parent = ET.Element('AST2XML', version="0.0")

        visitor = self._find_visitor(ast)
        if visitor:
            visitor(ast=ast, parent=parent) # Grow the tree
        else:
            logger.info(f'No visitor for >>{ast}<<, skipping ... (fingers crossed)')

        return parent


###
### Register all/known subHandlers; by importing then --which executes XML_Serialize.register(....)
###
from . import _base
from . import peg
