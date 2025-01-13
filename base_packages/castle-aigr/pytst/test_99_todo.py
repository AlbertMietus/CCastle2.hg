# (C) Albert Mietus, 2025 Part of CCastle project

import logging; logger = logging.getLogger(__name__)
import pytest
from dataclasses import dataclass, KW_ONLY
from dataclasses import field as dc_field

from castle.aigr.namespaces import _hasScope

@dataclass
class _Mock_with_Scope(_hasScope):
    pass
@dataclass
class Mock_with_parameters(_Mock_with_Scope):
    parameters : tuple[int, ...]       = dc_field(default_factory=tuple)

@dataclass
class Mock_without_parameters(_Mock_with_Scope):
    pass



@pytest.mark.skip("Todo: 'Coverage for castle/aigr/namespaces.py: 92%' _hasScope._register_parameters()")
def test_hasScope_auto_register():
    m1 = Mock_without_parameters()
    m2 = Mock_with_parameters()
    assert False
