# (C) Albert Mietus, 2023. Part of Castle/CCastle project
"""Test the 'basic' (base) AIGR TestDoubles"""

import pytest

import castle.aigr as aigr

# Now that the _RootProtocol is gone, th this TestDoubles may be obsolete.
# Still we need a test, are pytest --running 0 tests- will fail.

def test_dummy():
    assert True
