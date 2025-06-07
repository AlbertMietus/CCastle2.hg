# (C) Albert Mietus, 2025. Part of Castle/CCastle project
# created with codeAI

import pytest

def pytest_addoption(parser):
    parser.addoption(
        "--runslow", action="store_true", default=False, help="Run slow tests"
    )

def pytest_configure(config):
    config.addinivalue_line("markers", "slow: mark test as slow")

def pytest_collection_modifyitems(config, items):
    if not config.getoption("--runslow"):
        skip_slow = pytest.mark.skip(reason="Skipping slow tests (use --runslow to include)")
        for item in items:
            if "slow" in item.keywords:
                item.add_marker(skip_slow)
