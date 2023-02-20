# (C) Albert Mietus, 2022, 2023. Part of Castle/CCastle project

import logging; logger = logging.getLogger(__name__)
import pytest
from . import * # CCompare

from castle.writers.CC2Cpy.Component import * # CC_B_ComponentClass


ref_sieveMethods="""\
CC_B_methodHandler cc_S_Sieve_methods[] = {
 (CC_B_methodHandler)CC_Mi_error,
 (CC_B_methodHandler)CC_Mc_New,
 (CC_B_methodHandler)CC_Mi_error,
 (CC_B_methodHandler)CC_Mi_Sieve__init,
};
"""

ref_TryPort="""\
CC_B_eventHandler cc_S_Sieve_try[] = {
  (CC_B_eventHandler)CC_Mi_error,
  (CC_B_eventHandler)CC_Mi_error,
  (CC_B_eventHandler)CC_Mi_error,
  (CC_B_eventHandler)CC_Mi_error,
  (CC_B_eventHandler)CC_Mi_error,
  (CC_B_eventHandler)CC_Mi_error,
  (CC_B_eventHandler)CC_E_Sieve__SimpleSieve_input__try,
};
"""

#XXX move to common?
from .test_9_genSieve import *

@pytest.mark.skip
def test_SieveMethods(sieveClass):
    dispatch_table= sieveClass.render_Fill_MethodHandlers()
    logger.debug("\n%s\n", dispatch_table)
    assert CCompare(ref_sieveMethods,dispatch_table, log_all=True)

TRY="fill_in_later"
@pytest.mark.skip
def test_TryPortHandlers(sieveClass):
    dispatch_table= sieveClass.render_Fill_PortHandlers(TRY)
    logger.debug("\n%s\n", dispatch_table)
    assert CCompare(ref_TryPorr, dispatch_table, log_all=True)


@pytest.mark.skip(reason="More CompStruct-tests are needed")
def test_more(): pass
