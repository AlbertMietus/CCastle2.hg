# (C) Albert Mietus, 2023,2024 Part of Castle/CCastle project
"""Test the AIGR TestDoubles of the Sieve NameSpaces
   See: http://docideas.mietus.nl/en/default/CCastle/4.Blog/b.TheSieve.html#the-design
   See file:///Users/albert/work/DocIdeas,hg/__result/html/CCastle/HACK/DocParts/Design/231016_NS.html
   (not published yet -- see .../DocParts/Design/231016_NS.rst for source)"""

import logging; logger = logging.getLogger(__name__)
import pytest

from castle.TESTDOUBLES.aigr.sieve import namespaces
from castle.TESTDOUBLES.aigr.base import base as base_ns

from . import verify_NS

def test_slow_start_has_SlowStart():
    ns = namespaces.slow_start
    verify_NS(ns, "slow_start", ["SlowStart"])

def test_start_sieve_has_StartSieve():
    ns = namespaces.start_sieve
    verify_NS(ns, "start_sieve", ["StartSieve"])

def test_simple_sieve_has_SimpleSieve_and_SpecialiseGeneric():
    ns = namespaces.simple_sieve
    #verify_NS(ns, "simple_sieve", ["SlowStart_1", "SimpleSieve"])
    verify_NS(ns, "simple_sieve", ["SimpleSieve"])


def test_top():
    ns = namespaces.top
    verify_NS(ns, "top", as_name='TheSieve', registered_names=('start_sieve', 'slow_start', 'simple_sieve'))
    verify_NS(ns, "top", as_name='TheSieve', registered_names=('base',))


def test_all_NS_base_in_start_sieve():
    nss = namespaces.start_sieve.all_NS()
    for n,ns in nss.items(): print(f'name={n}: {ns.name} // {ns}')
    assert nss['base'] is base_ns
