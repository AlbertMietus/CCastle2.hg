# (C) Albert Mietus, 2025,2026. Part of Castle/CCastle project
import logging; logger = logging.getLogger(__name__)
import pytest

from castle import aigr
from castle.readers.parser import CastleParser

@pytest.fixture
def castle_parser():
    parser = CastleParser()
    return parser.parse


def verify_parms_tuple(parms, length):
    assert isinstance(parms, tuple), f"Expecting a tuple, got: {type(parms)} :: {parms}"
    assert len(parms) == length,     f"Expecting {length} parameter(s), got {len(parms)}"

def verify_parm(parm, name, type_, check_optional=False):
    assert isinstance(parm, aigr.TypedParameter), f"Expecting a TypedParameter, got: {type(parm)} :: {parm}"
    assert isinstance(parm.name, aigr.ID) and parm.name == name, f"Expecting {aigr.ID(name)=}, got {parm.name!r}"
    assert parm.type == type_, f"Expecting type {type_=!r}, got {parm.type!r} for {parm=}"
    assert isinstance(parm.type, aigr.ID)
    assert isinstance(parm.type.context, aigr.base.names.Ref) # Note aigr.base.names.Ref) != aigr.ID.Ref
    if check_optional:
        assert False, "optional parameters not yet supported in AIGR"

