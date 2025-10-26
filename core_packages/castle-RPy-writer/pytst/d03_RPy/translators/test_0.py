# (C) Albert Mietus, 2025. Part of Castle/CCastle project

import logging; logger = logging.getLogger(__name__)
import pytest

from castle.writers.RPy import translators


_FLAG_ABC = f"DUMMY_ABC_{id(object)}"
_FLAG_RPY = f"DUMMY_RPY_{id(object)}"

class Dummy_ABC(translators.base.TranslatorCommand):
    def runner(self): #called via execute()
        return _FLAG_ABC

class Dummy_RPY(translators.base.RPY_Translator):
    def __init__(self, **kwargs):
        super().__init__(driver=None, **kwargs)

    def runner(self): #called via execute()
        return _FLAG_RPY

class Dummy_ls(translators.base.RPY_Translator):
    def __init__(self, **kwargs):
        super().__init__(driver=None, **kwargs)

    def runner(self): #called via execute()
        return self.process(cmd=['ls', '-l'])

def test_1_ABC():
    r = Dummy_ABC()
    assert r.execute() == _FLAG_ABC

def test_2_Base():
    r = Dummy_RPY()
    assert r.execute() == _FLAG_RPY

def test_2a_ls():
    r = Dummy_ls()
    assert 'pytst' in r.execute()

def test_2b_ls():
    r = Dummy_ls(inDir='pytst/d03_RPy/translators/') # this dir
    assert 'test_0' in r.execute()
