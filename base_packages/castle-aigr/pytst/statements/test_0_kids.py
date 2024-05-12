# (C) Albert Mietus, 2024. Part of Castle/CCastle project

"""Verify multiple statements has kids :-)"""

import pytest
from .. import Dummy, verifyKids
from castle.aigr import statements

def test_kids_VoidCall():
    s = statements.VoidCall(Dummy("not a call, but it works for kids"))
    verifyKids(s)


