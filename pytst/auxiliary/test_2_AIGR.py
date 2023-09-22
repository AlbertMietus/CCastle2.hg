# (C) Albert Mietus, 2023. Part of Castle/CCastle project

from castle.auxiliary import AIGR

class Demo(AIGR):
    pass

def test_noAIGR():
    try:
        AIGR()
        assert False , "shouldn't be able to initiate an AIGR directly"
    except NotImplementedError:
        pass

def test_AIGR_sub():
    d = Demo()
    assert isinstance(d, AIGR)
