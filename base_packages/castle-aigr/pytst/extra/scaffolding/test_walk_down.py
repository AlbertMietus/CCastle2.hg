# (C) Albert Mietus 2026, Part of Castle/CCastle project
# Orginal version made by CodeAI: Claude

"""Tests for ScaffolderNode._kids(), .walk_down(), and .apply_down().

Naming convention:  test_<N><suffix>_<intention>
  N       : natural test order — test_<X> assumes test_<X-1> passes
  suffix  : a/b/c/… — tests that belong together at the same level
  _0*     : bootstrap — the most basic structural assertions
"""

import logging; logger = logging.getLogger(__name__)
import pytest

from castle import aigr
from castle.aigr import ID
from castle.aigr.namespaces import Scope
from castle.aigr_extra.scaffolding.node import ScaffolderNode, WalkOrder
from castle.aigr_extra.scaffolding.namespaces import ScaffolderNameSpace
from castle.aigr_extra.scaffolding.callables import ScaffolderCallable


# ======================================================================
#  Fixtures
# ======================================================================

@pytest.fixture
def leaf_node():
    """A single NamedNode with no children."""
    return aigr.NamedNode(name=ID.Def('leaf'))


@pytest.fixture
def flat_ns():
    """Source_NS with two flat NamedNode children (alpha, beta)."""
    ns = aigr.namespaces.Source_NS(name=ID.Def('root'))
    ns._ns['alpha'] = aigr.NamedNode(name=ID.Def('alpha'))
    ns._ns['beta']  = aigr.NamedNode(name=ID.Def('beta'))
    return ScaffolderNameSpace(ns)


@pytest.fixture
def nested_ns():
    """
    root (Source_NS)
     ├── flat  (NamedNode)
     └── sub   (Scope)
          ├── child_one (NamedNode)
          └── child_two (NamedNode)
    """
    root   = aigr.namespaces.Source_NS(name=ID.Def('root'))
    sub    = Scope()
    child1 = aigr.NamedNode(name=ID.Def('child_one'))
    child2 = aigr.NamedNode(name=ID.Def('child_two'))
    flat   = aigr.NamedNode(name=ID.Def('flat'))

    sub._ns['child_one'] = child1
    sub._ns['child_two'] = child2
    root._ns['flat']     = flat
    root._ns['sub']      = sub

    return ScaffolderNameSpace(root)


@pytest.fixture
def method_node():
    """A Method node with a body containing one statement."""
    from castle.aigr.statements.callables import Method
    from castle.aigr.statements.compounds import Body
    from castle.aigr.statements.simple import Become

    body = Body(statements=[Become(targets=(ID.Def('x'),), values=(aigr.Constant(value=1),))])
    m = Method(name=ID.Def('my_method'), body=body)
    from castle.aigr_extra.scaffolding.callables import ScaffolderCallable
    return ScaffolderCallable(m)


# ======================================================================
#  0 — Bootstrap: bucket collection
# ======================================================================

def test_0a_ScaffolderNode_has_link_fields():
    k, a, l = ScaffolderNode._effective_buckets()
    assert 'parent' in l

def test_0b_ScaffolderNode_parent_not_in_kids():
    k, a, l = ScaffolderNode._effective_buckets()
    assert 'parent' not in k

def test_0c_ScaffolderNode_outer_ns_is_link():
    k, a, l = ScaffolderNode._effective_buckets()
    assert 'outer_ns' in l

def test_0d_ScaffolderNode_ns_is_kid():
    k, a, l = ScaffolderNode._effective_buckets()
    assert '_ns' in k

def test_0e_ScaffolderCallable_inherits_ns_kid():
    """ScaffolderCallable must inherit _ns from ScaffolderNode (MRO union)."""
    k, a, l = ScaffolderCallable._effective_buckets()
    assert '_ns' in k

def test_0f_ScaffolderCallable_body_is_kid():
    k, a, l = ScaffolderCallable._effective_buckets()
    assert 'body' in k

def test_0g_ScaffolderCallable_parameters_is_attr():
    k, a, l = ScaffolderCallable._effective_buckets()
    assert 'parameters' in a

def test_0h_ScaffolderCallable_parameters_not_kid():
    k, a, l = ScaffolderCallable._effective_buckets()
    assert 'parameters' not in k

def test_0i_ScaffolderCallable_inherits_parent_as_link():
    k, a, l = ScaffolderCallable._effective_buckets()
    assert 'parent' in l

def test_0j_link_never_in_kids_or_attrs():
    for cls in (ScaffolderNode, ScaffolderNameSpace, ScaffolderCallable):
        k, a, l = cls._effective_buckets()
        assert k.isdisjoint(l), f"{cls.__name__}: overlap between kids and links: {k & l}"
        assert a.isdisjoint(l), f"{cls.__name__}: overlap between attrs and links: {a & l}"


# ======================================================================
#  1 — _kids() on a leaf node
# ======================================================================

def test_1a_leaf_kids_is_empty(leaf_node):
    sn = ScaffolderNode(leaf_node)
    assert list(sn._kids()) == []

