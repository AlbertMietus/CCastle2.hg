# (C) Albert Mietus, 2025. Part of Castle/CCastle project

import logging; logger = logging.getLogger(__name__)
import pytest

from pathlib import Path

from castle import aigr
from castle.writers import RPy
from castle.writers.RPy.writer import Renderer
from castle.aigr_extra.scaffolding import  ScaffolderNameSpace

from ..verify import *
from .. import my_renderer, verify_line_by_line

def verify_file(expect: str, file: Path|str):
    if isinstance(file, str):
        file = Path(file)
    logger.info("read from: %s", file)
    assert file.is_file()
    verify_line_by_line(expect, file.read_text())
