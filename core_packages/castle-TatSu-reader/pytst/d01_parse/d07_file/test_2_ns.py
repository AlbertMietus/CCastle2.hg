# (C) Albert Mietus, 2025,2026. Part of Castle/CCastle project
import logging; logger = logging.getLogger(__name__)
import pytest

from castle import aigr

from . import *

@pytest.mark.xfail
def test_1_outerNS_of_Node_in_NamedSpace_is_NamedSpace(load_and_wrap):
    wrapped_source = load_and_wrap("file1.Castle")
    comp = wrapped_source.findNode('One'); assert isinstance(comp, aigr.ComponentImplementation)
    assert comp.outer_ns == wrapped_source.node, "XXX"



