# (C) Albert Mietus, 2023-2024. Part of Castle/CCastle project

from __future__ import annotations # Postponed evaluation of annotations

import typing as PTH                                                                                 # Python TypeHints
from dataclasses import dataclass, KW_ONLY
from dataclasses import field as dc_field

from .AIGR import AIGR

@dataclass
class _types(AIGR):
    """A type in the AIGR is unique object, not a type, that represents the type.

    We use the name of the type (as string) as well as the sub-type of `_types` to make it unique.

    So, the build-in-type 'foo' is a instance of `CC_buildin` with "foo" as value (stored in ``.represents``).
    A user defined-type in never a `CC_buildin`, (but a `CC_user` instance) and will never conflict"""

    represents : str # the name of the AIGR-type


class CC_buildin(_types): pass
class CC_Number(AIGR): pass
class CC_buildinNumber(CC_buildin, CC_Number): pass
class CC_user(_types): pass

int 	= CC_buildinNumber('int')                                                 # pragma: no mutate
float	= CC_buildinNumber('float')                                               # pragma: no mutate

string 	= CC_buildin('string')                                                    # pragma: no mutate
boolean = CC_buildin('boolean')


