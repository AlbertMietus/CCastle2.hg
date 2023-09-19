# (C) Albert Mietus, 2022, 2023. Part of Castle/CCastle project
"""
These tests only exist to show we can run a tests in RPy
"""
import logging; logger = logging.getLogger(__name__)
import pytest

from . import *
from castle.writers import RPy

def test_run():
    print(f"{__name__}::")

def test_import():
    print(f"{__name__}:: {RPy.__dict__}")
