# (C) Albert Mietus, 2025. Part of Castle/CCastle project
"""See ../../doc/mocks/eTables.rst"""


import logging; logger = logging.getLogger(__name__)
import pytest

from castle import aigr
from castle.aigr import ID

from .. import chainDict_renderer
from ..verify import *

from .demoTables import * # fixtures and `Expected-strings`

### DispatchTable(s): See remark on EventDispatchTable

def DEAD_test_simpeTable(simpleTable, chainDict_renderer):
    result = chainDict_renderer.render(simpleTable)
    #print_out(result, label='simpleTable')
    verify_line_by_line(Expected_4_simpleTable, result)


def DEAD_test_childTable(childTable, chainDict_renderer):
    result = chainDict_renderer.render(childTable)
    #print_out(result, label='childTable')
    verify_line_by_line(Expected_4_childTable, result)
