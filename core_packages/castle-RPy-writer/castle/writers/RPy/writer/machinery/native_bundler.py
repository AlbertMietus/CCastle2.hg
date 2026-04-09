# (C) Albert Mietus, 2026. Part of Castle/CCastle project
import logging; logger = logging.getLogger(__name__)
import typing as PTH

from castle.writers.RPy.aid import Block, TextBlock
from . import Bundler, ArgumentList, Signature

class NativeBundler(Bundler):

    def pack(self, arguments:ArgumentList, signature:Signature) -> TextBlock:
        return ""

    def unpack(self, signature:Signature) -> TextBlock:
        return ""
