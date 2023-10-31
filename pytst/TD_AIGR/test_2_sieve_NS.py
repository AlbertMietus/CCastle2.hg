# (C) Albert Mietus, 2023. Part of Castle/CCastle project
"""Test AIGR representation of the TheSieve protocols
   See file:///Users/albert/work/DocIdeas,hg/__result/html/CCastle/HACK/DocParts/Design/231016_NS.html
    (not published yet -- see .../DocParts/Design/231016_NS.rst for source)
"""

import pytest

import castle.aigr as aigr
from TestDoubles.AIGR.sieve import namespaces
from TestDoubles.AIGR.base import base as base_ns

def verify_NS(ns, name, registered_names, as_name=None):
    if as_name is None: as_name=name
    assert ns.name == as_name
    for n in registered_names:
        if isinstance(n, (list, tuple)):
            #This is hardly/not used: be we support `import n[1] as n[0]`
            assert len(n) == 2
            name, asName = n[1], n[0]
        else:
            name, asName = n, n
        assert ns.getID(asName).name == name

def test_start_sieve():
    ns = namespaces.start_sieve
    verify_NS(ns, "start_sieve", ["StartSieve"])

def test_slow_start():
    ns = namespaces.slow_start
    verify_NS(ns, "slow_start", ["SlowStart"])

def test_simple_sieve():
    ns = namespaces.simple_sieve
    verify_NS(ns, "simple_sieve", ["SlowStart_1", "SimpleSieve"])

def test_top():
    ns = namespaces.top
    verify_NS(ns, "top", as_name='TheSieve', registered_names=('start_sieve', 'slow_start', 'simple_sieve'))
    verify_NS(ns, "top", as_name='TheSieve', registered_names=('base',))


def test_all_NS_base_in_start_sieve():
    nss = namespaces.start_sieve.all_NS()
    for n,ns in nss.items(): print(f'name={n}: {ns.name} // {ns}')
    assert nss['base'] is base_ns
