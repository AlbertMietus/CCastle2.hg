# (C) Albert Mietus, 2023-2024. Part of Castle/CCastle project

from typing import TYPE_CHECKING

from .names import *
if TYPE_CHECKING:
    from .names import ID # import ID  explicit, so that basedpyright knows ID
from .AIGR import *
from .types import *

from . import errors # always use them as errors.XXXXX
