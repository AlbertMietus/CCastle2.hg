# (C) Albert Mietus, 2025. Part of Castle/CCastle project

import pytest
from castle.writers import RPy_buildin

def test_import_CC():
    "Just read something ..."
    assert RPy_buildin._version == "CC-0.0"
