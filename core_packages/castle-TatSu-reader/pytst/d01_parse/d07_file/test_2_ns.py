# (C) Albert Mietus, 2025,2026. Part of Castle/CCastle project
import logging; logger = logging.getLogger(__name__)
import pytest

from castle import aigr

from . import *

def test_1_outerNS_of_Node_in_NamedSpace_is_NamedSpace(load_and_wrap):
    wrapped_source = load_and_wrap("file1.Castle")
    comp = wrapped_source.findNode('One'); assert isinstance(comp, aigr.ComponentImplementation)
    assert comp.outer_ns == wrapped_source.node, "a NS in a NS has an outer_ns, that is the NS"



