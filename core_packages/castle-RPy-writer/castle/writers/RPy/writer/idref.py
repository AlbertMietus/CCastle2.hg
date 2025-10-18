# (C) Albert Mietus, 2025. Part of Castle/CCastle project

import logging; logger = logging.getLogger(__name__)

from castle.monorail.base.visitors import Visitor
from castle import aigr

class IDRef(Visitor):
    """An ID with an aigr.Ref() as should be rendered depending on the AIGR it reffers.
       IDRef is an auxility class of Renderer, for those case.

       It main entry-point is ``portray()`` which returns (a typical short) string. The single
       argument is `node:aigr.ID` -- which is the ID itself. **NOT** the ref! """

    _defaultType=str                      #used in Visitor, to return a default value of the right type

    def __init__(self, renderer):
        self._renderer = renderer

    def portray(self, node: aigr.ID) ->str: # MAYBE: add 'hint', then also in Visitor
        """
        Parameters
        ----------
        node : aigr.ID
            The ID (with a ref) that will be converted to a string.

        Returns
        -------
        str
            The text, to be used when rendering this ID -- it depend on the (class of the context
        """
        logger.info("IDRef.portray: %s", str(node))

        assert node.context.reference, f"IDRef needs a set reference as context {node=}"
        return self.visit(node, dispatch_on=node.context.reference)

    def _default_visit(self, node:aigr.ID): # XXX TMP
        raise NotImplementedError("No IDRef::visit_%s, Can't portray: %s", type(node).__name__, node )

    def visit_ID(self, node):
        """This node (an ID) refers anotherID: easy - render it"""
        return self._renderer.visit(node.context.reference) # XXX See test_1...

    def visit_ComponentInterface(self, node):
        return self._renderer.portray.cc_CI_elm_prefix(str(node))

    def visit_ComponentImplementation(self, node):
        # refer to `class CC_$Name` --subclass of buildin.CC_B_Component`
        return self._renderer.portray.CC_cls_prefix(str(node))


    def visit_ComponentClass(self, node):
        """ Which one GAM XXX ToDo"""
        #return self._renderer.portray.cc_C_elm_prefix(str(node))
        return self._renderer.portray.cc_CI_elm_prefix(str(node))

    def visit__Named_callable(self, node):
        return self._renderer.portray.callDef_name(node)


    def visit_AIGR(self, node):  # HACK
        txt = str(node)
        logger.error("IDRef/AIGR: Not Implemented; use node, not ref. %s -> %s", node, txt)
        return txt

    def visit_str(self, node):  # Unusual_but_Fine
        return node.context.reference
