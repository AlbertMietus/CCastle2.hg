# (C) Albert Mietus, 2023. Part of Castle/CCastle project
"""
These tests only exist to show we can run a tests in RPy
"""
import logging; logger = logging.getLogger(__name__)
import pytest

from . import *
from castle.writers import RPy

@pytest.fixture
def proto_template():
    return RPy.Template("protocol.jinja2")

@pytest.mark.xfail
def test_0(proto_template):
    out = proto_template.render()
    assert False, out
