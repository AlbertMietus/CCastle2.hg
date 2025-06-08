# (C) Albert Mietus, 2025. Part of Castle/CCastle project

import logging; logger = logging.getLogger(__name__)
import pytest

from castle.writers.RPy.writers import Renderer, Machinery

from .verify import *

@pytest.fixture
def my_renderer() ->Renderer:
    return Renderer()

@pytest.fixture
def chainDict_renderer() ->Renderer:
    r =  Renderer(machinery=Machinery(hint="chained_dict"))
    logger.info("Using 'chained_dict' Machinery for Renderer: %s", r)
    return r