def test_1b_leaf_kids_returns_generator(leaf_node):
    import types
    sn = ScaffolderNode(leaf_node)
    assert isinstance(sn._kids(), types.GeneratorType)


# ======================================================================
#  2 — _kids() on a flat namespace
# ======================================================================

def test_2a_flat_ns_kids_count(flat_ns):
    assert len(list(flat_ns._kids())) == 2

def test_2b_flat_ns_kids_are_AIGRNodes(flat_ns):
    for kid in flat_ns._kids():
        assert isinstance(kid, aigr.AIGRNode)

def test_2c_flat_ns_kids_names(flat_ns):
    names = {str(k.name) for k in flat_ns._kids()}
    assert names == {'alpha', 'beta'}

def test_2d_parent_not_in_kids(flat_ns):
    """outer_ns of root is None here, but parent must never appear."""
    kids = list(flat_ns._kids())
    # parent field value is None — should not appear
    for kid in kids:
        assert kid is not flat_ns.node.parent


# ======================================================================
#  3 — _kids() on a nested namespace (one level deep)
# ======================================================================

def test_3a_nested_direct_kids_count(nested_ns):
    """Root has 2 direct children: flat and sub (the Scope itself)."""
    assert len(list(nested_ns._kids())) == 2

def test_3b_nested_direct_kid_types(nested_ns):
    kids = list(nested_ns._kids())
    types_found = {type(k).__name__ for k in kids}
    assert types_found == {'NamedNode', 'Scope'}

def test_3c_scope_itself_has_kids(nested_ns):
    """The Scope child has two kids of its own."""
    scope_kids = [k for k in nested_ns._kids() if isinstance(k, Scope)]
    assert len(scope_kids) == 1
    scope_wrapper = ScaffolderNameSpace(scope_kids[0])
    assert len(list(scope_wrapper._kids())) == 2


# ======================================================================
#  4 — walk_down(): PRE_ORDER (default)
# ======================================================================

def test_4a_walk_default_is_pre_order(nested_ns):
    """Default walk_down should match explicit PRE_ORDER."""
    default = list(nested_ns.walk_down())
    explicit = list(nested_ns.walk_down(order=WalkOrder.PRE_ORDER))
    assert default == explicit

def test_4b_walk_pre_excludes_self_by_default(nested_ns):
    result = list(nested_ns.walk_down())
    assert nested_ns.node not in result

def test_4c_walk_pre_includes_self_when_requested(nested_ns):
    result = list(nested_ns.walk_down(include_self=True))
    assert nested_ns.node is result[0]   # self is FIRST in pre-order

def test_4d_walk_pre_total_count(nested_ns):
    """flat + sub + child_one + child_two = 4 nodes."""
    assert len(list(nested_ns.walk_down())) == 4

def test_4e_walk_pre_total_count_with_self(nested_ns):
    assert len(list(nested_ns.walk_down(include_self=True))) == 5

def test_4f_walk_pre_parent_before_children(nested_ns):
    """In pre-order the Scope must appear before its children."""
    result = list(nested_ns.walk_down())
    idx_scope  = next(i for i, n in enumerate(result) if isinstance(n, Scope))
    idx_child1 = next(i for i, n in enumerate(result) if getattr(n, 'name', None) and str(n.name) == 'child_one')
    assert idx_scope < idx_child1

def test_4g_walk_pre_all_are_AIGRNodes(nested_ns):
    for node in nested_ns.walk_down(include_self=True):
        assert isinstance(node, aigr.AIGRNode)

def test_4h_walk_pre_returns_generator(nested_ns):
    import types
    assert isinstance(nested_ns.walk_down(), types.GeneratorType)


# ======================================================================
#  5 — walk_down(): POST_ORDER
# ======================================================================

def test_5a_walk_post_children_before_parent(nested_ns):
    result = list(nested_ns.walk_down(order=WalkOrder.POST_ORDER, include_self=True))
    idx_scope = next(i for i, n in enumerate(result) if isinstance(n, Scope))
    idx_child1 = next(i for i, n in enumerate(result) if getattr(n, 'name', None) and str(n.name) == 'child_one')
    assert idx_child1 < idx_scope

def test_5b_walk_post_self_is_last(nested_ns):
    result = list(nested_ns.walk_down(order=WalkOrder.POST_ORDER, include_self=True))
    assert result[-1] is nested_ns.node

def test_5c_walk_post_count(nested_ns):
    assert len(list(nested_ns.walk_down(order=WalkOrder.POST_ORDER))) == 4

def test_5d_walk_post_excludes_self_by_default(nested_ns):
    result = list(nested_ns.walk_down(order=WalkOrder.POST_ORDER))
    assert nested_ns.node not in result


# ======================================================================
#  6 — walk_down(): LEVEL_ORDER
# ======================================================================

