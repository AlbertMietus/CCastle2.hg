# (C) Albert Mietus, 2025,2026- Part of Castle/CCastle project
import logging; logger = logging.getLogger(__name__)
import typing as PTH                                                           # Python TypeHints
import pytest

from pprint import pprint, pformat
from importlib import resources

from . import *
from castle.readers.ladon.aigr import FileNS, ScaffolderFileNS
from castle import aigr
from castle.aigr.namespaces import _NameSpace
from castle.aigr_extra.scaffolding import ScaffolderNameSpace

@pytest.mark.xfail(reason="Dot-on-Horizon: elemental HelloWorld")
def test_1_file_as_txt(castle_parser):
    module, file  = "CastleCode.elemental", "HelloWorld.Castle"
    with resources.open_text( module, file) as f:
        logger.debug("Going to read %s", f.name)
        eHW = castle_parser(f.read())

    assert isinstance(eHW, FileNS), "Oke for now -- will become Source_NS"
    wrapped: ScaffolderNameSpace = ScaffolderFileNS(eHW)
    dottedNames: tuple = wrapped.search_dottedNames()
    logger.info("XXX found dottedNames: %s", dottedNames)

    verify_namespace_have_outer_ns(dottedNames, wrapped)

    # verify parameters ('label') is in NS
    HW_method= wrapped.search('Elemental_HelloWorld.HelloWorld')
    assert isinstance(HW_method, aigr.Method)
    wrapped_method = ScaffolderNameSpace(HW_method)
    parm = wrapped_method.findNode('label')
    assert isinstance(parm, aigr.TypedParameter), f"Parameter `label` should be in the namespace, but is {parm=}"

    # Manually check the AIGR
    pprint(eHW, compact=True)


def verify_namespace_have_outer_ns(dottedNames: tuple[str, ...], wrapped_top: ScaffolderNameSpace)->None:
    for name in (name for name in dottedNames if isinstance(name, aigr.NamedSpace)):
        dad_name = name.rsplit('.', maxsplit=1)[0]
        if dad_name == name: dad_name= ""
        logger.info("name=%s, dad_name=%s", name, dad_name)

        node, dad = wrapped_top.search(name), wrapped_top.search(dad_name) if dad_name != "" else wrapped_top.node
        node, dad = PTH.cast(_NameSpace, node), PTH.cast(_NameSpace, dad) # Fix for linter: node & dad are a _NameSpace
        logger.info("node=%s\n\t dad=%s", node, dad)

        assert node.outer_ns == dad, f"outer_ns of {name=} isn't {dad_name=}: {dad=}"

