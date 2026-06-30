# (C) Albert Mietus, 2025,2026- Part of Castle/CCastle project
import logging; logger = logging.getLogger(__name__)
import typing as PTH                                                           # Python TypeHints
import pytest



from . import *
from castle import aigr
from castle.aigr.namespaces import _NameSpace
from castle.aigr.tools.scaffolding import ScaffolderNameSpace
from castle.readers.ladon.loaders.simple_loader import PyModuleLoader


@pytest.mark.xfail(reason="Dot-on-Horizon: elemental HelloWorld")
def test_1_file_as_txt():

    loader=PyModuleLoader(module="CastleCode.elemental", file="HelloWorld.Castle")
    eHW = loader.parse()
    assert isinstance(eHW, aigr.Source_NS)

    wrapped: ScaffolderNameSpace = ScaffolderNameSpace(eHW)
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
    from pprint import pformat
    logger.info(pformat(eHW))


def verify_namespace_have_outer_ns(dottedNames: tuple[str, ...], wrapped_top: ScaffolderNameSpace)->None:
    for name in (name for name in dottedNames if isinstance(name, aigr.NamedSpace)):
        dad_name = name.rsplit('.', maxsplit=1)[0]
        if dad_name == name: dad_name= ""
        logger.info("name=%s, dad_name=%s", name, dad_name)

        node, dad = wrapped_top.search(name), wrapped_top.search(dad_name) if dad_name != "" else wrapped_top.node
        node, dad = PTH.cast(_NameSpace, node), PTH.cast(_NameSpace, dad) # Fix for linter: node & dad are a _NameSpace
        logger.info("node=%s\n\t dad=%s", node, dad)

        assert node.outer_ns == dad, f"outer_ns of {name=} isn't {dad_name=}: {dad=}"

