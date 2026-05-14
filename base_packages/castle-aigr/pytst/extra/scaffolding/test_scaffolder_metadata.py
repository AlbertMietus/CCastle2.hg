# (C) Albert Mietus 2026, Part of Castle/CCastle project

"""Tests for ScaffolderNode field bucket metadata and kids()/attrs() functionality.

This test file ensures that:
1. Field bucket metadata is correctly declared for all Scaffolder subclasses
2. The kids() method correctly yields structural children
3. The _attrs() method correctly yields attribute-like metadata
4. Future AIGR node types don't forget to declare their metadata

Naming convention:  test_<N><suffix>_<intention>
  N       : natural test order — test_<X> builds on previous tests
  suffix  : a/b/c/… — tests that belong together at the same level
  _0*     : bootstrap — basic structural assertions about metadata
"""

import logging; logger = logging.getLogger(__name__)
import pytest

from castle import aigr
from castle.aigr import ID
from castle.aigr.namespaces import Scope
from castle.aigr_extra.scaffolding.node import ScaffolderNode
from castle.aigr_extra.scaffolding.namespaces import ScaffolderNameSpace
from castle.aigr_extra.scaffolding.callables import ScaffolderCallable
from castle.aigr_extra.scaffolding.protocols import ScaffolderProtocol, ScaffolderEventProtocol


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
    return ScaffolderCallable(m)


# ======================================================================
#  0 — Bootstrap: bucket collection and inheritance
# ======================================================================

def test_0a_ScaffolderNode_has_link_fields():
    """Base class defines link_fields."""
    k, a, l = ScaffolderNode._effective_buckets()
    assert 'parent' in l


def test_0b_ScaffolderNode_parent_not_in_kids():
    """Links are explicitly excluded from kids."""
    k, a, l = ScaffolderNode._effective_buckets()
    assert 'parent' not in k


def test_0c_ScaffolderNode_outer_ns_is_link():
    """outer_ns is part of link_fields."""
    k, a, l = ScaffolderNode._effective_buckets()
    assert 'outer_ns' in l


def test_0d_ScaffolderNode_ns_is_kid():
    """_ns is part of kid_fields (namespace children)."""
    k, a, l = ScaffolderNode._effective_buckets()
    assert '_ns' in k


def test_0e_ScaffolderCallable_inherits_ns_kid():
    """ScaffolderCallable inherits _ns from ScaffolderNode via MRO union."""
    k, a, l = ScaffolderCallable._effective_buckets()
    assert '_ns' in k


def test_0f_ScaffolderCallable_body_is_kid():
    """ScaffolderCallable declares body as a kid_field."""
    k, a, l = ScaffolderCallable._effective_buckets()
    assert 'body' in k


def test_0g_ScaffolderCallable_parameters_is_attr():
    """ScaffolderCallable declares parameters as an attr_field."""
    k, a, l = ScaffolderCallable._effective_buckets()
    assert 'parameters' in a


def test_0h_ScaffolderCallable_parameters_not_kid():
    """Parameters must NOT be in kids (they are attrs only)."""
    k, a, l = ScaffolderCallable._effective_buckets()
    assert 'parameters' not in k


def test_0i_ScaffolderCallable_inherits_parent_as_link():
    """Links are inherited through the hierarchy."""
    k, a, l = ScaffolderCallable._effective_buckets()
    assert 'parent' in l


def test_0j_link_never_in_kids_or_attrs():
    """Critical invariant: links are always disjoint from kids and attrs."""
    for cls in (ScaffolderNode, ScaffolderNameSpace, ScaffolderCallable, 
                ScaffolderProtocol, ScaffolderEventProtocol):
        k, a, l = cls._effective_buckets()
        assert k.isdisjoint(l), f"{cls.__name__}: overlap between kids and links: {k & l}"
        assert a.isdisjoint(l), f"{cls.__name__}: overlap between attrs and links: {a & l}"
        assert k.isdisjoint(a), f"{cls.__name__}: overlap between kids and attrs: {k & a}"


# ======================================================================
#  1 — kids() on a leaf node
# ======================================================================

def test_1a_leaf_kids_is_empty(leaf_node):
    """A leaf node has no structural children."""
    sn = ScaffolderNode(leaf_node)
    assert list(sn.kids()) == []


def test_1b_leaf_kids_returns_generator(leaf_node):
    """kids() returns a generator (lazy evaluation)."""
    import types
    sn = ScaffolderNode(leaf_node)
    assert isinstance(sn.kids(), types.GeneratorType)


# ======================================================================
#  2 — kids() on a flat namespace
# ======================================================================

def test_2a_flat_ns_kids_count(flat_ns):
    """Flat namespace yields correct number of children."""
    assert len(list(flat_ns.kids())) == 2


def test_2b_flat_ns_kids_are_AIGRNodes(flat_ns):
    """All yielded kids are AIGRNode instances."""
    for kid in flat_ns.kids():
        assert isinstance(kid, aigr.AIGRNode)


def test_2c_flat_ns_kids_names(flat_ns):
    """kids() yields the correct named children."""
    names = {str(k.name) for k in flat_ns.kids()}
    assert names == {'alpha', 'beta'}


