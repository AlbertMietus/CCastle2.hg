# (C) Albert Mietus, 2025. Part of Castle/CCastle project

import logging; logger = logging.getLogger(__name__)
import pytest

from pathlib import Path

from castle import aigr
from castle.aigr import ID
from castle.writers import RPy
from castle.writers.RPy.writer import Renderer


from ..verify import *
from .. import my_renderer, verify_line_by_line

pytestmark = pytest.mark.xfail(reason="Rendering.Call ness the new 'Bundler'", allow_module_level=True) #type: ignore
