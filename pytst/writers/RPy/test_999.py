# (C) Albert Mietus, 2022, 2023. Part of Castle/CCastle project
"""
These tests only exist to show we can run a tests in RPy
"""
import logging; logger = logging.getLogger(__name__)
import pytest

@pytest.mark.skip(reason="Todo, soon")
def test_todo_soon():
    assert False, "At the moment, no test/code are on the short-todo list"

@pytest.mark.skip(reason="Todo, later")
def test_todo_eventually():
    assert False, "Generate the 'The Sieve in RPython' code-files"
