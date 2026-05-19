# (C) Albert Mietus 2026. Part of Castle/CCastle project

import logging; logger = logging.getLogger(__name__)
import pytest

@pytest.mark.skip(reason="ToDo: after we support plugin with node/scaffolder pairs")
def test_999_plugin_with_nodeSsaffolder_pair_shouldBe_found_withAuto():
    """When AutoScaffolder uses a cache, and a plugin is loaded after that, the correct Scaffolder should be found"""
    assert False
