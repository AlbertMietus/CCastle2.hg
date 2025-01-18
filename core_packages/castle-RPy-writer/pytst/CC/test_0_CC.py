# (C) Albert Mietus, 2025. Part of Castle/CCastle project

import pytest
from castle.writers.RPy import CC

def test_import_CC():
    "Just read something ..."
    assert CC._version == "CC-0.0"
