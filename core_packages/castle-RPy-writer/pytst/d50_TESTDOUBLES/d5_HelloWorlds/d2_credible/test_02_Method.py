# (C) Albert Mietus, 2025,2026 Part of Castle/CCastle project

import logging; logger = logging.getLogger(__name__)
import pytest

from . import *
from . import credible, wrapped_Hello_World

def test_1_method_HW(wrapped_Hello_World, my_renderer):
    expected ="""\
def HelloWorld(self, label):
    print("Hello %s World" % (label,))
\n""" #Same as for elemental
    m1 = wrapped_Hello_World.search('Credible.HelloWorld')
    txt=my_renderer.render(m1)
    verify_line_by_line(expected, txt)

def test_2_method_init(wrapped_Hello_World, my_renderer):
    """//CastleCode
    init() {
       .credible := Credible();
    }"""
    expected ="""\
def _castle_init(self):
    self.credible = CC_Credible()
\n"""
    m1 = wrapped_Hello_World.search('Credible_HelloWorld.init')
    txt=my_renderer.render(m1)
    verify_line_by_line(expected, txt)
    logger.warning("""This init works, but may be conflicting with
    pytst/d50_TESTDOUBLES/d5_HelloWorlds/d2_credible/test_12_file.py
    See the remark on "`__init__` // _castle_init` mismatch""")



