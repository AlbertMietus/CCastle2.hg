# (C) Albert Mietus, 2022, 2023. Part of Castle/CCastle project

from . import * # CCompare

from castle.writers.CC2Cpy.CCbase import * # Some generic types

LOG_ALL=True

def test_0_trival_same():
    abc='A B C'
    assert CCompare(abc,abc, log_all=LOG_ALL)

def test_1_not_same():
    abc='A B C'
    assert False == CCompare(abc,abc[::-1], log_all=LOG_ALL)

def test_2_diff_length():
    abc=' A B C '
    assert False == CCompare(abc, abc+abc, log_all=LOG_ALL)
    assert False == CCompare(abc+abc, abc, log_all=LOG_ALL)

def test_4_logvariants():
    abc=' A B C '
    assert CCompare(abc,abc, log=False, log_all=False)
    assert CCompare(abc,abc, log=False, log_all=True) # log=.. will be overiden
    assert CCompare(abc,abc, log=True , log_all=False)
    assert CCompare(abc,abc, log=True,  log_all=True)

def test_5_types():
    """Test some trivial (type-hints) types; mostly by just using them"""

    assert CC_TypedParameter('test', int).type is int
