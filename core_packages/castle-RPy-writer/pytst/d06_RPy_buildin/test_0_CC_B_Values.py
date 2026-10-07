# (C) Albert Mietus, 2026. Part of Castle/CCastle project
import logging; logger = logging.getLogger(__name__)

import pytest


from castle.writers.RPy_buildin import buildin

def test_0():
    """To kick-off: unboxing an boxed (int) value gives the value"""
    i = 42 # random it
    assert buildin.CC_B_int.unbox(buildin.CC_B_int(i)) == i

def test_UnBoxBoxed_is_equeal__forAllTypes():
    template = "buildin.CC_B_{T}.unbox(buildin.CC_B_{T}({V}))"
    for T, v in [
            ('int', 	42),
            ('float', 42.0),
            ('string', ("'forty-two'", "forty-two")), # format/eval will forget the quotes
            ('boolean', True),
            ('boolean', False),
            ]:
        val, exp = (v[0], v[1]) if isinstance(v, (tuple, list)) else (v,v)
        code= template.format(T=T, V=val) # BUG
        got = eval(code)
        assert got == exp, f"{code} is not {v}"
