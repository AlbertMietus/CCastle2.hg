# (C) Albert Mietus, 2025. Part of Castle/CCastle project

import logging; logger = logging.getLogger(__name__)
import typing as PTH                                                                                  # Python TypeHints

from . import base

exe    = 'main_HW'
driver = f'{exe}.py'

class Compile(base.RPY_Translator):
    def runner(self):
        return self.process([self.RPYTHON, '--no-pdb', f'--output={exe}', driver], PATH_prefix=str(self.PyPy_BINd),)

class Execute(base.RPY_Translator):
    def runner(self):
        return self.process(["./"+exe])
