# (C) Albert Mietus, 2024. Part of Castle/CCastle project

"""Just verify all @dataclasses are dataclasses ... Mostly for MutMut"""

import pytest
import dataclasses

from castle.aigr import machinery

def isDataClass(cls):
    assert dataclasses.is_dataclass(cls) # This will also pass when cls inherits from a dataclass
    my_init = getattr(cls, '__init__')
    inherited_init = getattr(cls.mro()[1], '__init__')
    assert my_init is not inherited_init, f"Probably you subclasses a dataclass, but forgot @dataclass for {cls}"


def test_dataclass_all():
    for cls in (machinery.machinery,
                machinery.send_proto,
                machinery.sendStream,
                machinery.sendData,
                machinery.sendEvent,
                machinery.connection,
                machinery.DispatchTable,
                machinery.eDispatchTable,
                ):
        isDataClass(cls)
