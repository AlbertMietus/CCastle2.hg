# (C) Albert Mietus, 2025,  Part of CCastle project

import logging; logger = logging.getLogger(__name__)
import pytest
import typing as PTH                                                                                  # Python TypeHints

from castle import aigr
from castle.aigr import ID
from castle.aigr import ComponentImplementation

from castle.aigr_extra.scaffolding import ScaffolderNameSpace

from . import a_node, outer_NS


def test_ComponentImplementation_hasScope(a_node):
    """An component(implementation) act as a namedspace: we can register nodes, and find them"""
    aComp = ScaffolderNameSpace(ComponentImplementation(ID('aComp')))
    aComp.register(a_node)
    assert aComp.findNode('a_node') is a_node

def test_ComponentImplementation_has_outer_NS(outer_NS, a_node):
    """Inside a component(implementation) we can refer/find nodes that are defined
       in the namespaces which contain the contain the component.

       .. note::

          * Usally, the component is registered in that NS, but that is not done/tested here
          * We only need to set the outer_namespace when creating the Component  """
    aComp=ComponentImplementation(ID('aComp'), outer_ns=outer_NS)
    assert aComp.findNode('a_node') is a_node


def test_callable_hasScope_Method(a_node):
    """Same as above: Method is a callable, and to has scope"""
    aMethod = aigr.Method(ID('aMethod'))
    aMethod.register(a_node)
    assert aMethod.findNode('a_node') is a_node

def test_callable_has_outer_NS_Method(outer_NS, a_node):
    callable = aigr.Method(ID('aMethod'), outer_ns=outer_NS)
    assert callable.findNode('a_node') is a_node


def test_callable_hasScope_EventHandler(a_node):
    callable=aigr.EventHandler('anEventHandler', protocol='a_protocol', event='an_event', port='a_port')
    callable.register(a_node)
    assert callable.findNode('a_node') is a_node

def test_callable_has_outer_NS_EventHandler(outer_NS, a_node):
    callable=aigr.EventHandler('anEventHandler', protocol='a_protocol', event='an_event', port='a_port', outer_ns=outer_NS)
    assert callable.findNode('a_node') is a_node

