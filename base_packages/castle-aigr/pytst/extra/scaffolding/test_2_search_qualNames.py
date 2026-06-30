# (C) Albert Mietus 2025, Part of Castle/CCastle project
# partly made by claude-AI

#GAM: XXX some test have to be rewritten.
#GAM: XXX Also, add (the same tests) ad dottedNames (ipv QualID)

import logging; logger = logging.getLogger(__name__)
import pytest

from castle import aigr
from castle.aigr import ID
from castle.aigr.tools.scaffolding.namespaces import ScaffolderNameSpace


@pytest.fixture
def empty_ns():
    """An empty namespace"""
    ns = aigr.namespaces.Source_NS(ID.Def('root'))
    return ScaffolderNameSpace(ns)

@pytest.fixture
def flat_ns():
    """A namespace with 3 flat (non-namespace) nodes"""
    ns = aigr.namespaces.Source_NS(name=ID.Def('root'))
    s = ScaffolderNameSpace(ns)
    for name in ('alpha', 'beta', 'gamma'):
        node = aigr.NamedNode(name=ID.Def(name))
        s.register_NamedNode(node)
    return s

@pytest.fixture
def nested_ns():
    """A namespace with 2 flat nodes and 1 sub-namespace containing 2 nodes"""
    root_ns  = aigr.namespaces.Source_NS(name=ID.Def('root'))
    child_ns = aigr.namespaces.Scope()

    child_node_1 = aigr.NamedNode(name=ID.Def('child_one'))
    child_node_2 = aigr.NamedNode(name=ID.Def('child_two'))
    child_ns._ns['child_one'] = child_node_1
    child_ns._ns['child_two'] = child_node_2

    flat_node = aigr.NamedNode(name=ID.Def('flat'))
    root_ns._ns['flat']     = flat_node
    root_ns._ns['sub']      = child_ns

    return ScaffolderNameSpace(root_ns)


def test_0a_empty_returns_empty_tuple(empty_ns):
    result = empty_ns.search_qualNames()
    assert result == ()

def test_0b_empty_is_tuple(empty_ns):
    assert isinstance(empty_ns.search_qualNames(), tuple)


##
## Tests: flat namespace (no sub-namespaces)
##

def test_1a_flat_count(flat_ns):
    assert len(flat_ns.search_qualNames()) == 3

def test_1b_flat_each_is_list_of_one_ID(flat_ns):
    for qualid in flat_ns.search_qualNames():
        assert isinstance(qualid, list)
        assert len(qualid) == 1
        assert isinstance(qualid[0], ID)

def test_1c_flat_names(flat_ns):
    names = [str(q[0]) for q in flat_ns.search_qualNames()]
    assert set(names) == {'alpha', 'beta', 'gamma'}


##
## Tests: nested namespace
##

def test_2a_nested_total_count(nested_ns):
    """flat + sub-ns itself + 2 children = 4"""
    assert len(nested_ns.search_qualNames()) == 4

def test_2b_nested_flat_node_is_depth_1(nested_ns):
    qualids = nested_ns.search_qualNames()
    flat = [q for q in qualids if str(q[0]) == 'flat']
    assert len(flat) == 1
    assert len(flat[0]) == 1

def test_2c_nested_sub_ns_itself_is_depth_1(nested_ns):
    qualids = nested_ns.search_qualNames()
    sub = [q for q in qualids if len(q) == 1 and str(q[0]) == 'sub']
    assert len(sub) == 1

def test_2d_nested_children_are_depth_2(nested_ns):
    qualids = nested_ns.search_qualNames()
    deep = [q for q in qualids if len(q) == 2]
    assert len(deep) == 2

def test_2e_nested_child_names(nested_ns):
    qualids = nested_ns.search_qualNames()
    deep = [q for q in qualids if len(q) == 2]
    leaf_names = {str(q[1]) for q in deep}
    assert leaf_names == {'child_one', 'child_two'}

def test_2f_nested_child_prefix_is_sub(nested_ns):
    qualids = nested_ns.search_qualNames()
    deep = [q for q in qualids if len(q) == 2]
    for q in deep:
        assert str(q[0]) == 'sub'


##
## Tests: bijzondere gevallen
##

def test_3a_qualid_elements_are_IDs(nested_ns):
    """All elements in all QualIDs must be ID instances"""
    for qualid in nested_ns.search_qualNames():
        for part in qualid:
            assert isinstance(part, ID)

def test_3b_prefix_not_mutated(nested_ns):
    """The internal _prefix list must not leak or mutate between calls"""
    result1 = nested_ns.search_qualNames()
    result2 = nested_ns.search_qualNames()
    assert result1 == result2
