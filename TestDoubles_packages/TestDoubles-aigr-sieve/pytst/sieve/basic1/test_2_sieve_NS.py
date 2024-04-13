# (C) Albert Mietus, 2024 Part of Castle/CCastle project
"""Test the AIGR TestDoubles of the BASIC1 Sieve protocols
   documented in :
       *  .../TestDoubles_packages/TestDoubles-aigr-sieve/doc/basic1-import.puml
       *  http://docideas.mietus.nl/en/default/CCastle/4.Blog/b.TheSieve.html#the-design
"""

import logging; logger = logging.getLogger(__name__)
import pytest

from castle.aigr import NameSpace
from castle import aigr
from castle.TESTDOUBLES.aigr.sieve.basic1 import namespaces

moat_files = ('protocols', 'interfaces')
comp_files = ('generator', 'sieve', 'finder')

def test_0_all_sieveProtocols_exist():
    for ns in (namespaces.interfaces, namespaces.protocols):
        assert isinstance(ns, aigr.Source_NS)
    for ns in (getattr(namespaces, name) for name in moat_files): # same loop as above!
        assert isinstance(ns, aigr.Source_NS)
    for ns in (namespaces.comps[name] for name in comp_files):
        assert isinstance(ns, aigr.Source_NS)
    assert isinstance(namespaces.main, aigr.Source_NS)



def test_1_comps_imports_moats():
    for (comp_name, comp_ns) in ((name, namespaces.comps[name]) for name in comp_files):
        logger.debug(f"comp_name={comp_name}, comp_ns={comp_ns}")
        for moat_name in moat_files:
            moat_node = comp_ns.findNode(moat_name)
            logger.debug(f"moat_name={moat_name}, moat_node={moat_node}")
            verify_nodeIsNS_withName(moat_node, moat_name)

def test_2a_main_imports_moats():
    """ main imports <interfaces>, <protocols> and (see test_2b...)"""
    for name in moat_files:
        ns_node = namespaces.main.findNode(name)
        verify_nodeIsNS_withName(ns_node, name)

def test_2b_main_imports_implements_optionally():
    """(see test_2a...) and optionally the 3 components"""
    log_prefix =f"namespaces._OPT_MAIN_IMPORTS_COMPS={namespaces._OPT_MAIN_IMPORTS_COMPS}..."
    if namespaces._OPT_MAIN_IMPORTS_COMPS:
        logger.info(log_prefix +f"check the comp_files ({comp_files})")
        for name in comp_files:
            ns_node = namespaces.main.findNode(name)
            verify_nodeIsNS_withName(ns_node, name)
    else:
        logger.info(log_prefix +f"skip check on comp_files")



def verify_nodeIsNS_withName(node, name:str):
    assert isinstance(node, aigr.NameSpace)
    assert node.name == name