def test_2d_parent_not_in_kids(flat_ns):
    """Link fields (like parent) are never yielded by kids()."""
    kids = list(flat_ns.kids())
    # parent field value is None — should not appear
    for kid in kids:
        assert kid is not flat_ns.node.parent


# ======================================================================
#  3 — kids() on a nested namespace (one level deep)
# ======================================================================

def test_3a_nested_direct_kids_count(nested_ns):
    """Root has 2 direct children: flat and sub (the Scope itself)."""
    assert len(list(nested_ns.kids())) == 2


def test_3b_nested_direct_kid_types(nested_ns):
    """kids() returns the correct types of children."""
    kids = list(nested_ns.kids())
    types_found = {type(k).__name__ for k in kids}
    assert types_found == {'NamedNode', 'Scope'}


def test_3c_scope_itself_has_kids(nested_ns):
    """Nested Scope nodes also correctly yield their own kids."""
    scope_kids = [k for k in nested_ns.kids() if isinstance(k, Scope)]
    assert len(scope_kids) == 1
    scope_wrapper = ScaffolderNameSpace(scope_kids[0])
    assert len(list(scope_wrapper.kids())) == 2


# ======================================================================
#  9 — _attrs() — attribute-like children (NOT traversed by kids)
# ======================================================================

def test_9c_attrs_yields_parameters():
    """_attrs() yields TypedParameter nodes when declared."""
    from castle.aigr.aid import TypedParameter
    from castle.aigr import types as aigr_types
    from castle.aigr.statements.callables import Method
    from castle.aigr.statements.compounds import Body
    
    p = TypedParameter(name=ID.Def('x'), type=aigr_types.int)
    m = Method(name=ID.Def('f'), parameters=(p,), body=Body())
    sc = ScaffolderCallable(m)
    attrs = list(sc._attrs())
    assert p in attrs


def test_9d_attrs_not_in_kids(method_node):
    """Critical: attrs and kids() must be disjoint."""
    kids  = set(id(n) for n in method_node.kids())
    attrs = set(id(n) for n in method_node._attrs())
    assert kids.isdisjoint(attrs)


# ======================================================================
#  NEW TESTS — Metadata Declaration Validation (Forward-Looking)
# ======================================================================

def test_all_scaffolder_subclasses_declare_buckets():
    """CRITICAL: All Scaffolder subclasses must explicitly declare field buckets.
    
    This test ensures that new/future AIGRNode types don't forget to declare
    _kid_fields, _attr_fields, or _link_fields. Without explicit declarations,
    the system silently falls back to inherited defaults, which is a common bug
    and defeats the purpose of the metadata system.
    
    When adding a new Scaffolder subclass, you MUST declare at least one bucket:
    
        class ScaffolderMyNode(ScaffolderNode):
            _kid_fields: frozenset[str] = frozenset({'some_field'})
            # and/or:
            _attr_fields: frozenset[str] = frozenset({'other_field'})
            # and/or:
            _link_fields: frozenset[str] = frozenset({'link_field'})
    
    If you only inherit without declaring, this test will FAIL.
    """
    scaffolder_classes = [
        ScaffolderNode,
        ScaffolderNameSpace,
        ScaffolderCallable,
        ScaffolderProtocol,
        ScaffolderEventProtocol,
    ]
    
    for cls in scaffolder_classes:
        # Each subclass (except base ScaffolderNode) must declare at least one bucket
        if cls is ScaffolderNode:
            continue  # Base class defines defaults
        
        has_own_kid_fields = '_kid_fields' in cls.__dict__
        has_own_attr_fields = '_attr_fields' in cls.__dict__
        has_own_link_fields = '_link_fields' in cls.__dict__
        
        has_own_declaration = has_own_kid_fields or has_own_attr_fields or has_own_link_fields
        
        assert has_own_declaration, (
            f"FAIL: {cls.__name__} must explicitly declare at least one of: "
            f"_kid_fields, _attr_fields, _link_fields. "
            f"Do not rely only on inherited defaults — this defeats the metadata system! "
            f"Add explicit declarations to {cls.__name__}, even if empty."
        )


def test_scaffolder_buckets_are_disjoint():
    """Verify that kids, attrs, and links never overlap within any Scaffolder class."""
    scaffolder_classes = [
        ScaffolderNode,
        ScaffolderNameSpace,
        ScaffolderCallable,
        ScaffolderProtocol,
        ScaffolderEventProtocol,
    ]
    
    for cls in scaffolder_classes:
        k, a, l = cls._effective_buckets()
        
        assert k.isdisjoint(a), (
            f"{cls.__name__}: Field(s) appear in both _kid_fields and _attr_fields: {k & a}. "
            f"This is a configuration error — fix {cls.__name__}._*_fields declarations."
        )
        assert k.isdisjoint(l), (
            f"{cls.__name__}: Field(s) appear in both _kid_fields and _link_fields: {k & l}. "
            f"This is a configuration error — fix {cls.__name__}._*_fields declarations."
        )
        assert a.isdisjoint(l), (
            f"{cls.__name__}: Field(s) appear in both _attr_fields and _link_fields: {a & l}. "
            f"This is a configuration error — fix {cls.__name__}._*_fields declarations."
        )
