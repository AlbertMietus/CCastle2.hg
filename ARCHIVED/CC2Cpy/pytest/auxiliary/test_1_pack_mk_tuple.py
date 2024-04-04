# (C) Albert Mietus, 2022, 2023. Part of Castle/CCastle project

from castle.auxiliary.pack import mk_tuple

def test_mk_tuple():
    assert mk_tuple(1)    == (1,)
    assert mk_tuple((1,)) == (1,)
    assert mk_tuple([1,]) == (1,)
    assert mk_tuple(None) == ()
