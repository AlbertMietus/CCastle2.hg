# (C) Albert Mietus 2026, Part of Castle/CCastle project

import logging; logger = logging.getLogger(__name__)
import pytest

import typing as PTH                                        # Python TypeHints


from castle.aigr_extra.scaffolding.node import ScaffolderNode


@pytest.fixture
def scaffolder_node_classes()-> list[type[ScaffolderNode]]:
    """Find (dynamicly) all descendants of ScaffolderNode
       That is, all the Scaffolders that need to set metadata fields """

    scaffolders = [ScaffolderNode] # ScaffolderNode is the base
    for cls in scaffolders:
        for subclass in cls.__subclasses__():
            if subclass not in scaffolders:
                scaffolders.append(subclass)

    logging.debug(f"Using {len(scaffolders)} {scaffolders=}")
    return scaffolders


