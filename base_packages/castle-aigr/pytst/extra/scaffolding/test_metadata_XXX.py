# (C) Albert Mietus 2026, Part of Castle/CCastle project
# Partialy made by CodeAI: github-copilot: Claude Haiku 4.5

"""Tests for ScaffolderNode field bucket metadata and kids()/attrs() functionality.

   This test file ensures that:
   1. Field bucket metadata is correctly declared for all Scaffolder subclasses
   2. The kids() method correctly yields structural children
   3. The _attrs() method correctly yields attribute-like metadata

.. seealso:: `test_4z_meta_futurecheck.py` -- did future nodes set the metadata"""

if False: # ScaffolderNode._effective_buckets() is gone. Copy from castle/aigr_extra/scaffolding/node.py
        @classmethod
        def _effective_buckets(cls) -> tuple[frozenset[str], frozenset[str], frozenset[str]]:
            """Return (kid_fields, attr_fields, link_fields) after MRO-merging and
            conflict resolution: link always wins over kid/attr for the same name."""
            links = cls._collect_field_bucket('_link_fields')
            kids  = cls._collect_field_bucket('_kid_fields')  - links
            attrs = cls._collect_field_bucket('_attr_fields') - links

            conflict = kids & attrs # Names in both kids AND attrs (within the same class) is a mistake.
            if conflict:
                logger.error(
                    "%s: field(s) %s appear in both _kid_fields and _attr_fields — "
                    "treating as _kid_fields. Fix the bucket declarations.",
                    cls.__name__, conflict,
                )
                attrs = attrs - conflict

            return kids, attrs, links



import logging; logger = logging.getLogger(__name__)
import pytest

from castle import aigr
from castle.aigr import ID
from castle.aigr.namespaces import Scope
from castle.aigr_extra.scaffolding.node import ScaffolderNode
from castle.aigr_extra.scaffolding.namespaces import ScaffolderNameSpace
from castle.aigr_extra.scaffolding.callables import ScaffolderCallable
from castle.aigr_extra.scaffolding.protocols import ScaffolderProtocol, ScaffolderEventProtocol

from . import *



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



