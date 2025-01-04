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

    So, the build-in-type 'foo' is a instance of `_buildin` with "foo" as value (stored in ``.represents``).
    A user defined-type in never a `_buildin`, (but a `_user` instance) and will never conflict"""

    represents : str # the 'name of the AIGR-type


class _buildin(_types): pass
class _Number(AIGR): pass
class _buildinNumber(_buildin, _Number): """For Now, we use python types as reference, as they are uniq"""
class _user(_types): pass

int		= _buildinNumber('int')                                                 # pragma: no mutate
float	= _buildinNumber('float')                                               # pragma: no mutate
string 	= _buildin('string')                                                    # pragma: no mutate
