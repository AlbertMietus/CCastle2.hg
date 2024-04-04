# (C) Albert Mietus, 2023. Part of Castle/CCastle project

import pytest

from castle.aigr import AIGR

class Demo(AIGR):
    pass

def test_noAIGR():
    try:
        AIGR()
        assert False , "shouldn't be able to initiate an AIGR directly"                   # pragma: no cover
    except NotImplementedError:
        pass

def test_AIGR_sub():
    d = Demo()
    assert isinstance(d, AIGR)

@pytest.mark.skip("The ID comes A bit later")
def test_ID_many():
    assert False, """Make an ID class in AIGR (or generic). ((also see NamedNode))

    It holds the name in AIGR -nodes ipv de str class. Model it a bit like pathlib.Path

    We should have atomic_ID, relative_ID, DottedName_ID, ect
    """
