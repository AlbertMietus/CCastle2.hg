# (C) Albert Mietus, 2026. Part of Castle/CCastle project
import logging; logger = logging.getLogger(__name__)

import pytest
import inspect

from castle.aigr import types as CCTypes

from castle.writers.RPy.writer import portray
from castle.writers.RPy_buildin.buildin import CC_B_Values


def all_CC_B_classes():
    """Discover all CC_B_* classes from CC_B_Values, except the base CC_B_Value"""
    return {name.removeprefix('CC_B_'): cls
            for name, cls in inspect.getmembers(CC_B_Values, inspect.isclass)
            if name.startswith('CC_B_') and name != 'CC_B_Value'}

def all_buildin_types():
    """Discover all _buildin instances from CCTypes"""
    return {t.represents: t
            for t in vars(CCTypes).values()
            if isinstance(t, CCTypes._buildin)}


def test_all_buildin_types_have_CC_B_class():
    cc_b = all_CC_B_classes()
    for represents, t in all_buildin_types().items():
        assert represents in cc_b, \
            f"CCTypes has '{represents}' but no CC_B_{represents} class found in CC_B_Values"

def test_all_CC_B_classes_have_buildin_type():
    buildin = all_buildin_types()
    for represents, cls in all_CC_B_classes().items():
        assert represents in buildin, \
            f"CC_B_Values has CC_B_{represents} but no matching CCTypes._buildin('{represents}') found"
