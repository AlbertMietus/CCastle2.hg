# (C) Albert Mietus, 2025,2026- Part of Castle/CCastle project
import logging; logger = logging.getLogger(__name__)
import typing as PTH                                                           # Python TypeHints
import pytest

from importlib import resources

from . import *
from castle.readers.ladon.aigr import FileNS, ScaffolderFileNS
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

    # verify that eventy "dottedName" has the correct outer_ns
    for name in dottedNames:
        dad_name = name.rsplit('.', maxsplit=1)[0]
        if dad_name == name: dad_name= ""
        logger.info("name=%s, dad_name=%s", name, dad_name)

        node, dad = wrapped.search(name), wrapped.search(dad_name) if dad_name != "" else eHW
        node, dad = PTH.cast(_NameSpace, node), PTH.cast(_NameSpace, dad) # Fix for linter: node & dad are a _NameSpace
        logger.info("node=%s\n\t dad_%s", node, dad)

        assert node.outer_ns == dad, f"outer_ns of {name=} isn't {dad_name=}: {dad=}"


