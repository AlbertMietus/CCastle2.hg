 # (C) Albert Mietus, 2024. Part of Castle/CCastle project

import logging; logger = logging.getLogger(__name__)
import pytest
from .. import  Dummy, verifyMark, verifyKids

from castle import aigr
from castle.aigr import Method, ID

def verify_NamedCallableTypes(c):
    logger.info("verify_NamedCallable: %s", c)
    assert isinstance(c.name, ID)
    assert isinstance(c.parameters, tuple)
    assert isinstance(c.body, (aigr.Body, type(None)))
    #assert isinstance(c.returns,  ... )  # XXX ToDo: # See test_9_returnType (merge once)
    verifyKids(c)


def test_1_MethodWithName():
    m = Method(ID('test'))
    verify_NamedCallableTypes(m)
    assert m.name == 'test'


@pytest.mark.skip("returns-type of callable needs to be designed, as is ``aigr.Type``")
def test_9_returnType():
    m = Method(ID('test'))
    assert m.returns is not None
