# (C) Albert Mietus, 2026. Part of Castle/CCastle project
import logging; logger = logging.getLogger(__name__)

import typing as PTH                                       # Python TypeHints
from pathlib import Path


from ._base_loader import _FileLoader

class SimpleFileLoader(_FileLoader):
    def __init__(self, file:PTH.Optional[Path], **kw):
        super().__init__(**kw)
        self._file     = Path(file)

