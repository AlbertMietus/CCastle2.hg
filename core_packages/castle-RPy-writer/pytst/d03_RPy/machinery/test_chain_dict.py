# (C) Albert Mietus, 2025. Part of Castle/CCastle project

import logging; logger = logging.getLogger(__name__)
import typing as PTH                                                                                  # Python TypeHints

import pytest

from castle.aigr import ID
from castle.writers.RPy.writer.machinery import Machinery
from castle.writers.RPy.writer.machinery import M_DC_chained_dict
from castle.writers.RPy.aigr import EventDispatchTable

from .. import my_renderer
from .. import verify_line_by_line, print_out

from .fixtures import machinery
from .mocks.tables import *

def test_0_hint_gives_chainned_dict_machinery(machinery):
    explicit = M_DC_chained_dict()
    assert type(machinery) is type(explicit)


def test_1_render_a_single_table(machinery, my_renderer, singleTable):
    """See CastleCode in mocks: a eTable without a parentTable"""
    table, expected = singleTable
    blck = machinery.render_EventDispatchTable(renderer=my_renderer, node=table)
    verify_line_by_line(expected, str(blck))

def test_2_render_childTable_a_single_table(machinery, my_renderer, childTable):
    """See CastleCode in mocks: a eTable with a parentTable"""
    table, expected = childTable
    blck = machinery.render_EventDispatchTable(renderer=my_renderer, node=table)
    verify_line_by_line(expected, str(blck))

