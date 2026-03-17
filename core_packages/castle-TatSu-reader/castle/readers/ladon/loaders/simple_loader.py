# (C) Albert Mietus, 2026. Part of Castle/CCastle project
import logging; logger = logging.getLogger(__name__)

import typing as PTH                                       # Python TypeHints
from pathlib import Path
import importlib

from ._base_loader import _FileLoader

class SimpleFileLoader(_FileLoader):
    def __init__(self, file:PTH.Optional[Path], **kw):
        super().__init__(**kw)
        self._source     = Path(file)

class PyModuleLoader(_FileLoader):
    """Load a Castlefile, which is distributed in a pythonPackae"""
    def __init__(self, module:str, file:str, **kw):
        super().__init__(**kw)
        mod = importlib.import_module(module)
        self._source = Path(mod.__path__[0]) / file
