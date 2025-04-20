# (C) Albert Mietus, 2025. Part of Castle/CCastle project

import logging; logger = logging.getLogger(__name__)
import typing as PTH                                                                                  # Python TypeHints

from . import base


class Evaluate(base.RPY_Translator):
    def runner(self):
        main = self.driver+".py"
        return self.process(cmd=["python", main])
