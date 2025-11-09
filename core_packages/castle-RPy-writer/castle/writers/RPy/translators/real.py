# (C) Albert Mietus, 2025. Part of Castle/CCastle project

import logging; logger = logging.getLogger(__name__)
import typing as PTH                                                                                  # Python TypeHints

from . import base

class Compile(base.RPY_Translator):
    def runner(self):
        return self.process([self.RPYTHON, '--batch', f'--output={self.into}', self.driver+'.py'], )

class Execute(base.RPY_Translator):
    def runner(self):
        return self.process([f"./{self.into}"])
