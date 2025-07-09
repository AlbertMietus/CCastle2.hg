# (C) Albert Mietus, 2024. Part of Castle/CCastle project

"""Just verify all @dataclasses are dataclasses ... Mostly for MutMut"""

import pytest

from castle.aigr import machinery

from .. import verifyisDataClass

def test_dataclass_all():
    for cls in (
            machinery._machinery,
            machinery._send_proto,
            machinery.sendStream,
            machinery.sendData,
            machinery.sendEvent,
            machinery.connection,
            ):
        verifyisDataClass(cls)