def test_6a_walk_level_direct_kids_before_grandchildren(nested_ns):
    """Level-order: flat and sub appear before child_one / child_two."""
    result = list(nested_ns.walk_down(order=WalkOrder.LEVEL_ORDER))
    direct_names = {'flat', 'sub'} & {str(getattr(n, 'name', '')) for n in result}
    grand_names  = {'child_one', 'child_two'} & {str(getattr(n, 'name', '')) for n in result}
    # All direct-kid indices must be < all grandchild indices
    direct_idxs = [i for i, n in enumerate(result) if str(getattr(n,'name','')) in {'flat'} or isinstance(n, Scope)]
    grand_idxs  = [i for i, n in enumerate(result) if str(getattr(n,'name','')) in {'child_one','child_two'}]
    assert max(direct_idxs) < min(grand_idxs)

def test_6b_walk_level_self_is_first_when_included(nested_ns):
    result = list(nested_ns.walk_down(order=WalkOrder.LEVEL_ORDER, include_self=True))
    assert result[0] is nested_ns.node

def test_6c_walk_level_count(nested_ns):
    assert len(list(nested_ns.walk_down(order=WalkOrder.LEVEL_ORDER))) == 4

def test_6d_walk_level_count_with_self(nested_ns):
    assert len(list(nested_ns.walk_down(order=WalkOrder.LEVEL_ORDER, include_self=True))) == 5


# ======================================================================
#  7 — apply_down()
# ======================================================================

def test_7a_apply_down_calls_func_for_each_node(nested_ns):
    collected = []
    nested_ns.apply_down(collected.append)
    assert len(collected) == 4

def test_7b_apply_down_with_include_self(nested_ns):
    collected = []
    nested_ns.apply_down(collected.append, include_self=True)
    assert len(collected) == 5
    assert collected[0] is nested_ns.node   # pre-order default

def test_7c_apply_down_returns_none(nested_ns):
    result = nested_ns.apply_down(lambda n: n)
    assert result is None

def test_7d_apply_down_post_order_self_last(nested_ns):
    collected = []
    nested_ns.apply_down(collected.append, order=WalkOrder.POST_ORDER, include_self=True)
    assert collected[-1] is nested_ns.node

def test_7e_apply_down_same_order_as_walk_down(nested_ns):
    """apply_down and walk_down must visit nodes in the same order."""
    walked  = list(nested_ns.walk_down(order=WalkOrder.POST_ORDER, include_self=True))
    applied = []
    nested_ns.apply_down(applied.append, order=WalkOrder.POST_ORDER, include_self=True)
    assert walked == applied


# ======================================================================
#  8 — Idempotency and isolation
# ======================================================================

def test_8a_walk_down_is_reentrant(nested_ns):
    """Calling walk_down twice must yield identical results."""
    r1 = list(nested_ns.walk_down())
    r2 = list(nested_ns.walk_down())
    assert r1 == r2

def test_8b_walk_does_not_mutate_node(nested_ns):
    before_keys = set(nested_ns.node._ns.keys())
    list(nested_ns.walk_down())
    assert set(nested_ns.node._ns.keys()) == before_keys

def test_8c_leaf_walk_returns_empty(leaf_node):
    sn = ScaffolderNode(leaf_node)
    assert list(sn.walk_down()) == []

def test_8d_leaf_walk_with_self_returns_one(leaf_node):
    sn = ScaffolderNode(leaf_node)
    result = list(sn.walk_down(include_self=True))
    assert result == [leaf_node]


# ======================================================================
#  9 — _attrs() — parameters as attr-kids (not recursed by walk_down)
# ======================================================================

def test_9a_method_body_is_a_walk_kid(method_node):
    """Body must appear in walk_down output."""
    walked = list(method_node.walk_down())
    body_nodes = [n for n in walked if isinstance(n, aigr.statements.compounds.Body)]
    assert len(body_nodes) == 1

def test_9b_method_parameters_not_in_walk(method_node):
    """Parameters are attrs, not structural kids — walk_down must not yield them."""
    from castle.aigr.aid import TypedParameter
    walked = list(method_node.walk_down())
    param_nodes = [n for n in walked if isinstance(n, TypedParameter)]
    assert param_nodes == []

def test_9c_attrs_yields_parameters(method_node):
    """_attrs() must yield the TypedParameter nodes."""
    # method_node has no parameters in the fixture — create one that does
    from castle.aigr.aid import TypedParameter
    from castle.aigr import types as aigr_types
    from castle.aigr.statements.callables import Method
    from castle.aigr.statements.compounds import Body
    p = TypedParameter(name=ID.Def('x'), type=aigr_types.int)
    m = Method(name=ID.Def('f'), parameters=(p,), body=Body())
    from castle.aigr_extra.scaffolding.callables import ScaffolderCallable
    sc = ScaffolderCallable(m)
    attrs = list(sc._attrs())
    assert p in attrs

def test_9d_attrs_not_in_kids(method_node):
    """No node should appear in both _kids() and _attrs()."""
    kids  = set(id(n) for n in method_node._kids())
    attrs = set(id(n) for n in method_node._attrs())
    assert kids.isdisjoint(attrs)
