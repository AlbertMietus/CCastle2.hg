# (C) Albert Mietus, 2024. Part of Castle/CCastle project

import pytest

from castle.aigr_extra.blend import mangle_event_handler

def test_typical():
    mix = mangle_event_handler(protocol='P', event='E', port='p')
    assert mix == "P_E__p"

def test_veryDefault_None():
    mix = mangle_event_handler(protocol=None, event=None, port=None)
    assert mix == "default_default__default"

def test_veryDefault_Empty():
    mix = mangle_event_handler(protocol='', event='', port='')
    assert mix == "default_default__default"
