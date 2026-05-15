# (C) Albert Mietus 2027, Part of Castle/CCastle project
import logging; logger = logging.getLogger(__name__)
import pytest

from castle import aigr
from castle.aigr import ID
from castle.aigr_extra.scaffolding import ScaffolderBody, ScaffolderCallable ## XXX ScaffolderCallable >> **Auto***
from . import *


@pytest.fixture
def demo_tree():
    """
       top :NS
        └──dad :ComponentImplementation
            └──theNode :Method (_callable)
                 ├── :Body
                 |    └──> statements [ :Become, :Become ]    -- Use Stub Become's
                 └─── returns :ReturnType                     -- a dummy value

    Note: we use `theNode` as `node` also has an internal meaning in Scaffolders """

    top  = aigr.NamedSpace('top')
    dad  = aigr.ComponentImplementation('dad', parent=top) ; top._ns[ID('dad')]= dad
    theNode = aigr.Method('theNode', parent=dad, returns=aigr.ReturnType(type=aigr.types.int)); dad.handlers.append(theNode) #type: ignore
    body = PTH.cast(aigr.Body, theNode.body)
    body.statements.append(aigr.Become(targets=None, values=None, parent=body)) #type: ignore
    body.statements.append(aigr.Become(targets=None, values=None, parent=body)) #type: ignore

    return dict(locals())

@pytest.fixture
def theNode(demo_tree) ->ScaffolderCallable:
    return ScaffolderCallable(demo_tree[ID('theNode')])

@pytest.fixture
def body(theNode) -> ScaffolderBody:
    return ScaffolderBody(theNode.body)                                     #  note: theNode.body === theNode._node.body


def test_1_theNode_has_parent_as_links(theNode, demo_tree):
    links = list(theNode.links())
    assert len(links) == 1
    assert demo_tree['dad'] in links

def test_2a_theNode_has1_kids(theNode):
    kids = list(theNode.kids())
    assert len(kids) == 1
    assert isinstance(kids[0], aigr.Body)

def test_2b_theNodeBody_has2_kids(body):
    kids = list(body.kids())
    assert len(kids) == 2
    for k in kids: # verifies the "correct" kids
        assert isinstance(k, aigr.Become)

def test_3_theNode_has_foo_attrs(theNode):
    attrs = list(theNode.attrs())
    assert len(attrs) == 1 # 'returns'
    assert isinstance(attrs[0], aigr.ReturnType)

