# (C) Albert Mietus, 2025. Part of Castle/CCastle project

import logging; logger = logging.getLogger(__name__)
import typing as PTH                                                                                  # Python TypeHints

import pytest

from castle.writers.RPy.writer import Renderer, Machinery


@pytest.fixture
def my_renderer() ->Renderer:
    r = Renderer()
    return r

@pytest.fixture
def bundle_renderer(my_renderer):
    from castle.writers.RPy.writer.machinery.native_bundler import NativeBundler
    b = my_renderer.machinery.arg_bundler
    b = PTH.cast(NativeBundler, b)
    b.force_bundling = True # type:ignore
    logger.info("bundle_renderer:: Set force_bundling to: %s", b.force_bundling)
    return my_renderer


@pytest.fixture
def chainDict_renderer() ->Renderer:
    r =  Renderer(machinery=Machinery(hint="chained_dict")) # type: ignore
    logger.debug("Using 'chained_dict' Machinery for Renderer: %s", r)
    return r

