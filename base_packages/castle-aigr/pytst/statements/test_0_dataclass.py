# (C) Albert Mietus, 2024. Part of Castle/CCastle project

"""Just verify all @dataclasses are dataclasses ... Mostly for MutMut"""

import pytest

from castle import aigr

from .. import verifyisDataClass

def test_callables_are_dataclass():
    for cls in (
            aigr.statements.callables._callable,
            aigr.statements.callables._Named_callable,
            aigr.statements.callables.Method,
            aigr.Method,
            ):
        verifyisDataClass(cls)

def test_long_callables_are_short_callables():
    """A class inport as aigr.NAME and aigr.path.to.NAME is tje same thing"""
    assert aigr.statements.callables.Method is aigr.Method

