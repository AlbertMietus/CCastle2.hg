# (C) Albert Mietus, 2023. Part of Castle/CCastle project

"""This file contains AIGR-classes to model (all kind of) NameSpaces.

There are several NameSpaces: the most prominent one is the ``Source_NS``, roughly the file that contains the (Castle) code.
"""

from __future__ import annotations
import typing as PTH                                                                                  # Python TypeHints
from enum import Enum
from dataclasses import dataclass, KW_ONLY
from dataclasses import field as dc_field

from . import AIGR

class NameSpace(AIGR): pass
class Source_NS(NameSpace): pass
